# Review and delivery

The coordinator owns the result and may delegate detailed integration/checks.
Use the current project agreement for target branches, commands and gates.

1. Refresh assignment reports and actual Git state. Identify acceptance gaps,
   scope changes, uncertainty and resource implications.
2. Integrate selected ready contributions in the assigned task workspace. Do not
   pull unrelated unfinished work because it is on a convenient branch.
3. Run relevant checks and obtain required independent review. Specify the outcome,
   integrated version, review scope, acceptance/evidence, prior coverage and repair
   owner. Review combined behavior and gaps; reuse lower-level coverage while its
   version and assumptions remain valid. Reopen affected checks when warranted.
4. Evaluate findings against intended behavior and recorded trade-offs. Reviewers
   remain review-only; named repair owners handle ordinary corrections directly
   with them, followed by a targeted recheck. The coordinator resolves disagreements
   and wider consequences. Continue necessary refinements before declaring readiness;
   persistent failure calls for reassessment. Optional additions require judgment
   by the owner able to assess their value and authority.
5. Prepare a concise PR explaining resulting behavior, checks, limitations and the
   task link. At a human integration gate, present the decision in chat: intended
   outcome, demonstrated change, suitable evidence or a usable preview, material
   discoveries/limits, recommendation and exact authorization requested. Assume
   the user has not followed execution. Complete ordinary repairs and required
   review first; agent reports or a review-passed assertion are not sufficient
   human evidence. The actual project gate determines when approval is needed.
6. Verify integration on the intended target and update the authoritative task/
   report record. Mark stable promotion separately when applicable.

TC-to-AC integration can finish a task even while the area awaits project
integration, if that is the task's agreed acceptance target. Never imply a stable
release from a task/area merge alone. AC curates coherent area increments before
the next integration decision rather than forwarding intermediate worker output.

Workers, coordinators and EL may each have integration worktrees. Combined roles
can collapse stages. Keep workspace allocation independent of approval policy.

Scope-local technical choices and dependency scheduling remain coordinator
judgments. Use small evidence lookups or delegate substantial investigation to
avoid filling leadership context with implementation details.
