#!/usr/bin/env python3
"""Validate the optional starter mapping, not authorization or remote freshness."""
import argparse
import json
from pathlib import Path, PurePosixPath, PureWindowsPath
import re


def validate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["Mapping must be a JSON object"], []
    if data.get("schema_version") != 1:
        errors.append("schema_version must be 1")
    requirements = {
        "project": ("name", "prefix", "repository"),
        "records": ("canonical_ref", "overview", "decisions", "agreement", "roles", "tasks", "reports"),
        "branches": ("integration", "stable", "worktree_root"),
        "authority": ("status", "start", "worker_to_task", "task_to_area", "area_to_project", "promotion"),
        "resources": ("ledger", "model_policy", "dynamic_subscription"),
        "runtime": ("adapter", "visible_sessions", "helpers"),
    }
    for section, fields in requirements.items():
        obj = data.get(section)
        if not isinstance(obj, dict):
            errors.append("Missing mapping: " + section)
            continue
        for field in fields:
            value = obj.get(field)
            if field == "dynamic_subscription":
                if not isinstance(value, bool):
                    errors.append("resources.dynamic_subscription must be boolean")
            elif not isinstance(value, str) or not value.strip():
                errors.append(section + "." + field + " must be a nonempty string")
    if errors:
        return errors, warnings
    if not re.fullmatch(r"[A-Z][A-Z0-9]{1,11}", data["project"]["prefix"]):
        errors.append("Project prefix must be 2-12 uppercase letters/digits")
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", data["project"]["repository"]):
        errors.append("Repository must be OWNER/REPO")
    for key in ("overview", "decisions", "agreement", "roles"):
        value = data["records"][key].split("#", 1)[0]
        if value.startswith("https://"):
            continue
        if PurePosixPath(value).is_absolute() or PureWindowsPath(value).drive or ".." in value.replace("\\", "/").split("/"):
            errors.append("records." + key + " must be repo-relative or an HTTPS URL")
    if data["authority"]["status"] == "example-not-a-grant":
        warnings.append("Example settings are not permission to dispatch or merge")
    warnings.append("Validate actual grants, record existence and runtime separately")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mapping", type=Path)
    args = parser.parse_args()
    try:
        errors, warnings = validate(json.loads(args.mapping.read_text()))
        print(json.dumps({"errors": errors, "warnings": warnings}, indent=2))
        return bool(errors)
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(1, "mapping: " + str(exc) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
