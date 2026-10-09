# Operating model

## Boundaries

The hierarchy is reusable across repository layouts. Workspace setup maps logical
records to project locations; it does not impose a universal directory tree.
AGENTS.md is a short entry point into the project agreement, not a live task log.
Roles, branch responsibility, workspace allocation and merge authority are
separate concepts.

## Guided entry point

One invocation of agent-workflow owns the onboarding walkthrough, composing the
independent hierarchy, workspace and task capabilities internally. The user answers
consequential project-specific questions; the agent discovers factual settings,
performs setup and generates/delivers the handoffs. Users do not need to know the
skill sequence or write informed prompts to transfer setup responsibility.

The invoking agent normally acts as a temporary setup facilitator. This is a duty,
not a seventh rank or an additional permanent supervisor. Leadership starts with
fresh focused context after the setup. EL owns ongoing operations after handoff
and can delegate later configuration work to a setup specialist.

Setup asks one unresolved question at a time, with a recommendation and tradeoff,
and reuses accepted decisions. It records a concise recovery checkpoint and
resumes existing occupants/workspaces/grants on repeat invocation. Creation of
the agreement alone is not completion: finish the authorized initial role handoff
and orient the user, or explicitly identify the remaining blocker.

A planning launch carries an immediate objective: brief orientation, then the
next consequential unresolved question using known context. When already scoped,
advance the authorized next step or request the actual missing grant. Acknowledgment
is part of that response, not a separate waiting phase unless explicitly requested.
Routine activation reuses records and updates the registry once; unrelated
workflow publication is not a prerequisite. This changes neither implementation
permissions nor the ownership checks needed for recovery.

## Role boundaries

PL owns human/project alignment, EL execution planning, AC area alignment, TC a
task deliverable, W implementation and S focused expertise. PL's five duties are
maintaining alignment, answering project questions, developing/conveying decisions,
following through on human requests, and directing human attention where it is
most valuable. Human collaboration is principally with PL/EL and through AC for
an area, with direct access to visible workers.

PL is conversation-first: clarify needs and gaps, preserve lightweight meaningful
checkpoints, and relay agreed changes at a natural discussion boundary or on
explicit request. Keep tentative ideas separate and mark decisions not yet conveyed.
Flag material consequences of delaying an instruction during the conversation.
Brief asynchronous delivery and follow-through keep PL available; routine dispatch,
integration and continuous monitoring do not belong to it.

PL can retrieve facts or convey agreed human instructions directly to any rank;
affected coordinators/EL receive concise updates on changed commitments. This
changes routing, not grants or execution ownership. EL owns operational priority.
Existing priorities can be applied without reapproval; small adjustments on new
facts may be resolved with PL when clearly aligned and within authority. Existing
explicit human decisions and consequential new tradeoffs return to the human.
PL is not an additional approval gate for routine authorized EL decisions.

Active human collaboration prioritizes consequential intent/scope decisions that
need the human. Once enough is settled, announce the transition to independent
work and proceed under existing authority; ask only for a missing grant. Operational
choices remain with the hierarchy, while nonurgent human questions can accumulate
for the next useful discussion. A visible session is not always conversational.

Human approval requests at any rank use a compact schedule directly in chat,
separate from detailed agent proposals. A table distinguishes immediate work from
blocked stages; a small dependency map exposes intermediate handoffs and integration
order. Coordinators plan parallel progress across their full known responsibility,
with justified deferrals/serial work and aggregate staffing/resources. Store the
resulting grant and conditions in the authoritative record, not a duplicate of the
human document. The example's team size is not a default or execution grant.

Every supervisor assesses whether a subordinate's approach/request makes sense
in its broader context. Agreement is a valid outcome; critical judgment does not
require manufacturing objections or absorbing all subordinate detail.

Every rank advances its actual responsibility. For PL, clarifying human needs
and decisions is that work; conveying changes follows the discussion boundary.
Execution roles carry known work into authorized action/delegation or a concrete
request for the missing decision. A status summary alone does not fulfill an
unfinished responsibility. Genuine waiting, explicit pause, exhausted allowance
and completion are valid stopping conditions; no continuous polling or invented
work is required.

An initiative can span areas. A numbered task belongs to one area and one TC.
Worker assignments belong beneath that task. Cross-area decisions belong above
TC. Operational sequencing, interfaces, parallelism and investigations remain
coordinator judgments within the grant.

## Records and context

Record each fact once in its authoritative home. Use GitHub issues for live tasks
and reports in the starter workflow: one task issue, one editable comment per
assignment, and separate AC/EL coordination issues for reports from their direct
subordinates. Coordination issues never enter the ready pool.

Published strategy, briefs and durable decisions use a canonical branch, such as
dev. Code and provisional implementation notes use area/task worktrees. Each
role owns its scoped records. EL maintains an overview with links rather than
transcribing every update. Publishing does not imply escalating.

Routine supervisor-relevant reports update records without requiring a reply.
Request a decision or help directly when needed. Superiors read current relevant
summaries when coordinating. Reports contain implications at the receiver's scope;
they do not concatenate child reports. Evidence is linked for inspection, not
automatically loaded. Normally ask the responsible subordinate for clarification.
Inspect directly for a compact fact or when the chain is failing.

Capture meaningful human agreements and rationale when settled. New role
occupants use fresh focused context and authoritative records, with additional
material loaded as needed. Full conversation inheritance is exceptional.

## Lifecycle

Combine roles when useful. The user initiates PL/EL separation; EL can initiate
AC/TC separation within authority and allowance. The current agent keeps the
lower execution role, workspace and running workers; a new agent takes the
supervisory role. Record the change, notify affected roles and track acknowledgment.
Native spawn ancestry need not equal logical supervision.

Visible hierarchy agents are human-accessible points of contact. Temporary review
or promotion helpers may be sub-agents without direct human access. Keep them out
of the routine overview where supported, while preserving results/accountability.
Specialist status alone does not determine visibility.

Use names such as W1 · PCT007 Edge-case tests · EL1/AC1/TC1. Roles persist across
agent replacement. Workspace folders use stable area/task names, not occupants.

Every role's final chat message explains its valid stopping state, decision owner,
user action needed and resumption condition. Accepted assignment completion triggers
an immediate-supervisor decision on follow-up, deliberate retention or retirement;
it does not justify an ownerless idle session. Standing leadership duties can
justify retention. Results awaiting review remain distinct from accepted completion.

## Authority and resources

The user configures start and integration gates. The starter grants more autonomy
to begin bounded work than to integrate results: for example approve an area
scope/allowance once, while retaining approval of each task integration.
Both gates can subsequently change independently. Missing merge authority means
human approval. One agent filling two roles is not an independent reviewer.

Each independently writing/integrating agent normally has an isolated worktree.
TC integrates its task, AC may integrate its area, EL manages project integration.
PL is not a mandatory final technical integration stage. EL or a delegated
integrator performs promotion under the chosen gates. Read-only helpers need not
receive worktrees.

Setup and ordinary human/leadership conversations have no mandatory numeric cap.
There is no default project-lifetime budget. Optional time-window project
allocations remain distinct from cumulative task spending. Explicit user limits
apply only to their stated scope.

Task allowances are fixed and cumulative. Model/category-weighted estimated
credits are not exact charges or subscription shares. Count own and descendant
usage once; never add cached input or reasoning output again. Allocate from
existing allowance. Release unspent allowance before reallocating it. Session
replacement and subscription reset do not restore task spending.

At roughly 80% consumption, or sooner when remaining work exceeds allowance,
request reassessment. Supervisors assess the approach and value of further work,
not just available funds. At exhaustion without an approved extension, checkpoint
and pause affected work. Dynamic quota management is opt-in and not implemented
by the initial fixed-accounting helper.

## Pilot and later work

Pilot the workflow in useful authorized work; a separate synthetic project is
optional. Keep validation inputs non-sensitive and use the authorized billing
mode. Record recurring friction in existing coordination records, distinguish
project conventions from reusable mechanics and propose focused corrections.
Validate communication,
direct input, unattended wake, detach survival, role splitting and full usage
attribution before asserting them. A strategy encoded in a skill is not proof
that a runtime supports it. Automatic adoption of a departed coordinator's live
workers is not a pilot requirement.

Later: specialist skill libraries, optional subscription advisor, skill
self-improvement, wider host support and a template repository extracted from a
working practice setup. Improve from observed needs rather than adding ranks or
infrastructure speculatively.
