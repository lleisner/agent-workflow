# Validation status

The v0.1.0 helper package passed local checks on 2026-09-30. A subsequent live pilot
reached leadership splitting and area planning, then entered a resource hold.
Implementation/review/integration and the complete hierarchy remain untested.
Unit tests establish helper behavior, not model judgment or unattended reliability.

## Guided onboarding update

The v0.2.0 instructions add one agent-workflow entry point. It composes the three
existing capabilities through a temporary setup facilitator, unresolved-choice
walkthrough, automatic role briefing and acknowledged handoff. Component skills
remain independently usable. No new runtime service or model agents are added by
this package update.

Validation covers all four skill definitions and bundled references, plus the
existing helper suite. Static walkthrough review covers a new project, adaptation
of existing records, partially completed setup and an exhausted/missing grant:
each keeps setup ownership with the facilitator instead of requiring a user-written
EL prompt. This is instruction review, not a model-executed acceptance test.

The guided entry point has not yet completed a live end-to-end walkthrough.
The held pilot is not restarted by installing these instructions.

## Focused startup correction — 2026-10-08

A private pilot reported passive leadership/area openings and excessive routine
activation overhead. The inspected launch briefs explicitly requested acknowledgment
and waiting despite established planning objectives. The shared instructions now
cover both brief generation and recipient behavior: a useful first planning question,
reuse of existing context, explicit-pause exceptions and one routine registry update.

Validation is package/skill validation plus static scenario review: known planning
mission, explicit pause/acknowledgment diagnostic, routine area activation, missing
ownership during recovery and bounded implementation authority. This is not a fresh
model-executed behavioral test. Helpers and runtime configuration are unchanged;
no agents or project setup are restarted for validation. Confirm the improvement
on the next authorized real activation.

## Package and helper checks

- python3 -m unittest discover -s tests -v: 18 tests covering allowance
  reservation/reallocation, recursive usage, replay/replacement, unknown usage,
  invalid counters, session extraction/naming guards, worktree isolation, mapping
  validation, GitHub pagination, creation retries and stable editable reports.
- python3 scripts/validate.py: all three skill packages, references and syntax.
- Codex skill-creator quick_validate.py: all three skills valid. The validator's
  existing PyYAML environment was used; the package itself needs no PyYAML.
- GitHub live check in the separate private practice repository: task creation
  retry reused one issue; a report update preserved its ID and direct link.
- Usage reader checked against an authorized earlier session's cumulative native
  counters. No transcript content is returned by the reader.

The helper suite ran with Python 3.9.6 on macOS. It uses temporary synthetic Git
repositories. Local allowance locking currently supports macOS/Linux; network
filesystem/distributed writers are not supported.

No new model sessions were launched for these package checks. Session renaming
is covered by a fake native client here and earlier runtime evidence below;
the current packaged adapter still needs live pilot validation.

## Runtime evidence inherited from design experiments

On a macOS host with Codex CLI 0.158.0 and daemon 0.159.0, synthetic tests on
2026-09-29 demonstrated nested/peer messages, waking a completed native child via
followup_task, messages between active independent sessions via codex queue,
session naming/readback and observable token-category counters.

The tested native child viewer disabled direct user input. An idle disconnected
independent session processed queued work after its viewer was resumed; unattended
wake was not established. Active-work survival through detach was not established.
Account quota was observable, but per-thread account credit usage was unavailable.
These observations are version/host specific.

## Subsequent pilot observations

Independent leadership/area sessions and a PL/EL split were established. Native
thread messaging resumed an idle session after its CLI viewer released writer
ownership. Another interface initially encountered an active-writer conflict;
queue acceptance had not established that direct attachment would work.

Resource control failed during planning: default session-list filtering omitted
registered native-created sessions, and soft limits were exceeded before all
roles checkpointed. Collection by exact participant IDs exposed the missing
usage. Guided setup now requires the explicit registry and includes setup,
observation and closeout in resource planning. These instructions do not amount
to a tested automatic budget enforcement fix. Human direct input, active detach,
working AC/TC splitting, review/integration and recovery still need live validation.

## Required checks before describing the pilot as complete

- Visible roles and workers accept independent human interaction.
- Requests reach and wake the intended role, including when idle.
- Active work survives detaching the interface on the chosen host.
- A role split preserves the lower role's execution and routes future decisions.
- Real session usage, including helpers, is attributed without double-counting.
- Reports and reviewed code reach their configured canonical destinations.
- Fresh roles recover from records; helper visibility matches user expectations.

## Sources

- https://learn.chatgpt.com/docs/agent-configuration/agents-md
- https://learn.chatgpt.com/docs/build-skills
- https://learn.chatgpt.com/docs/app-server
- https://learn.chatgpt.com/docs/pricing#token-rates
- https://docs.github.com/en/rest/issues/comments
- https://git-scm.com/docs/git-worktree
