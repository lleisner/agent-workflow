# Operating model

## Responsibilities and project boundaries

The hierarchy is reusable across repository layouts. Workspace setup maps goals,
decisions, records, permissions and resources to the project's existing locations.
AGENTS.md is an entry point, not a live task log. Logical responsibility, session
identity, branch ownership and permission to act are separate.

User Liaison (UL) aligns the user's conception with the agents' conception of the
project. It clarifies intent and underspecification, answers project questions,
develops/conveys decisions, follows important requests through and guides human
attention. It directs sustained area/task discussion to the responsible agent once
ownership is clear, before developing that area's detailed scope itself. At every
rank, use the lowest role whose responsibility covers the whole decision; quick
answers need no handoff and broader choices remain with their owner. A concise
handoff preserves context so the user does not repeat it. Meaningful decisions are
checkpointed and relayed at a natural boundary or on request; tentative ideas remain
distinguishable. Direct discussion decisions need no second approval through UL.
Focused direct contact with any rank is possible without hidden changes to others'
commitments. UL remains outside autonomous execution and does not coordinate ELs.

One logical executive Project Lead (PL) owns project-wide execution and acceptance.
EL coordinates ongoing work across its assigned areas; AC coordinates and curates
TC deliverables within an area; TC owns one integrated deliverable and its workers.
Specialists are bounded helpers available at any rank, not another hierarchy rank.
The [role map](../skills/agent-hierarchy/references/roles.md) links the authoritative
role instructions. Overview prose does not replace those instructions.

Initially one occupant holds executive PL+EL, with UL separate. Separate executive
PL is useful only for an authorized expansion to multiple ELs. EL ownership is by
initiative, with one primary EL per AC. PL coordinates wider priorities/resources;
ELs can make ordinary peer handoffs directly. Counts of areas are not automatic
staffing thresholds. Multi-EL runtime operation remains deferred for the pilot.

An initiative may span areas. A numbered ready-pool task belongs to one area and
one TC; worker assignments belong beneath it. User gates configure which decisions
require approval, without transferring decision ownership out of the hierarchy.
Internal subtree reorganization needs no inherent parent approval when outcomes,
commitments, authority, resources and review obligations remain intact. Material
coordination changes are communicated; wider boundary changes involve their owners.
The current pilot retains user gates on new/split areas and added executive capacity.

## Reusable instructions and assembly

Role-specific sources and the shared supervision contract are authored once in
the hierarchy skill. A small assembler produces complete native TOML profiles.
Combined profiles contain both full role responsibilities and transfer rules;
there is no dependency on native multiple-profile inheritance or hot swapping.
UL, workers and review helpers receive focused instructions, not the entire
supervisor contract. Skills retain startup, coordination and lifecycle procedures;
project records retain live assignments and actual authority. Generated assets are
not installed automatically. See [assembly](../skills/agent-hierarchy/references/profiles.md).

The shared relationship is clarify, delegate, coordinate, curate and integrate.
Supervisors remain responsible while execution is underway: address dependencies,
drift, contention and avoidable waiting, not just initial assignments and final
merges. Each role critically evaluates requests against its broader scope and
respects evidence held below. It advances known authorized work, requests a real
missing decision or states a genuine waiting condition. No continuous polling or
manufactured work is required. UL's useful work includes deliberate availability.

## Guided entry and continuity

One agent-workflow invocation owns discovery, unresolved choices, workspace
preparation and focused handoffs. The invoking session normally acts as temporary
setup facilitator; users do not compose prompts or invoke a sequence of skills.
Role startup supplies an immediate objective and useful first action/question,
not an acknowledgment-only waiting phase unless requested. Scope already settled
should lead to authorized work or the specific missing grant. Normal activation
reuses scoped records and makes one registry update, not a whole-project reread.

Reentry reconciles existing occupants, work, grants and records. No duplicated
roles, renewed limits or migration to a template is implied. New occupants start
with focused context. Verify actual profile loading, settings, communication and
human access before claiming them; successful queueing alone is not receipt.

AC+TC can share an occupant when one TC deliverable covers the area's current work.
On an authorized split, the existing occupant keeps the lower role, workspace and
running team; a new occupant takes the upper role. Preparation can happen while the
incumbent works. The new upper ownership becomes effective after the incumbent
confirms relinquishment. This one-time transfer confirmation is distinct from
routine reports. A retained combined profile may keep inactive upper instructions;
active assignments determine responsibility. Do not replace both agents just to
obtain pure profiles or assume native reparenting. A later replacement uses the
appropriate profile. For PL+EL, separation accompanies approved multiple-EL need.

## Review, correction and integration

Workers verify contributions and obtain built-in Codex code review through the
agreed route. TC arranges independent integrated-result assessment, normally with
the focused Integration Reviewer. AC, EL and PL assess combinations at their own
scope, reusing valid lower coverage. Reopen affected coverage for changed behavior,
requirements, assumptions, gaps or contrary evidence; a larger diff alone does not
justify repeating every review. Critics are optional for an identified need.

Reviewers remain independent and review-only. Named original repair owners handle
ordinary corrections directly with the reviewer, without a coordinator relaying
each message or a fresh whole-diff review after every fix. Findings must be judged
against intended behavior and recorded trade-offs; scope/disagreement issues go to
the responsible coordinator. Necessary repairs are completion work. Optional
improvements go to the supervisor able to judge value and wider consequences.
Continue while refinement makes meaningful progress; persistent failure requires
reassessment rather than unlimited retries or weakened acceptance.

TC curates results before AC sees them; AC evaluates useful coherent area increments
and returns deficiencies before human review. Several TC outputs can form an area
increment while unrelated work continues. The pilot's intended integration preset
allows AC to accept TC results and retains human approval for area-to-dev and
dev-to-main integration. It is applied only through explicit project adoption;
existing live grants and starter examples do not change themselves.

Each independent writer normally has an isolated worktree. TC integrates its task,
AC its area where useful, and EL the designated project destination. Shared dev
writes, including coordination docs, require exclusive turns. Prepare candidates
and approvals before taking the turn; check current dev, validate the combined
result and hand back a recorded clean state. Reconcile interrupted work before
reuse. PL adds project-wide acceptance responsibility without another mandatory
branch, merge or full technical review. A worktree lock is not a write mutex.

## Human decisions and evidence

Human-facing proposals are compact and delivered in chat, separate from detailed
agent reports. Start proposals may reuse recent scoping context and show the
schedule, real dependencies, high-impact choices and exact authorization requested.
Integration requests must stand alone: assume the user has not followed execution.
Provide the outcome, demonstrated change, meaningful discoveries, suitable evidence
or a usable interaction, limits/trade-offs and a specific recommendation/decision.
A review-passed assertion does not demonstrate the outcome. Keep detailed evidence
as optional depth and preserve decision-relevant uncertainty despite brevity.
Use language that is self-explanatory or established in discussion with the user.
Translate internal task, fixture and failure codes into their meaning and consequence;
introduce unfamiliar terms only when useful and explain them. Identifiers belong
in supporting references unless needed for navigation. Each role owns the clarity
of its user-facing communication; UL does not rewrite all reports.

Anticipate this evidence during scoping: claims, useful comparisons/interaction and
baselines or material to preserve. Record a few lines in the existing scope and
assign evidence collection with the work. This adds neither a document nor a gate.
The requesting execution owner prepares the package; UL curates the user's attention
and obtains missing context without becoming another technical reviewer.

## Records, reporting and closeout

Use one canonical published home for durable direction/decisions and the selected
tracker for live work. In the GitHub starter, a TC deliverable is one issue with
editable assignment comments; separate coordination issues hold subordinate reports
and stay out of the ready pool. Each role owns scoped records, not copies of every
child report. Read concise current summaries and relevant evidence progressively.

Routine changes update records; material changes to others' planning assumptions
also receive concise notification without acknowledgment waits. Actual decisions,
blockers and handoffs use direct contact. Synthesize implications at each level.
Respect the normal escalation route: unresolved user-level choices reach UL via
executive PL, while UL-initiated focused inquiries can receive direct replies.

Readiness, accepted completion and retirement remain distinct. The immediate
supervisor arranges follow-up, deliberate retention or authorized retirement.
Final chat output explains why work stopped, who owns the next step and what resumes
it. Close accepted/integrated, canceled, duplicate or superseded issues with their
disposition; inactivity alone does not justify closure. Preserve searchable history
and material decisions while removing stale entries from current summaries.
Session archive/delete and worktree cleanup remain separate scoped permissions.

## Resources and pilot limits

Model selection stays with the project. Bundled profiles request Standard, with
medium worker/reviewer, high TC/AC and xhigh EL/PL+EL reasoning. UL preserves its
established setting with xhigh fallback; standalone PL settings are deferred.
Native overrides must be checked at adoption, not assumed from prompt text.
Conversational acceleration remains conditional on verified host control/accounting.

Numerical allowances are optional; explicit limits/holds always apply. When enabled,
count own and descendant/helper consumption once, allocate from actual remaining
funds and request reassessment before exhaustion. Replacement, splitting and quota
reset do not restore task allowance. Estimated credits are not exact subscription
percentages. No mandatory project-lifetime or setup budget is introduced.

Use useful authorized real work to test the fixed hierarchy. Record concise lessons
about coordination received/provided and act on recurring evidence. Static package
checks do not establish model judgment, unattended wake or direct human access.
General recursive topology, council support, automatic subscription optimization,
new orchestration infrastructure and a settings UI remain later work. The pilot
should reveal when additional coordination earns its cost.
