#!/usr/bin/env python3
"""Small GitHub record operations. Coordinators serialize writes to each key."""
import argparse
import json
from pathlib import Path
import re
import subprocess

LABELS = {"aw:task": "1d76db", "aw:coordination": "5319e7", "aw:draft": "ededed",
          "aw:ready": "0e8a16", "aw:active": "fbca04", "aw:review": "d93f0b",
          "aw:paused": "b60205"}


def valid_repo(repo):
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
        raise ValueError("Repository must be OWNER/REPO")
    return repo


def marker(kind, key):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,99}", key) or "--" in key:
        raise ValueError("Record key must be a safe short identifier")
    return "<!-- agent-workflow:" + kind + ":" + key + " -->"


def body_text(body):
    if not body.strip() or "<!-- agent-workflow:" in body:
        raise ValueError("Body must be nonempty and contain no reserved record marker")
    return body.rstrip()


class GitHub:
    def api(self, method, path, data=None):
        cmd = ["gh", "api", "--method", method, path]
        if data is not None:
            cmd += ["--input", "-"]
        result = subprocess.run(cmd, input=None if data is None else json.dumps(data),
                                capture_output=True, text=True, check=True, timeout=60)
        return json.loads(result.stdout) if result.stdout.strip() else None

    def pages(self, path):
        result, page = [], 1
        sep = "&" if "?" in path else "?"
        while True:
            batch = self.api("GET", path + sep + "per_page=100&page=" + str(page))
            if not isinstance(batch, list):
                raise ValueError("Expected a paginated list")
            result.extend(batch)
            if len(batch) < 100:
                return result
            page += 1


def unique(records, token):
    matches = [record for record in records if token in (record.get("body") or "")]
    if len(matches) > 1:
        raise ValueError("Duplicate matching records; coordinator must reconcile them")
    return matches[0] if matches else None


def init_labels(api, repo):
    path = "repos/" + valid_repo(repo) + "/labels"
    existing = {label["name"] for label in api.pages(path)}
    created = []
    for name, color in LABELS.items():
        if name not in existing:
            api.api("POST", path, {"name": name, "color": color,
                                  "description": "Agent workflow " + name[3:]})
            created.append(name)
    return {"created": created}


def create_task(api, repo, prefix, key, title, body):
    path = "repos/" + valid_repo(repo) + "/issues"
    if not re.fullmatch(r"[A-Z][A-Z0-9]{1,11}", prefix) or not title.strip():
        raise ValueError("A project prefix and title are required")
    token, body = marker("task", key), body_text(body)
    record = unique([i for i in api.pages(path + "?state=all") if "pull_request" not in i], token)
    created = record is None
    if created:
        record = api.api("POST", path, {"title": title, "body": token + "\n\n" + body,
                                        "labels": ["aw:task", "aw:draft"]})
    task_id = prefix + str(record["number"]).zfill(3)
    # Recover the narrow create-then-title failure, without replacing edited bodies.
    if created or record["title"] == title:
        record = api.api("PATCH", path + "/" + str(record["number"]),
                         {"title": task_id + " " + title})
    return {"number": record["number"], "task_id": task_id,
            "url": record["html_url"], "created": created}


def report(api, repo, issue, key, body):
    if not isinstance(issue, int) or issue < 1:
        raise ValueError("Positive issue number required")
    root = "repos/" + valid_repo(repo)
    path = root + "/issues/" + str(issue) + "/comments"
    token, body = marker("report", key), body_text(body)
    existing = unique(api.pages(path), token)
    payload = {"body": token + "\n\n" + body}
    if existing:
        result = api.api("PATCH", root + "/issues/comments/" + str(existing["id"]), payload)
    else:
        result = api.api("POST", path, payload)
    return {"id": result["id"], "url": result["html_url"], "created": existing is None}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name in ("init-labels", "create-task", "report"):
        p = commands.add_parser(name)
        p.add_argument("--repo", required=True)
        if name != "init-labels":
            p.add_argument("--key", required=True)
            p.add_argument("--body-file", type=Path, required=True)
        if name == "create-task":
            p.add_argument("--prefix", required=True)
            p.add_argument("--title", required=True)
        if name == "report":
            p.add_argument("--issue", type=int, required=True)
    args = parser.parse_args()
    try:
        api = GitHub()
        if args.command == "init-labels":
            result = init_labels(api, args.repo)
        elif args.command == "create-task":
            result = create_task(api, args.repo, args.prefix, args.key, args.title, args.body_file.read_text())
        else:
            result = report(api, args.repo, args.issue, args.key, args.body_file.read_text())
        print(json.dumps(result, indent=2))
    except subprocess.CalledProcessError as exc:
        parser.exit(1, "github: " + (exc.stderr or str(exc)) + "\n")
    except (OSError, ValueError, KeyError, subprocess.TimeoutExpired) as exc:
        parser.exit(1, "github: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
