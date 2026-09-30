# Agent Workflow

An experimental skill collection for human-directed agent teams. Persistent
roles provide continuity; the agents occupying them can change. Coordinators
exercise judgment within explicit scope, permissions and resource allowances.

## Installable skills

| Skill | Use |
| --- | --- |
| agent-hierarchy | Establish, operate, split or resume PL, EL, AC, TC, W and S roles. |
| agent-workspace | Adapt an existing project or prepare a practice workspace for the hierarchy. |
| agent-task | Define, claim, report, review and integrate a bounded deliverable. |

The hierarchy and project workflow can be used independently. An existing
repository supplies its own record locations and conventions through a small
project agreement. No orchestration service or MCP server is required.

## Install

Ask Codex's skill installer:

> Install agent-hierarchy, agent-workspace and agent-task from
> lleisner/agent-workflow, using their directories under skills/.

Install a tested tag or commit on each machine when reproducibility matters.
Each skill includes its own references and helpers; do not install only SKILL.md.
For local development, Codex also supports linking skill directories into its
user skill discovery directory. Avoid installing duplicate copies with the same
skill name.

The scripts require Python 3.9+, Git, and the GitHub CLI for GitHub operations.
The local allowance writer currently supports macOS/Linux file locking.
Codex session operations require a compatible, signed-in Codex CLI. Local skill
installation does not transfer running sessions, credentials or uncommitted code.
Host-specific behavior must be checked on each supported platform.

## Start

1. Invoke $agent-workspace in the intended project. Reuse its existing documents;
   settle only missing or contradictory settings.
2. Invoke $agent-hierarchy with a role and scope. Start small: combined PL+EL and
   AC+TC roles are valid. The project agreement points to the relevant records.
3. Use $agent-task for scoped deliverables. In a hierarchy a TC owns a task;
   in a solo workflow the current agent or human can own it.

Published plans and decisions have a canonical branch. Live task state and
concise reports use GitHub issues/comments in the supplied starter workflow.
Implementation branches contain code, evidence and working drafts.

## Maturity

This is a pilot implementation, not an assurance of unattended execution.
See [validation](docs/VALIDATION.md) for tested behavior and open runtime checks.
The skills express authority and budget rules; helpers do not enforce every
action the agent or its tools can take.

Fixed estimated-credit accounting includes all subordinate and helper usage.
Dynamic subscription optimization, extensive specialist libraries, automatic
skill improvement and a separate starter-template repository are later work.

The source repository and synthetic practice project are separate. Do not
publish project transcripts, private mappings, credentials or local ledgers here.

## Contribute and verify

Run:

~~~sh
python3 -m unittest discover -s tests -v
python3 scripts/validate.py
~~~

Use [the design](docs/DESIGN.md) for accepted behavior. Keep reusable instructions
separate from project-specific settings, and prefer bounded improvements based on
observed failures. License selection is pending; no open-source license is
asserted by this initial experimental publication.
