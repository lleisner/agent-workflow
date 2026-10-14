import importlib.util
import json
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile
import unittest

try:
    import tomllib
except ImportError:
    tomllib = None

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills/agent-hierarchy'
spec = importlib.util.spec_from_file_location('profiles', SKILL / 'scripts/profiles.py')
profiles = importlib.util.module_from_spec(spec)
spec.loader.exec_module(profiles)


class ProfileAssemblyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.skill = Path(self.temp.name)
        self.sources = self.skill / 'references/profile-sources'
        self.sources.mkdir(parents=True)
        self.parts = {'common.md': 'Common instructions.', 'upper.md': 'Upper responsibility.',
                      'lower.md': 'Lower responsibility.', 'combined.md': 'Combined transfer.'}
        for name, text in self.parts.items():
            (self.sources / name).write_text(text)
        self.manifest = [
            dict(name='lower', description='Lower role', reasoning_effort='high',
                 sources=['common.md', 'lower.md']),
            dict(name='combined', description='Both roles', reasoning_effort='xhigh',
                 sources=['common.md', 'upper.md', 'lower.md', 'combined.md']),
        ]
        self.save_manifest()

    def save_manifest(self):
        (self.sources / 'profiles.json').write_text(json.dumps(self.manifest))

    def test_composition_is_ordered_complete_and_deterministic(self):
        actual = profiles.render_profiles(self.skill)
        self.assertEqual(actual, profiles.render_profiles(self.skill))
        self.assertNotIn('Upper responsibility.', actual['lower.toml'])
        combined = actual['combined.toml']
        expected = '\n\n'.join(self.parts.values())
        self.assertIn(expected, combined)
        self.assertEqual(combined.count('Common instructions.'), 1)

    def test_shared_edit_reaches_both_outputs_without_editing_roles(self):
        before = profiles.render_profiles(self.skill)
        (self.sources / 'common.md').write_text('Revised shared instructions.')
        after = profiles.render_profiles(self.skill)
        for filename in before:
            self.assertNotEqual(before[filename], after[filename])
            self.assertIn('Revised shared instructions.', after[filename])
        self.assertEqual((self.sources / 'lower.md').read_text(), self.parts['lower.md'])

    def test_check_is_read_only_and_write_is_idempotent(self):
        self.assertTrue(profiles.check_profiles(self.skill))
        self.assertFalse((self.skill / 'assets').exists())
        profiles.write_profiles(self.skill)
        self.assertEqual(profiles.check_profiles(self.skill), [])
        path = self.skill / 'assets/agents/combined.toml'
        before = path.stat().st_mtime_ns
        profiles.write_profiles(self.skill)
        self.assertEqual(path.stat().st_mtime_ns, before)
        path.write_text('edited')
        self.assertTrue(profiles.check_profiles(self.skill))
        self.assertEqual(path.read_text(), 'edited')

    def test_invalid_manifest_cannot_partially_write(self):
        for field, value in [('name', '../escape'), ('name', 'worker'), ('description', ''),
                             ('reasoning_effort', 'bogus'), ('sources', []),
                             ('sources', ['common.md', 'common.md']),
                             ('sources', ['../escape.md'])]:
            with self.subTest(field=field, value=value):
                old = self.manifest[1][field]
                self.manifest[1][field] = value
                self.save_manifest()
                with self.assertRaises(ValueError):
                    profiles.write_profiles(self.skill)
                self.assertFalse((self.skill / 'assets').exists())
                self.manifest[1][field] = old
        self.manifest[1]['name'] = 'lower'
        self.save_manifest()
        with self.assertRaises(ValueError):
            profiles.render_profiles(self.skill)

    def test_unknown_settings_rejected_and_missing_sources_do_not_write(self):
        self.manifest[1]['sandbox_mode'] = 'danger-full-access'
        self.save_manifest()
        with self.assertRaises(ValueError):
            profiles.write_profiles(self.skill)
        del self.manifest[1]['sandbox_mode']
        self.save_manifest()
        (self.sources / 'lower.md').unlink()
        with self.assertRaises(OSError):
            profiles.write_profiles(self.skill)
        self.assertFalse((self.skill / 'assets').exists())

    def test_unrecognized_assets_and_symlinks_are_preserved(self):
        profiles.write_profiles(self.skill)
        unknown = self.skill / 'assets/agents/other.toml'
        unknown.write_text('user material')
        with self.assertRaises(ValueError):
            profiles.write_profiles(self.skill)
        self.assertEqual(unknown.read_text(), 'user material')
        unknown.unlink()
        path = self.skill / 'assets/agents/lower.toml'
        path.unlink()
        target = self.skill / 'outside.toml'
        target.write_text('unchanged')
        path.symlink_to(target)
        with self.assertRaises(ValueError):
            profiles.write_profiles(self.skill)
        self.assertEqual(target.read_text(), 'unchanged')

    @unittest.skipIf(tomllib is None, 'TOML roundtrip requires Python 3.11+')
    def test_toml_roundtrip_preserves_quotes_unicode_and_literal_escapes(self):
        content = 'Literal \\n, \\t, """, café, \\ and\nsecond line\tend'
        (self.sources / 'lower.md').write_text(content, encoding='utf-8')
        self.manifest[0]['reasoning_effort'] = None
        self.save_manifest()
        parsed = tomllib.loads(profiles.render_profiles(self.skill)['lower.toml'])
        self.assertEqual(parsed['developer_instructions'], self.parts['common.md'] + '\n\n' + content + '\n')
        self.assertEqual(set(parsed), {'name', 'description', 'developer_instructions'})

    @unittest.skipIf(tomllib is None, 'TOML roundtrip requires Python 3.11+')
    def test_real_profiles_settings_and_single_combined_consistency(self):
        rendered = {name: tomllib.loads(value) for name, value in profiles.render_profiles(SKILL).items()}
        expected = dict(user_liaison='xhigh', project_lead=None, execution_lead='xhigh',
                        area_coordinator='high', task_coordinator='high', workflow_worker='medium',
                        integration_reviewer='medium', project_execution_lead='xhigh', area_task_coordinator='high')
        self.assertEqual(set(rendered), {name + '.toml' for name in expected})
        for name, effort in expected.items():
            data = rendered[name + '.toml']
            self.assertEqual(data['name'], name)
            self.assertEqual(data.get('model_reasoning_effort'), effort)
            self.assertNotIn('service_tier', data)
            self.assertNotIn('model', data)
            self.assertNotIn('sandbox_mode', data)
            self.assertNotIn('approval_policy', data)
        for upper, lower, combined in [('project_lead', 'execution_lead', 'project_execution_lead'),
                                       ('area_coordinator', 'task_coordinator', 'area_task_coordinator')]:
            for name in (upper, lower):
                role_text = (SKILL / 'references/profile-sources' / (name + '.md')).read_text().strip()
                self.assertIn(role_text, rendered[combined + '.toml']['developer_instructions'])

    def test_copied_skill_checks_without_source_repository(self):
        copied = self.skill / 'installed-skill'
        shutil.copytree(SKILL, copied, ignore=shutil.ignore_patterns('__pycache__'))
        run = subprocess.run([sys.executable, str(copied / 'scripts/profiles.py'), '--check'],
                             cwd=self.skill, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)

    def test_bundled_assets_and_cli_check(self):
        self.assertEqual(profiles.check_profiles(SKILL), [])
        run = subprocess.run([sys.executable, str(SKILL / 'scripts/profiles.py'), '--check'],
                             capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)


if __name__ == '__main__':
    unittest.main()
