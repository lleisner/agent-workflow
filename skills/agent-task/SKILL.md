---
name: agent-task
description: Define, claim, report, review or integrate a bounded project deliverable using the project's issue tracker and branch/worktree agreement. Use for a task lifecycle or editable assignment reports, with or without an agent hierarchy.
---

# Agent task

Read the project agreement and relevant current task/area records. In a hierarchy
a TC owns the deliverable; in a solo workflow the current agent or human can own
it. Use the project's conventions rather than requiring the companion skills.

## Define and release

Use assets/task.md as a compact starting point. Identify outcome/non-goals,
acceptance, dependencies, owner/area, integration target, authority and allowance.
An initiative spanning areas is decomposed above TC; it is not one cross-area task.
The responsible coordinator judges readiness and dependency strategy within the
approved scope. Priority alone does not grant permission or budget.

When human approval is required, present a compact schedule directly in chat:
work/owner and intended result, what can start now and what must wait, plus a small
dependency map when useful. Add the recommendation/tradeoff, justified staffing and
aggregate resource/stop limits, material exclusions and exact authority requested.
Keep detailed agent assignments in their own records; record the resulting human
decision there without duplicating the chat document. Ask only for missing grants.

For the GitHub starter, read [GitHub records](references/github.md). One task issue
is the deliverable; worker assignments use editable comments beneath it. Keep
coordination issues out of the ready pool. Use GitHub's issue number with the
project prefix for a stable ID; gaps are fine and no separate ID allocator is
required.

## Take responsibility and execute

Refresh the current issue, check it is unclaimed/assigned to you and authorized
to start, then record the owner/session and phase before launching assignments.
Serialize dispatch within a scope using its responsible coordinator. If another
claim appears, resolve it there; a status label alone is not an atomic lock.

Give concurrent writers isolated assigned worktrees. Declare expected component/
interface overlap and let the responsible coordinator agree a division or sequence
affected work. Keep unrelated authorized work moving.

Each assignment updates its own short report using assets/report.md. Report only
changes relevant to the supervisor. Ask directly when a decision is needed.
Significant human decisions go in their canonical decision record.

## Deliver and integrate

Read [delivery](references/delivery.md). Assemble evidence and the integrated
result, obtain applicable independent review, and critically assess readiness.
Follow the configured gate at each integration boundary. Do not infer merge
permission from responsibility, a ready label or a positive review.

After integration, verify the target commit/PR and checks before updating status.
Keep task integration distinct from stable release. Close using actual acceptance
and the configured task target. Update scoped records and conserve useful evidence.
Do not perform routine destructive cleanup or discard local work as a side effect.
