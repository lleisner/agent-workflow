# Startup, planning, splitting and recovery

## Start or resume

For a newly onboarded project, accept the focused brief delivered by its temporary
setup facilitator. Confirm ownership briefly as part of the first useful response.
For an established planning objective, orient to the known mission and ask the
highest-impact unresolved question that needs human input. Use known context;
do not make the user repeat it or prompt again to begin. If the scope is already
sufficient, state the transition to authorized work or request the actual missing
grant; do not invent an opening question. Follow the human/independent-work
boundary in [communication](communication.md). Respect an explicit pause or
acknowledgment-only diagnostic. Planning alone does not grant autonomous
investigation, implementation, inference or worker dispatch. No particular
interview skill or long questionnaire is required.

Return unresolved setup defects to the facilitator; do not require the human to
relay a transcript or reconstruct setup. Ongoing execution belongs to EL after
handoff, while substantial later setup changes can use a focused helper.

For routine activation in an established project, reuse current records, supply
a focused brief with its immediate objective, launch/name/verify the contact and
make one concise registry update. Read only the relevant role/scope and genuinely
missing or changed information. Keep unrelated workflow publication and repeated
whole-project reads off this path; resolve actual ownership/authority gaps when
needed. This does not replace the reconciliation required for recovery.

1. Find the project agreement and the authoritative scope record.
2. Establish role identity separately from the native session ID and task ID.
   Record scope, supervisor/children references, active occupant, authority,
   applicable resource policy or remaining work allowance and workspace/report locations in the existing record.
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

## From area scoping to coordinated work

An AC's planning responsibility continues beyond identifying the scope:

1. State your assessment of readiness and summarize outcomes, exclusions,
   constraints and remaining uncertainties. Confirm scope when needed; reuse
   existing explicit user confirmation instead of asking again.
2. Plan across the area's known responsibility before selecting the next task.
   Show bounded deliverables/acceptance, priorities, ready parallel streams,
   genuinely dependent work and deliberate deferrals with reasons. Name the
   artifact/milestone each dependency needs; distinguish what can start now from
   what must wait to finish. Include shared interfaces/file ownership, integration
   order and cross-area needs. Justify serial exploration by the uncertainty it
   resolves and the parallel work it unlocks; do not impose blanket wave barriers
   or spawn extra agents merely to appear parallel. Turn unresolved technical
   questions into bounded deliverables or actual gates, not silent assumptions.
   EL applies this across areas; TC applies it within its deliverable.
3. Surface proposed priorities/dependencies to EL for broader review through the
   existing reporting mechanism; request a decision directly when needed. Keep
   the summary at EL's scope and link the proposal. EL addresses wider conflicts,
   not a repetition of user choices already confirmed with AC. Cross-area work is
   coordinated above TC; do not give one TC authority over several areas.
4. State the proposed launch scope and applicable resource/authority needs. Scope
   confirmation and planning alone are not dispatch authorization. Apply the
   project's actual gates and existing grants: if already covered, proceed; if
   not, request only the missing decision from the designated approver. For the
   human, use the [chat approval schedule](approvals.md); a long agent-facing
   proposal is not the human review surface. Add no universal EL approval
   gate or fixed TC count. Do not reset spending or request a new allowance or
   permission when the existing grant already covers the proposed work.
5. Once authorized, dispatch and coordinate within the agreed plan, keep EL
   informed and escalate material changes. Close the planning phase with the
   next decision or authorized action, rather than stopping at "scope is clear."

Use the existing area/task records; no extra planning registry is needed.

## Split a combined role

The user initiates PL/EL splitting. EL can initiate AC/TC splitting within its
grant. Repeated unavailability, competing context and delayed coordination are
signals, not fixed thresholds.

- The existing agent retains the lower execution role, its workspace and workers.
- Create the upper role with a fresh brief from existing published records.
  For PL/EL separation, the existing occupant keeps execution and running work;
  the new PL receives goals/preferences, settled priorities, a concise project
  overview, pending human decisions/requests and contact routes. Give it the
  [PL alignment duties](roles.md#pl--project-lead) and conversation-first workflow,
  not a second execution-management assignment or an extra mandatory approval gate.
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

Result readiness, accepted assignment completion and agent retirement are distinct.
Request the relevant review/integration when results are ready. After acceptance,
the immediate supervisor owns the closeout decision: authorized follow-up work,
deliberate retention for a stated responsibility/trigger, or retirement under the
cleanup policy. Preserve the result/usage and route that decision request; do not
leave a finished occupant without an owner for its next disposition. The supervisor
handles this at its next relevant coordination checkpoint, not by forwarding every
closeout to EL/the human. Ongoing leadership/contact duties can justify retention
without inventing new assignments or repeatedly seeking permission after each chat.

Prefer replacement at a meaningful boundary, normally after live subordinate work
has finished. Preserve references to current commits/PRs, unresolved questions,
applicable resource policy or remaining work allowance and next action. Canonical records are the handoff; add only
missing facts. Retire old routing deliberately so two occupants do not both act
as owner.

Do not require automatic adoption of live workers in the pilot. If a coordinator
is lost mid-task, involve the human in recovery. Account for all earlier sessions;
replacement does not renew spending. Preserve uncommitted artifacts separately:
documentation alone does not transport a worktree to another host.

When cleanup is authorized, make it part of closeout instead of leaving stale
roles for the human to discover. Confirm accepted/integrated results, preserved
reports/evidence and final usage, no pending review/request/recovery duty, and no
active work in the affected native descendants. Mark the occupant retired in the
existing registry and preserve its session ID. Prefer reversible session archiving;
permanent deletion needs the project's explicit retention/deletion authority.
Use existing cleanup grants; request only a missing decision with a concrete list.

Worktrees and sessions are separate resources. Remove only owned, unused worktrees
after checking tracked, untracked and ignored artifacts and confirming relevant
changes are retained at the agreed integration target. Use normal Git worktree
removal, not force removal; preserve unique evidence or unresolved work. Local or
remote branch deletion is a separate scoped choice. Do not remove a shared area/
project worktree just because one occupant's duty ended. Record cleanup outcomes
concisely in the existing closeout report, including anything deliberately retained.
