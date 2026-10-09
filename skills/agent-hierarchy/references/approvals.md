# Human approval schedules

Use this when any role, including TC, needs the human to approve a work plan.
Only ask for genuinely missing authority. Deliver the decision view directly in
chat: short Markdown table and, for more complex dependencies, a small readable
map. Plain text is a valid map when diagrams do not render. Do not require opening
an issue, external document or special renderer to understand the decision.

The human schedule is a distinct document from detailed agent review/assignment
records. Keep methods, full evidence, exact commands and low-level context with
those records. The chat view must itself contain the important decision facts;
links are optional depth, not a substitute for an informed approval. After the
answer, record the granted scope/actions, resource boundaries, conditions and
proposal date/revision/reference in the authoritative record. Do not copy the
whole chat view or conversation there. A missing chat permalink does not excuse
an incomplete durable grant summary.

## Compact structure

1. **Goal/value:** the outcome and why this increment matters, in one sentence.
2. **Schedule:** rows for concrete workstreams/owners, what can begin now, and
   exactly what must wait. For an AC/EL request, show the relevant whole area/
   initiative, not just the stages of one chosen TC. Mark deferred/out-of-request
   branches briefly. For TC, show its worker assignments. Include a short result/
   acceptance phrase when the task name is insufficient.
3. **Dependency map when useful:** show outputs exchanged and integration order.
   Label early milestones separately from completion, even for the same owner.
   Resolve genuine circular dependencies; an arrow to an unspecified "done" state
   must not hide a deadlock. Phases describe dependencies, not invented durations.
4. **Recommendation/resources/boundary:** a few short lines for the high-impact
   choice and tradeoff, staffing rationale, new versus existing participants,
   total peak concurrency, expected usage where estimable and actual limits/stops.
   Explain the basis and uncertainty of non-obvious caps. Attempt/task counts are
   not token or monetary caps; include review/helpers/coordination in the stated
   envelope. If no numeric spending cap is proposed, say so explicitly rather than
   inventing one or implying it exists. Keep material exclusions and residual risk
   visible; omit routine administration.
5. **Exact decision:** name what one approval covers and which later gates remain.
   Reuse existing grants; approving a schedule does not implicitly authorize extra
   streams, resource extensions or production merges outside its stated envelope.

Scale down to one row and a short paragraph for small work. The five-task example
below illustrates dependency notation, not a required team size or staffing choice.
For a change to an approved plan, show the affected schedule and consequential
changes; do not request the entire grant again. Dependent work waits for the answer;
other authorized work can proceed using available asynchronous communication.
Do not imply a chat question by itself schedules future execution or wakes agents.

## Example: overlapping preparation and handoffs

**Goal:** deliver a tested export prototype. Illustrative, not a launch request.

| Work / owner | Can begin now | What must wait |
| --- | --- | --- |
| TC1 · Source mapping | Define document locations | No dependency |
| TC2 · Test cases | Prepare cases and expected results | No dependency |
| TC3 · Integration | Publish an early interface; prepare the skeleton | Final integration needs TC4 and TC5 outputs |
| TC4 · PDF mechanics | Prepare methods and checks | Applying them needs TC1 mapping and TC2 cases |
| TC5 · Allocation | Define consistency rules and examples | Connecting implementation needs TC3's early interface |

~~~text
TC1 · Mapping ──┐
                ├──► TC4 · PDF mechanics ────┐
TC2 · Cases ────┘                            │
                                             ├──► TC3 · Final integration
TC3 · Early interface ─► TC5 · Allocation ───┘
~~~

**Recommendation:** parallel preparation, then release each dependent stage as its
inputs arrive; do not wait for unrelated tasks. Extra concurrency trades resource
use for earlier results. TC3's early and final stages are the same owner.

**People/resources:** supply justified actual staffing, peak activity across all
streams plus the coordinator, and a total allowance/stop policy. This example does
not estimate them; do not turn hypothetical counts into a live approval request.

**Approval boundary:** name which deliverables, writes/runs, review and integration
are included, the stopping outcome and any retained production gate. A negative or
inconclusive study finding can be a valid completed deliverable. Use real proposal
values here before asking the human to decide.
