#!/usr/bin/env python3
"""Create one explicitly owned leaf worktree; never switch or clean checkouts."""
import argparse
import json
from pathlib import Path
import re
import subprocess


def git(repo, *args):
    return subprocess.check_output(["git", "-C", str(repo), *args], text=True).strip()


def create(repo, root, area, task, assignment, base, branch):
    repo = Path(git(repo, "rev-parse", "--show-toplevel")).resolve()
    root = Path(root).resolve()
    for segment in (area, task, assignment):
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", segment):
            raise ValueError("Area, task and assignment must be single safe path segments")
    if not base or base.startswith("-") or not branch or branch.startswith("-"):
        raise ValueError("Explicit base and branch required")
    git(repo, "check-ref-format", "--branch", branch)
    git(repo, "rev-parse", "--verify", base + "^{commit}")
    target = root / area / task / assignment
    if target.resolve() != target:
        raise ValueError("Worktree path traverses a symlink; choose its explicit canonical location")
    if target.exists() or target.is_symlink():
        raise ValueError("Target already exists; inspect and reuse explicitly")
    # Reject nesting inside any registered checkout, not just the caller's cwd.
    entries = git(repo, "worktree", "list", "--porcelain", "-z")
    checkouts = [Path(line[9:]).resolve() for line in entries.split("\0")
                 if line.startswith("worktree ")]
    for checkout in checkouts:
        if target == checkout or checkout in target.parents or target in checkout.parents:
            raise ValueError("Worktree must be outside existing checkouts")
    # Catch an unrelated repository in an organizational container.
    for parent in target.parents:
        if (parent / ".git").exists() or parent.name == ".git":
            raise ValueError("Worktree containers cannot be inside another repository")
    target.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["git", "-C", str(repo), "worktree", "add", "-b", branch,
                    str(target), base], check=True)
    return {"path": str(target), "branch": git(target, "branch", "--show-current"),
            "base": base, "head": git(target, "rev-parse", "HEAD")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("repo", "root", "area", "task", "assignment", "base", "branch"):
        parser.add_argument("--" + key, required=True)
    args = parser.parse_args()
    try:
        print(json.dumps(create(**vars(args)), indent=2))
    except (OSError, ValueError, subprocess.SubprocessError) as exc:
        parser.exit(1, "worktree: " + str(exc) + "\n")


if __name__ == "__main__":
    main()
