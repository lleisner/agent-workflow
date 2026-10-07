# Agent Workflow

An experimental skill collection for human-directed agent teams. Persistent
roles provide continuity; the agents occupying them can change. Coordinators
exercise judgment within explicit scope, permissions and resource allowances.

## Installable skills

| Skill | Use |
| --- | --- |
| agent-workflow | One guided setup/resume walkthrough, including workspace preparation and role handoff. |
| agent-hierarchy | Establish, operate, split or resume PL, EL, AC, TC, W and S roles. |
| agent-workspace | Adapt an existing project or prepare a practice workspace for the hierarchy. |
| agent-task | Define, claim, report, review and integrate a bounded deliverable. |

The hierarchy and project workflow can be used independently. An existing
repository supplies its own record locations and conventions through a small
project agreement. No orchestration service or MCP server is required.

## Install

Ask Codex's skill installer:

> Install agent-workflow, agent-hierarchy, agent-workspace and agent-task from
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

In a fresh session in the intended project, invoke **$agent-workflow** once.
The setup facilitator inspects the repository, guides only unresolved choices,
prepares the agreed workspace and tracker, and starts or reconnects the authorized
initial roles. It writes and delivers their focused handoffs and shows you which
contact is ready for your next project conversation. You do not compose launch
prompts or invoke the component skills in sequence.

The setup facilitator is temporary; PL and EL receive settled context instead of
inheriting the onboarding conversation. Repeat the same invocation to resume an
interrupted setup without duplicating roles or renewing allowances.

Install all four directories for this complete walkthrough. The three component
skills can still be installed and used independently for existing role operations,
workspace-only setup or solo task workflows. Existing project conventions remain
configurable, and combined PL+EL or AC+TC roles are valid.

Published plans and decisions have a canonical branch. Live task state and
concise reports use GitHub issues/comments in the supplied starter workflow.
Implementation branches contain code, evidence and working drafts.

## Maturity

This is a pilot implementation, not an assurance of unattended execution.
See [validation](docs/VALIDATION.md) for tested behavior and open runtime checks.
The skills express authority and budget rules; helpers do not enforce every
action the agent or its tools can take.

Allowances bound autonomous work and include its coordination and helper usage.
Setup and ordinary leadership conversations have no mandatory numeric cap; a
project-wide time-window allocation is optional. Estimated-credit accounting is
not an exact subscription percentage.
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
