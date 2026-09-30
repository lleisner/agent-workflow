# Validation status

The v0.1.0 pilot package passed local/helper checks on 2026-09-30. The live
model-based pilot is prepared but awaits its bounded resource grant. Unit tests
establish helper behavior, not the quality of model judgment or reliability of
an unattended hierarchy.

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
