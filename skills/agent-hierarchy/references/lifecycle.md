# Startup, splitting and recovery

## Start or resume

1. Find the project agreement and the authoritative scope record.
2. Establish role identity separately from the native session ID and task ID.
   Record scope, supervisor/children references, active occupant, authority,
   remaining allowance and workspace/report locations in the existing record.
3. Read the relevant brief, settled decisions, current summary and next action.
   Load evidence progressively. Ask a focused question for missing context.
4. Reconcile actual worktree, GitHub and budget state before resuming. A disconnected
   occupant may still be working. Do not silently adopt its active work.
5. Name the session and verify the communication route. A queued message is not
   evidence that an idle recipient has processed it.

Example names:

- EL1
- AC1 · Export · EL1
- TC1 · PCT007 Export validation · EL1/AC1
- W1 · PCT007 Edge-case tests · EL1/AC1/TC1
- AC1+TC1 · PCT007 Export validation · EL1

Use the project's stable prefix and short description. Add the project name only
when the interface does not already group sessions by project.

## Split a combined role

The user initiates PL/EL splitting. EL can initiate AC/TC splitting within its
grant. Repeated unavailability, competing context and delayed coordination are
signals, not fixed thresholds.

- The existing agent retains the lower execution role, its workspace and workers.
- Create the upper role with a fresh brief from existing published records.
- Record the intended new ownership and the transition state. Notify the existing
  occupant and relevant peers; track acknowledgment in the scope record.
- Let the new supervisor orient and collaborate immediately. Resolve overlapping
  decision authority explicitly while acknowledgment is pending. Do not claim the
  lower agent has changed behavior before it has received the change.
- Keep existing assignments and grants valid unless explicitly revised. Do not
  move branches or reparent native sessions merely to match the logical tree.
- Close the transition record once affected roles acknowledge the arrangement.

The coordinator chooses practical timing within these responsibilities; this
procedure does not require a new lock service or a project-wide pause.

## End or replace

Prefer replacement at a meaningful boundary, normally after live subordinate work
has finished. Preserve references to current commits/PRs, unresolved questions,
remaining allowance and next action. Canonical records are the handoff; add only
missing facts. Retire old routing deliberately so two occupants do not both act
as owner.

Do not require automatic adoption of live workers in the pilot. If a coordinator
is lost mid-task, involve the human in recovery. Account for all earlier sessions;
replacement does not renew spending. Preserve uncommitted artifacts separately:
documentation alone does not transport a worktree to another host.
