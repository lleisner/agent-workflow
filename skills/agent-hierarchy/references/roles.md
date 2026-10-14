# Role responsibilities and profile selection

The native profiles contain their complete role instructions. When a profile is
already loaded, do not read all source files again. For a manual role assignment,
read only the relevant role source and applicable shared supervision contract.
Project records determine actual scope, occupants, permissions and active roles.

| Role | Responsibility | Profile | Authoritative role source |
| --- | --- | --- | --- |
| UL | User understanding, decisions and attention | `user_liaison` | [UL](profile-sources/user_liaison.md) |
| PL | Single project-wide executive; coordinates EL scopes | `project_lead` | [PL](profile-sources/project_lead.md) |
| EL | Ongoing execution coordination across assigned areas | `execution_lead` | [EL](profile-sources/execution_lead.md) |
| AC | Area outcomes and coordination/integration of TC deliverables | `area_coordinator` | [AC](profile-sources/area_coordinator.md) |
| TC | One bounded deliverable, its workers, review and integrated result | `task_coordinator` | [TC](profile-sources/task_coordinator.md) |
| W | Bounded contribution and correction | `workflow_worker` | [Worker](profile-sources/workflow_worker.md) |
| Review helper | Independent assessment of combined work | `integration_reviewer` | [Reviewer](profile-sources/integration_reviewer.md) |
| PL+EL | Both executive responsibilities in one occupant | `project_execution_lead` | PL + EL + [combination](profile-sources/combined_leads.md) |
| AC+TC | One area and its single TC deliverable | `area_task_coordinator` | AC + TC + [combination](profile-sources/combined_coordinators.md) |

Supervisors use the [shared supervision contract](profile-sources/supervision.md).
Combined occupants also use the [transfer rules](profile-sources/combined.md).
Workers, UL and reviewers receive their focused instructions rather than the full
supervisor contract. Specialists are bounded helpers available to any responsible
role, not another hierarchy rank; add a specific profile only for a useful recurring
capability. There is no generic specialist profile to launch by default.

The initial design is UL plus one executive PL+EL. Separate executive PL requires
an authorized expansion to multiple ELs. Standalone PL's effort is deliberately
unspecified until that later launch is agreed. One logical PL remains per project.
The former conversation-first PL is now UL: historical PL+EL titles are not evidence
that a live occupant has adopted the new executive combination. Reconcile assignments
explicitly when adopting this revision.

See [profile assembly and startup](profiles.md) for assets, settings, installation
boundaries and runtime verification. Profile names are reusable types; session names
and logical role IDs identify individual occupants.
