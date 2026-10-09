---
name: agent-workflow
description: Guide the user through setting up or resuming an agent team in a project, from workspace discovery and unresolved choices through role startup and automatic handoff. Use for a complete hierarchy/workflow setup or onboarding walkthrough; use the individual component skills for isolated role, workspace or task operations.
---

# Guided agent workflow

Own the setup from this single invocation. Act as a temporary setup facilitator;
this duty is not a new hierarchy rank and does not make you PL or EL. Keep the
setup conversation here and launch leadership with fresh, focused context.
Do not send the user away to compose instructions for another agent.

Follow [the walkthrough](references/walkthrough.md). Inspect first, reuse settled
choices, and ask one consequential unresolved question at a time with a
recommendation and tradeoff. Explain what happens next in ordinary language.
The user supplies project-specific decisions; you perform the mechanical work.

## Compose the existing capabilities

This entry point is distributed with three companion skills. Locate them in the
installed bundle or its source checkout; load each only when its phase needs it:

- [agent-workspace](../agent-workspace/SKILL.md) maps records, permissions and
  workspaces without forcing a new repository layout.
- [agent-hierarchy](../agent-hierarchy/SKILL.md) starts/resumes roles and handles
  their scope, focused context, communication and handoffs.
- [agent-task](../agent-task/SKILL.md) prepares the selected tracker and task/report
  conventions. Defining implementation tasks is only needed when already in scope.

If a companion is missing, resolve the bundle location or use an available skill
installer within the setup authorization. Preserve existing installations and
customizations. Continue independent inspection while resolving a genuine blocker;
do not invent companion behavior or tell the user to orchestrate several prompts.
The three component skills remain independently usable.

## Finish with an operational handoff

Prepare the agreed project setup, verify the relevant capabilities, generate and
deliver role briefs with a concrete immediate objective, and verify the intended
contact's first useful response. For planning, that response briefly confirms the
handoff and addresses the next consequential unresolved question from known context.
If sufficiently scoped, it states the next authorized action or actual missing gate.
Do not invent a question or instruct the recipient to merely acknowledge and wait
unless the user requested an acknowledgment-only diagnostic.

Setup and ordinary human/leadership conversations need no numeric allowance by
default. Resolve actual launch authority or explicitly imposed limits
here; never invent a project-lifetime cap or reuse an unrelated pilot budget.

Reuse existing occupants when resuming setup. Start only the roles needed now,
then let leadership grow the team. Explain who the user should talk to and why,
using actual session names and available open/resume controls. The user's next
conversation should concern the project, not how to assemble the workflow.

Report what is ready, what remains unverified and any blocker that prevents
handoff. Setup remains your responsibility until accepted by its recipient; a
configuration file or a queued message alone does not complete the handoff.
