import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(skill, name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "skills" / skill / "scripts" / (name + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


allowance = load("agent-hierarchy", "allowance")
session = load("agent-hierarchy", "session")
worktree = load("agent-workspace", "worktree")
mapping = load("agent-workspace", "validate_project")
github = load("agent-task", "github_records")


class AllowanceTests(unittest.TestCase):
    def setUp(self):
        self.data = allowance.new_ledger("project", 10, {
            "source": "synthetic", "date": "2026-09-30",
            "models": {"test": {"input": 1, "cached_input": .1, "output": 4}}})

    def observe(self, scope, name, n=1_000_000, **kwargs):
        allowance.observe(self.data, scope, name, "test",
                          {"input": n, "cached_input": n//2, "output": n//10,
                           "reasoning_output": n//20}, **kwargs)

    def test_rollup_and_snapshots_charge_categories_once(self):
        allowance.allocate(self.data, "project", "EL", 6, "grant")
        allowance.allocate(self.data, "EL", "helper", 2, "grant")
        self.observe("EL", "parent")
        self.observe("helper", "child")
        self.observe("helper", "child")
        self.assertAlmostEqual(allowance.spent(self.data, "project"), 1.9)
        self.assertAlmostEqual(allowance.spent(self.data, "EL"), 1.9)
        self.assertAlmostEqual(allowance.committed(self.data, "EL"), 2.95)
        self.assertAlmostEqual(allowance.committed(self.data, "project"), 6)

    def test_reallocation_requires_releasing_reservation(self):
        allowance.allocate(self.data, "project", "A", 7, "grant")
        with self.assertRaises(ValueError):
            allowance.allocate(self.data, "project", "B", 4, "grant")
        allowance.set_limit(self.data, "A", 6, "release")
        allowance.allocate(self.data, "project", "B", 4, "grant")
        self.observe("A", "a")
        with self.assertRaises(ValueError):
            allowance.set_limit(self.data, "A", .1, "invalid")

    def test_overrun_recorded_and_replacements_add(self):
        allowance.allocate(self.data, "project", "A", 1, "grant")
        self.observe("A", "old")
        self.observe("A", "replacement")
        summary = allowance.report(self.data)
        self.assertEqual(summary["scopes"]["A"]["status"], "exhausted")
        self.assertAlmostEqual(summary["scopes"]["project"]["observed_spend"], 1.9)
        self.assertAlmostEqual(summary["scopes"]["project"]["committed"], 1.9)

    def test_unknown_and_identity(self):
        allowance.register(self.data, "project", "new", "test")
        self.assertEqual(allowance.report(self.data)["unknown_sessions"], ["new"])
        self.observe("project", "new")
        with self.assertRaises(ValueError):
            self.observe("project", "new", speed=2)
        with self.assertRaises(ValueError):
            self.observe("project", "new", n=1)
        self.assertAlmostEqual(allowance.spent(self.data, "project"), .95)

    def test_invalid_categories_and_amounts(self):
        for n in (-1, float("nan"), float("inf"), True):
            with self.assertRaises(ValueError):
                allowance.set_limit(self.data, "project", n, "invalid")
        with self.assertRaises(ValueError):
            allowance.observe(self.data, "project", "x", "test",
                              dict(input=1, cached_input=2, output=3, reasoning_output=0))
        self.assertNotIn("x", self.data["sessions"])

    def test_reclassification_cannot_refund_observed_usage(self):
        self.observe("project", "x")
        with self.assertRaises(ValueError):
            allowance.observe(self.data, "project", "x", "test",
                              dict(input=1_000_000, cached_input=900_000,
                                   output=100_000, reasoning_output=50_000))
        self.assertAlmostEqual(allowance.spent(self.data, "project"), .95)

    def test_cli_persistence_and_no_reset(self):
        with tempfile.TemporaryDirectory() as d:
            ledger, rates = Path(d)/"ledger.json", Path(d)/"rates.json"
            rates.write_text(json.dumps(self.data["rates"]))
            cmd = ["python3", allowance.__file__, "init", "--ledger", str(ledger),
                   "--scope", "project", "--limit", "10", "--rates", str(rates)]
            subprocess.run(cmd, check=True, capture_output=True)
            self.assertEqual(json.loads(ledger.read_text())["scopes"], self.data["scopes"])
            self.assertNotEqual(subprocess.run(cmd, capture_output=True).returncode, 0)


class SessionTests(unittest.TestCase):
    def test_usage_extracts_cumulative_not_increment_and_no_transcript(self):
        counters = dict(input_tokens=100, cached_input_tokens=80,
                        output_tokens=20, reasoning_output_tokens=15)
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/"usage.jsonl"
            path.write_text(json.dumps({"type": "message", "payload": {"text": "private"}}) + "\n" +
                json.dumps({"type": "token_usage_record", "timestamp": "now", "payload": {
                    "thread_id": "test", "usage": {"input_tokens": 1},
                    "thread_token_usage": counters}}) + "\n" + '{"partial":')
            result = session.usage(path)
            self.assertEqual(result["counters"], counters)
            self.assertNotIn("private", json.dumps(result))

    def test_usage_unknown_or_cache_write_fails(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/"usage.jsonl"
            path.write_text('{"type":"message"}\n')
            with self.assertRaises(ValueError):
                session.usage(path)
            path.write_text(json.dumps({"type":"token_usage_record", "payload":{
                "thread_token_usage": dict(input_tokens=10, cached_input_tokens=0,
                    output_tokens=2, reasoning_output_tokens=0, cache_write_input_tokens=3)}}))
            with self.assertRaises(ValueError):
                session.usage(path)

    def test_legacy_counter_keeps_known_thread_identity(self):
        counters = dict(input_tokens=10, cached_input_tokens=8,
                        output_tokens=2, reasoning_output_tokens=0)
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)/"usage.jsonl"
            path.write_text(json.dumps({"type":"session_meta","payload":{"id":"thread"}}) + "\n" +
                            json.dumps({"type":"event_msg","payload":{"type":"token_count",
                                "info":{"total_token_usage":counters}}}) + "\n")
            self.assertEqual(session.usage(path)["thread_id"], "thread")

    def test_rename_checks_project_before_mutation(self):
        class FakeClient:
            def __init__(self, cwd):
                self.data = {"cwd": str(cwd), "name": "old"}
                self.mutations = 0
            def write(self, value):
                pass
            def rpc(self, method, params):
                if method == "thread/read":
                    return {"thread": dict(self.data)}
                if method == "thread/name/set":
                    self.mutations += 1
                    self.data["name"] = params["name"]
                return {}
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            client = FakeClient(root/"work")
            self.assertEqual(session.rename(client, "id", root, "TC1 · PCT001")["name"], "TC1 · PCT001")
            client = FakeClient(root.parent)
            with self.assertRaises(ValueError):
                session.rename(client, "id", root, "new")
            self.assertEqual(client.mutations, 0)


class WorktreeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.repo = self.root/"repo"
        self.repo.mkdir()
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        worktree.git(self.repo, "config", "user.name", "Test")
        worktree.git(self.repo, "config", "user.email", "test@example.invalid")
        (self.repo/"file").write_text("baseline")
        worktree.git(self.repo, "add", "file")
        worktree.git(self.repo, "commit", "-qm", "baseline")

    def create(self, **kwargs):
        params = dict(repo=self.repo, root=self.root/"worktrees", area="export",
                      task="PCT001", assignment="W1", base="HEAD", branch="task/PCT001-W1")
        params.update(kwargs)
        return worktree.create(**params)

    def test_isolated_leaf_preserves_dirty_source(self):
        (self.repo/"file").write_text("existing user work")
        result = self.create()
        path = Path(result["path"])
        self.assertEqual((path/"file").read_text(), "baseline")
        (path/"file").write_text("worker")
        self.assertEqual((self.repo/"file").read_text(), "existing user work")
        self.assertFalse((path.parent/".git").exists())
        with self.assertRaises(ValueError):
            self.create()

    def test_rejects_nested_traversal_and_symlink_paths(self):
        with self.assertRaises(ValueError):
            self.create(root=self.repo/"worktrees")
        with self.assertRaises(ValueError):
            self.create(area="../other")
        outside = self.root/"outside"
        outside.mkdir()
        container = self.root/"worktrees"
        container.mkdir()
        (container/"export").symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.create()


class MappingTests(unittest.TestCase):
    def test_custom_mapping_and_ungranted_example(self):
        data = json.loads((ROOT/"skills/agent-workspace/assets/project.json").read_text())
        data["records"]["overview"] = "existing/custom-plan.md"
        errors, warnings = mapping.validate(data)
        self.assertFalse(errors)
        self.assertTrue(any("not permission" in w for w in warnings))
        data["records"]["decisions"] = "../private.md"
        self.assertTrue(mapping.validate(data)[0])
        self.assertTrue(mapping.validate([])[0])


class FakeGitHub:
    def __init__(self):
        self.issues, self.comments, self.writes = [], [], []
    def pages(self, path):
        return copy.deepcopy(self.comments if path.endswith("/comments") else self.issues)
    def api(self, method, path, data):
        self.writes.append((method, path, data))
        if "/comments" in path:
            if method == "POST":
                result = dict(data, id=101, html_url="https://example.invalid/comment/101")
                self.comments.append(result)
            else:
                result = self.comments[0]
                result.update(data)
        else:
            if method == "POST":
                result = dict(data, number=7, html_url="https://example.invalid/issues/7")
                self.issues.append(result)
            else:
                result = self.issues[0]
                result.update(data)
        return copy.deepcopy(result)


class GitHubTests(unittest.TestCase):
    def test_task_retry_preserves_updated_record(self):
        api = FakeGitHub()
        result = github.create_task(api, "owner/repo", "PCT", "export", "Export", "scope")
        self.assertEqual(result["task_id"], "PCT007")
        api.issues[0]["body"] += "\nEdited acceptance"
        result = github.create_task(api, "owner/repo", "PCT", "export", "Export", "stale body")
        self.assertFalse(result["created"])
        self.assertEqual(len(api.issues), 1)
        self.assertIn("Edited acceptance", api.issues[0]["body"])

    def test_report_update_stable_link_and_duplicate_error(self):
        api = FakeGitHub()
        first = github.report(api, "owner/repo", 7, "W1", "initial")
        second = github.report(api, "owner/repo", 7, "W1", "complete")
        self.assertEqual(first["url"], second["url"])
        self.assertEqual(len(api.comments), 1)
        self.assertIn("complete", api.comments[0]["body"])
        api.comments.append(dict(api.comments[0], id=102))
        with self.assertRaises(ValueError):
            github.report(api, "owner/repo", 7, "W1", "another")

    def test_pagination_reads_beyond_first_page(self):
        class Pages(github.GitHub):
            def api(self, method, path, data=None):
                return [{"id": i} for i in range(100)] if path.endswith("page=1") else [{"id":100}]
        self.assertEqual(len(Pages().pages("repos/x/y/issues?state=all")), 101)

    def test_invalid_body_and_key_never_write(self):
        api = FakeGitHub()
        for key, body in (("W1", ""), ("../W1", "report"), ("W1", "<!-- agent-workflow:report:W2 -->")):
            with self.assertRaises(ValueError):
                github.report(api, "owner/repo", 7, key, body)
        self.assertFalse(api.writes)


if __name__ == "__main__":
    unittest.main()
