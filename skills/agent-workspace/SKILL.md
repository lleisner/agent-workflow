---
name: agent-workspace
description: Adapt an existing repository or prepare a new practice workspace for an agent workflow by mapping authoritative records, permissions, allowances, GitHub tracking and worktrees. Use for project onboarding or workflow setup; do not reorganize a repository merely because agents will work in it.
---

# Agent workspace

Inspect before creating. Read AGENTS.md, README, the current plan and development
instructions; check Git status, branch, remotes and existing worktrees. Preserve
ongoing work and ownership. Reuse existing documents and tracking conventions.

## Establish the project agreement

Read [the agreement guide](references/agreement.md). Identify the actual goals,
record locations, role ownership, canonical document reference, task tracker,
integration targets, authority and allowances. Ask about consequential gaps only.
The hierarchy skill needs these answers, not particular filenames.

For a new synthetic workspace, adapt assets/project.json and
assets/WORKFLOW.md. They are optional starter assets, not an automatic migration.
Keep AGENTS.md short and point it to the agreement. Do not copy live project data
into a reusable template or overwrite existing instructions.

Start small. Combined roles may share a workspace/integration stage. Each
independent writer or integrator normally gets an isolated worktree. Organize by
stable area, task and assignment, using container directories outside the source
checkout; leaf directories are worktrees.

## Connect tools

- Use GitHub issues/comments for live state when that is the project's chosen
  tracker. Distinguish coordination issues from executable tasks.
- Use one canonical published home for durable plans/decisions; keep code-specific
  docs with their implementation. A common branch does not imply a shared writable
  checkout or an EL who transcribes every record.
- Use scripts/worktree.py for explicit creation of an owned workspace,
  or use native Git directly. It never cleans or deletes worktrees.
- Optional scripts/validate_project.py checks the supplied JSON mapping and local
  path safety. It cannot establish that remote records are current or permissions
  have actually been granted.

## Ready to use

Record the resolved mapping, review/integration gates, initial model/allowance
settings, session operations and validation commands. Missing start authority or
allowance must be resolved before dispatch. Missing merge permission means human
approval. Treat runtime capabilities as observed facts or explicit unknowns.

Provide a short setup result with record references and the next action. The
companion agent-hierarchy and agent-task skills are optional independent consumers
of this agreement.
