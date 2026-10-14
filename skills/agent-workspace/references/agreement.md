# Project agreement

The agreement can be an existing document, a compact configuration plus prose, or
another clearly identified record. Keep semantic requirements stable and paths
configurable. A setup conversation resolves gaps once; agents subsequently load
their relevant slice.

Answer:

| Concern | Required information |
| --- | --- |
| Direction | Goals/non-goals, priorities, accepted decisions and initiative/area briefs |
| Authority | Who may define/start work, allocate resources, review and integrate at each boundary |
| Records | Canonical location AND branch/ref for published docs; task/report/role locations |
| Runtime | How to create/address/name/wake sessions; user-facing vs helper visibility |
| Resources | Bounded-work resource policy, observation owner, model settings and explicit limits; optional numerical allowances/time-window allocation |
| Git | Integration/stable targets, worktree root, ownership and evidence/check commands |
| Recovery | Current occupant references, checkpoint locations and workspace preservation |

Do not put live spending, task status and copies of every report in this agreement.
Point to their authoritative records. Changes of permission are explicit and
independent of changes in role titles or merge/start presets.

## Optional JSON mapping

The asset uses schema_version 1 and fields project, records, branches, authority,
resources and runtime. Location strings may be local repository-relative paths or
URLs. The canonical_ref describes which published document version is authoritative.
Resolve current records from that ref or the hosted version instead of silently
using the copy in a task branch.

The pilot example allows task starts within approved area scope and coordinator
acceptance of worker-to-task and task-to-area integration. Human approval remains
at area-to-project integration and stable promotion. Record structural gates too:
the pilot requires user approval for new/split areas and added executive capacity.
These are settings to agree on adoption, not grants created by copying an asset.

Numerical allowances are optional. Add resources.ledger only when using a ledger;
the path alone neither sets a limit nor enables accounting. Preserve explicit
limits in the authoritative grant even when no local ledger is used.

Use a private, ignored host directory for native session logs and the local usage
ledger. GitHub is the live task/report authority in this starter. Published grants
can link accounting snapshots without exposing credentials or unrelated sessions.

## Publishing records

Assign one owner per logical record. Contributors prepare separate bounded
documentation changes against the canonical branch under the current gate.
Code PRs must not overwrite live planning state with a stale branch-local copy.
Changing a task's phase is based on actual evidence and its configured integration
target; merged into an area is not automatically released to the stable branch.

The canonical source may be dev with main as the reviewed stable baseline.
AC integration branches and TC worktrees can contain drafts. Publish agreed
decisions independently of unfinished code when other work needs them.

## Template repositories

Adapt starter files when they help a new project; existing projects keep their
useful conventions. Validate the mapping on bounded real work or a small fixture
as appropriate. A separate practice project is not a prerequisite. A dedicated
template repository remains optional later work. Create new working branches from
the generated repository's initial branch: GitHub's option to copy all template
branches creates unrelated histories.

## Worktree helper

After the scope owner assigns the branch and location:

~~~sh
python3 scripts/worktree.py --repo /path/project --root /path/project-worktrees \
  --area export --task PCT007 --assignment W1 \
  --base dev --branch task/PCT007-W1
~~~

The helper checks the selected base but does not fetch automatically; verify its
freshness before using it. It creates the leaf only, preserves existing checkouts
and refuses existing targets, unsafe segments and nesting within another checkout.
Use git worktree list for inspection. Cleanup remains an explicit separate action.
