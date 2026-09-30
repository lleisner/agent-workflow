#!/usr/bin/env python3
"""Dependency-free package checks; does not execute agents or remote writes."""
import ast
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
errors = []
skills = sorted(p for p in (ROOT / "skills").iterdir() if p.is_dir())
for skill in skills:
    doc = (skill / "SKILL.md").read_text()
    if not doc.startswith("---\n") or "\n---\n" not in doc[4:]:
        errors.append(str(skill) + ": missing frontmatter")
        continue
    front = doc.split("---", 2)[1]
    if "name: " + skill.name not in front or "description: " not in front:
        errors.append(str(skill) + ": invalid name/description")
    metadata = (skill / "agents/openai.yaml").read_text()
    if "$" + skill.name not in metadata:
        errors.append(str(skill) + ": default prompt missing skill invocation")
    for path in skill.rglob("*"):
        if path.suffix == ".py":
            ast.parse(path.read_text(), filename=str(path))
        if path.suffix not in (".md", ".json", ".yaml", ".py"):
            continue
        text = path.read_text()
        if "/Users/" in text or "tmp-agent-comms" in text:
            errors.append(str(path) + ": private source path")
        if path.suffix == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if "://" not in target and not target.startswith("#"):
                    if not (path.parent / target.split("#")[0]).is_file():
                        errors.append(str(path) + ": missing link " + target)
            for ref in re.findall(r"\bscripts/([a-z_]+\.py)", text):
                if not (skill / "scripts" / ref).is_file():
                    errors.append(str(path) + ": missing script " + ref)
    for path in skill.rglob("*.json"):
        json.loads(path.read_text())
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print(f"Validated {len(skills)} skill packages, bundled references and Python syntax.")
