# Validation status

Current source checks pass. An isolated UL/AC startup and access trial established
the results below; the full revised hierarchy has not completed a runtime cycle.
Unit tests establish helper behavior,
not autonomous judgment, unattended reliability or adoption by existing sessions.
Current behavior is defined in [the design](DESIGN.md) and linked role sources.
Historical experiments below are evidence, not alternative policy.

## Current local checks — 2026-10-13

- **29 tests pass on Python 3.12.** Python 3.9 passes with two TOML-parser tests
  skipped. No model calls or live project mutations are part of this suite.
- Ten profile tests cover deterministic composition, shared-source propagation,
  settings, TOML quoting/roundtrips, invalid input, regeneration, stale assets,
  preservation of unknown files/symlinks and an independently copied skill package.
- Nineteen helper tests cover allowance reservations/reallocation, recursive usage,
  replay/replacement, unknown usage and invalid counters; session extraction/naming
  guards; worktree isolation; mappings with optional accounting; GitHub pagination,
  creation retries and stable editable reports. Fixtures are synthetic and local.
- Package validation covers all four skills, references, Python syntax and profile
  source/output consistency. All four skills pass skill frontmatter validation.
- Nine complete TOML assets are assembled, including executive PL+EL and AC+TC.
  Configuration keys were checked against CLI 0.162.0 schema; native layout and
  effort precedence against [custom-agent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents).

The generator writes bundled assets only. Installed skills were confirmed as
separate copies, not links to the maintenance checkout. These changes have not
installed profiles, launched roles or changed live project grants/settings.

Static instruction review covers guided setup/resume, useful first responses,
continuing known authorized work, partial waits, concise reporting, user decisions,
scope-specific review/correction, integration evidence, role release confirmation,
shared-dev exclusive turns and closeout. It does not prove agents follow those
instructions. Superseded instruction-update narratives are retained in Git history.

## Observed runtime evidence

| Observation | Evidence and limits |
| --- | --- |
| 2026-09-29, macOS, CLI 0.158.0 / daemon 0.159.0 | Nested/peer messages, completed native-child wake through followup_task, active independent-session messages via queue, renaming/readback and token-category counters worked. The child viewer disabled direct human input. An idle disconnected session processed queued work after viewer resume; unattended wake and active detach survival were not established. Account quota was visible; per-thread account credits were not. |
| Subsequent early pilot | Independent leadership/area sessions and a legacy PL/EL split were established. Historical PL meant today's user-facing UL, so this does not validate the new executive split. Native messaging resumed an idle session after its CLI viewer released writer ownership. Another interface encountered an active-writer conflict. User-reported access was promising, but queued delivery alone did not establish writable attachment on every route. |
| Early pilot resource hold | Default session-list filtering omitted registered native-created sessions; soft allowances were exceeded before all roles checkpointed. Collection by exact participant IDs exposed missing usage. Registry/accounting guidance is a response to that finding, not tested hard budget enforcement. |
| 2026-10-08, CLI 0.160.0, no model turns | Two ephemeral thread starts returned default for Standard and priority for requested fast. A settings update and notification confirmed return to default. This tests per-thread configuration only, not inference speed/cost, detach persistence or launch-wrapper inheritance. Inspected wrappers lacked a per-call tier argument. Effort settings for subsequent turns were exposed in the schema, without a model-quality test. |
| Earlier private practice checks | Retried GitHub task creation reused one issue; editable report update preserved its ID/link. The usage reader returned an authorized session's cumulative native counters without transcript content. The packaged rename adapter still needs a live check; its unit test uses a fake native client. |

These observations are specific to the inspected host/version. Recheck relevant
capabilities on the selected route. Earlier pilot holds belong to those scopes;
they neither create a project-lifetime cap nor authorize unrelated work.

[App-server documentation](https://learn.chatgpt.com/docs/app-server), local schemas
and CLI help exposed archive/unarchive and permanent deletion, including descendant
effects. No real sessions or worktrees were retired to test those operations.
Local allowance locking supports macOS/Linux, not distributed/network-filesystem
writers; the ledger imports whole-session totals and does not stop native sessions.

## Isolated profile/access trial — 2026-10-14

Host: macOS, CLI 0.162.0, shared daemon 0.162.1, existing ChatGPT subscription.
Synthetic workspace only; no live project occupants were migrated or retired.

| Check | Observed result and limit |
| --- | --- |
| Independent role configuration | App-server `thread/start` received the generated AC and UL `developer_instructions` separately from each focused assignment, with the existing parent model, explicit Standard and read-only/on-request permissions. AC returned high effort, UL xhigh. AC's exact supplied instructions were present in its persisted developer instructions; resume without overrides retained high/Standard. This is explicit configuration from the assembled asset, **not native custom-agent name selection**. |
| Native custom-profile selection | The exposed `collaboration.spawn_agent` had no profile selector. AC correctly declined to substitute an unprofiled helper. A native reviewer fixture was present, but no custom-profile child was selected or validated on this route. |
| UL → independent AC | A separately configured UL used native task tools to message the AC directly. A completed reply was verified by readback, establishing receipt and idle wake on this route, not just queue acceptance. |
| UL → ordinary native child control | Read succeeded. Initial direct-message failure required parent resume. After the parent resumed, retry failed with code -32600: `direct app-server input is not allowed for multi-agent v2 sub-agents`. The control was deliberately unprofiled; this tests native-child access independently of custom-profile loading. |
| Human menu access | Agent Command Center showed the independent AC session. Opening it encountered a scratch-folder trust prompt; accepting persistent trust was rejected by automatic approval review and was not performed. Writable human attachment and native-child menu access remain unverified in this trial. |

The current native-child route does not meet the requirement that an independent
UL can directly contact every visible role. Keep independently addressable roles
on a route verified for direct input, with assembled instructions/settings applied
explicitly. Do not label that a successful native custom-agent launch. Native
children can still serve bounded helpers addressed through their parent.

Current [custom-agent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agent-file-schema)
says service tier follows the root session. The generated assets therefore omit
the ineffective child `service_tier` override. Standard remains the startup policy
and must be applied through the root/session controls. The trial did not benchmark
speed/cost, exercise Fast inheritance or test ongoing detach survival.

## Remaining runtime checks

Use a separately authorized, bounded real deliverable to test relevant behavior;
a new synthetic playground is not required before project work.

- Verify generated instructions and effective settings load through the chosen
  independently accessible session route; test direct human input, communication,
  idle wake and active detach on that host.
- Exercise a combined-role split while preserving lower-role work and a confirmed
  ownership transfer. New executive multi-EL operation remains deferred.
- Complete the worker review/correction, TC curation, area acceptance and configured
  human integration-evidence cycle; verify actual code/report destinations.
- When accounting is enabled, attribute participant/helper usage without double
  counting and preserve explicit limits. Observations are not exact subscription
  credit attribution or an enforcement guarantee.
- Verify recovery from concise records and authorized closeout/retirement, including
  helper visibility. Do not infer success from static documentation or queueing.

Select checks relevant to the next authorized step rather than imposing every
unknown as a prerequisite to useful work. Report untested capabilities explicitly.
