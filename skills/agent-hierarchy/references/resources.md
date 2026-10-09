# Bounded-work allowances

A project and its persistent leadership do not need lifetime token budgets. Setup
and ordinary conversations have no mandatory numeric cap; respect any explicit
user limit. Put allowances on autonomous tasks, initiatives or investigations,
including their coordination and helpers. An unrelated experiment's spending or
hold does not govern a new project.

A weekly project allocation is optional and separate from a task's cumulative
allowance. Renewing a time window must not refill a task or erase prior usage.
Record the window and metric explicitly; estimated credits are not an exact
subscription percentage. Dynamic allocation remains optional.

Without a numeric cap, record relevant usage without inventing a fake/infinite
ledger limit. The fixed-limit helper below is only for bounded grants. Use one
ledger rooted at the task/initiative when there is no parent project grant.
Do not charge an entire ongoing leadership conversation to each new task: use
focused sessions for bounded investigations, or attributable deltas with an
accounting method that supports them. This helper imports whole-session totals.


Use the project's existing accounting mechanism when available. The optional
scripts/allowance.py helper provides local persistent accounting without a model
call. Its JSON ledger is private host state, not a second task tracker. Record
grants and significant decisions in the project's canonical scope records and
reference the ledger for observations.

The ledger measures estimated credits using supplied model rates per million
tokens. Configure uncached input, cached input and output rates and a documented
source/date. Rates are estimates, not actual charges or an exact subscription
percentage. The helper never invents a subscription token limit.

Input totals INCLUDE cached input. Output totals INCLUDE reasoning output.
Bill each category once:

    (input - cached_input) * input_rate
    + cached_input * cached_rate
    + output * output_rate

Apply the configured speed multiplier once. Fix model and speed per registered
session in v1; use a new session for a different model/tier so cumulative snapshots
do not misprice mixed usage. This limitation is explicit, not exact attribution
of an unobserved model change.

## Reasoning policy

Preserve the user's selected model and project-specific effort settings. When
adopting a rank-based profile, this is a starting point to evaluate in the pilot:

| Responsibility | Default reasoning effort |
| --- | --- |
| Worker or specialist | medium |
| Task coordinator | high |
| Area coordinator or execution lead | xhigh (extra high) |

PL retains its user-agreed strategic setting; xhigh is a reasonable initial choice
when none is established. Combined roles use the setting appropriate to the work
they are undertaking. These are configurable defaults, not quality guarantees:
a coordinator can assign higher effort to difficult investigation, security review
or integration reasoning within its authority/allowance. Specialist status alone
does not make an assignment easy. Record consequential exceptions in the assignment.
Verify that the selected model/runtime supports the requested effort; do not
silently substitute a different model or pretend a prompt applied a host setting.

## Speed policy

Fast is off by default for every role. When the project's policy enables
conversational acceleration, use Fast for active human collaboration where the
host controls and accounting support it, then restore and verify Standard before
independent work resumes. An open viewer, human availability or user-facing title
is not evidence of an active conversation. EL may explicitly prioritize autonomous
work for Fast within its authority and allowance. Keep reasoning effort separate:
Standard speed does not lower the chosen reasoning level.

Automatic conversation-based switching is conditional, not a capability supplied
by skill prose. If the host cannot reliably apply the transition, or usage cannot
be attributed correctly, keep Standard and state the limitation once. Do not
silently leave background work on Fast or create repeated user approval prompts.

Specify and verify the intended tier through supported host controls; a prompt
requesting Standard is not a runtime setting. Do not assume children inherit the
intended tier or change the account-wide default to configure one child. If the
launch tool lacks the control, use a supported route or surface that limitation
before launching costly work. See [Codex operations](codex.md).

Fast can consume subscription capacity/credits at a higher rate without generating
more tokens. Check the current provider rates for the user's billing mode and
account for the tier once. Switching tiers is technically possible on some hosts,
but this package's whole-session ledger cannot attribute mixed-tier usage: keep
registered work sessions at their recorded tier, or use a separate focused session
or an accounting method that supports attributable segments. Do not silently
reprice the entire history or replace leadership on every human interaction.

## Commands

The ledger helper uses local file locking on macOS/Linux, not a shared network
filesystem. A rate file has this shape (numbers below are deliberately synthetic):

~~~json
{"source":"synthetic test units, not prices","date":"2026-09-30",
 "models":{"example-model":{"input":1,"cached_input":0.1,"output":4}}}
~~~

~~~sh
python3 scripts/allowance.py init --ledger /private/path/allowance.json \
  --scope PCT021 --limit 100 --rates /private/path/rates.json
python3 scripts/allowance.py allocate --ledger /private/path/allowance.json \
  --parent PCT021 --scope W1 --limit 80 --decision "link to grant"
python3 scripts/allowance.py observe --ledger /private/path/allowance.json \
  --scope W1 --session THREAD_ID --model MODEL --input 1000 \
  --cached-input 500 --output 100 --reasoning-output 25
python3 scripts/allowance.py report --ledger /private/path/allowance.json
~~~

Register each session with the register command before starting work (same
scope/session/model/speed arguments as observe, without token counters).
Observe also registers on first import. Register each session in its spending scope.
A helper can spend directly in its
delegator's scope or receive a child scope allocated from it. Never observe the
same session separately in both parent and child. Descendant spending rolls up.

Allocation reserves part of a parent's allowance. Unallocated capacity is available
for the parent's own work. The helper rejects over-allocation and limit reductions
below already spent/reserved resources. It always records actual observed overrun,
even when an agent has exceeded a limit. It does not stop native sessions.

Use set-limit with the decision reference for an authorized adjustment. Release
unspent child allowance before assigning it elsewhere. Parent budget increases
require the appropriate grant, not merely the ability to run this script.

Snapshots are cumulative and idempotent. Counter decreases or changes of scope,
model or speed for an existing session are rejected. Replaced/closed helpers
remain in the ledger. The report distinguishes spending, reservations and
unallocated capacity. Refresh observations at meaningful checkpoints before
resource decisions. Missing observations remain an explicit unknown.

At 80% or a forecast shortfall, request critical reassessment. At exhaustion
checkpoint and pause the affected work until an extension exists. Keep this a
skill behavior; no hard runtime enforcement is claimed.

For native JSONL counters, scripts/session.py usage --file PATH prints the latest
recognized cumulative counter record. Only pass logs of authorized workflow
sessions. Associate its thread ID/model with the correct scope before importing.
The counter adapter fails if no recognized cumulative record exists.
