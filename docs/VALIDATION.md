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

## Scoping-to-work correction — 2026-10-08

A pilot AC reported stopping after area scoping without carrying its existing
coordination duties into a TC proposal or launch decision. The hierarchy guidance
now links those duties to a short transition in lifecycle.md. No new gate, budget
policy, record type or task-count rule is introduced.

Package/skill validation and static scenario review cover unconfirmed scope,
already-confirmed scope, planning-only authority, an existing dispatch grant and
cross-area dependencies. The review checks that confirmation is reused, proposals
show acceptance/dependencies/parallelism/ownership, EL receives broader questions,
and only missing authorization blocks launch. This is instruction review, not a
new model-executed acceptance test. Confirm behavior in the next authorized use;
helpers and project execution remain outside this maintenance change.

## Continuation, speed and closeout correction — 2026-10-08

Pilot feedback generalized passive scoping into a problem across ranks: reporting
known next steps without acting, delegating or requesting the missing decision.
The entry point now requires that transition while preserving actual waiting,
completion, discussion-only scope, authority and allowance boundaries. Speed
policy defaults background work to Standard, with explicit priority exceptions.
Closeout guidance separates reversible session archiving, permanent deletion and
safe worktree removal under the project's actual cleanup grant.

Package/skill validation and static scenario review cover authorized dispatch,
missing approval, planning-only work, completed review needing integration,
waiting children, exhausted allowance, completed scope, Fast inheritance unknown,
mixed-tier accounting and a stale-looking parent with live descendants. This is
instruction review, not a fresh model-executed test of autonomous continuation.

A bounded runtime probe on Codex CLI 0.160.0 created two ephemeral threads without
starting model turns. `thread/start` returned `default` for Standard and `priority`
for requested `fast`; `thread/settings/update` and its notification confirmed a
change back to `default`. The probe changed no existing session or global setting.
It verifies per-thread configuration, not inference speed/cost, reattachment
persistence or tier inheritance through native agent-launch wrappers. Those
wrappers currently expose no per-call service-tier argument.

Official app-server documentation, the locally generated schema and CLI help
expose archive/unarchive and permanent deletion, including descendant effects. No real
sessions, branches or worktrees were retired to validate those capabilities.
Runtime cleanup behavior remains untested by this package.

A follow-up instruction review covers partial dependency waits with independent
work available, legitimate waiting with nothing ready, repeated coordinator
congestion, delivery failure mistaken for congestion, and useful/no-new-lesson
closeouts. Waiting observations and brief pilot lessons reuse existing records;
there is no new monitoring loop, mandatory retrospective or automatic role split.
These scenarios were reviewed statically, not run as model-agent trials.

## Human collaboration and reasoning defaults — 2026-10-09

The guidance now distinguishes active human collaboration from independent work:
prioritize consequential scoping decisions, announce when input is sufficient,
reuse existing grants and route routine choices through the hierarchy. Planning
launch instructions no longer require an invented question when scope is settled.
A configurable reasoning profile starts workers/specialists at medium, TC at high,
and AC/EL at xhigh, preserving PL's agreed setting and allowing justified exceptions.
Fast defaults off; conversational acceleration requires working host transitions
and attribution of mixed-tier usage. The existing whole-session ledger is unchanged,
so automatic switching for its registered sessions is not claimed as implemented.

Validation covers package/skill checks and static scenarios: underspecified intent,
already-settled scope with/without execution authority, a low-impact operational
choice during human conversation, deferred nonurgent questions versus a blocker,
renewed user input, a difficult specialist assignment, and unsupported speed or
effort controls. Local CLI 0.160.0 schema inspection confirms an effort setting for
subsequent turns; this update adds no live reasoning test, agent launch, model
benchmark or automatic conversation detector. Existing sessions/configuration are
not changed by publishing the instructions.

## Human approval schedules and visible closeout — 2026-10-09

The user accepted a compact chat table plus dependency map for complex approvals.
The new hierarchy reference scales across EL/AC/TC work, separates the human view
from detailed agent records, and shows parallel starts, intermediate handoffs,
aggregate resources and the actual grant. The task skill includes the compact
standalone form. Final chat messages now explain every valid stopping state;
accepted completion routes reassignment/retention/retirement to the immediate
supervisor instead of leaving unowned idle sessions.

Package/skill validation and static walkthroughs cover a small task, a whole-area
five-TC plan, early versus final handoffs, a genuine dependency cycle, partial
waiting, unknown resource estimates, existing/changed grants, user/supervisor waits,
review pending, completed assignment closeout and retained leadership. These are
instruction checks, not new model-executed trials. No sessions were launched or
retired, no project scope was granted, and no runtime wake behavior was changed.

## Conversation-first project lead — 2026-10-09

Accepted pilot feedback broadens PL from vision alone to human/project alignment:
maintain intent, answer questions, develop/convey decisions, follow through and
direct human attention. PL prioritizes discussion, checkpoints meaningful decisions
and relays them at a natural boundary or on explicit request. Direct contact at any
rank preserves affected coordinators' visibility and actual grants. EL retains
execution ownership; explicit human decisions and consequential tradeoffs cannot be
silently overridden. Startup/split guidance and the all-rank continuation rule now
reflect that distinction.

Package/skill validation and static walkthroughs cover tentative versus settled
ideas, continued discussion, normal/interim delivery, time-sensitive running work,
queued versus adopted instructions, direct TC contact with resource consequences,
standing priorities, new facts with small adjustments versus protected choices,
attention triage, combined PL+EL duties and a split retaining live EL work. This is
instruction review, not a model-executed behavior or availability guarantee. No
role was launched, split or reconfigured and no runtime settings/helpers changed.

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
