# Codex host operations

The role protocol is independent of this adapter. Check the installed CLI's help
and authentication mode. Use the user's existing subscription login for a
subscription-only pilot; do not configure an API key or change account settings.

## Visible sessions

Use separately addressable sessions for roles requiring direct human input when
native child sessions are read-only in the chosen interface. Start in the owned
workspace with the focused brief, using existing permissions/configuration:

~~~sh
codex --cd /path/to/owned/worktree "Focused role brief and record references"
~~~

Session creation spends model resources and requires the current task's grant.
Do not broaden sandbox or disable approval merely to make a workflow run.

Use scripts/session.py rename --thread ID --project PATH --name TEXT for native
name/readback through a short-lived stdio app-server client. This does not launch
a model task. The adapter verifies the session's cwd belongs to the stated
project/worktree root. It does not write Codex databases.

Use scripts/session.py send --thread ID --message-file PATH [--remote unix://]
for an authorized message to an existing independent session. Successful queueing
is only acceptance of delivery; require an acknowledgment where continuation
depends on receipt. Current host behavior for unloaded sessions must be tested.

Inspect/resume using native Codex controls. A name is a display label, not a
session address or permission. Keep the immutable session identifier in the
canonical role/assignment record.

## Selecting speed

CLI sessions can select their own tier with `-c service_tier="default"` for
Standard or `-c service_tier="fast"` for Fast; `/fast` is the interactive toggle.
Use current [speed documentation](https://learn.chatgpt.com/docs/agent-configuration/speed#fast-mode)
and verify availability/readback rather than changing the global config.

The installed app-server schema is authoritative for programmatic controls. On
CLI 0.160.0, `thread/start` accepts `serviceTier`, and `thread/settings/update`
accepts `threadId` plus `serviceTier` for subsequent turns. A no-inference probe
confirmed `default` at startup, `fast` normalized to `priority`, and a subsequent
switch to `default` through the `thread/settings/updated` notification. It did not
benchmark latency, charges or persistence after reattachment.

The currently exposed `create_thread` and native `spawn_agent` wrappers have no
service-tier argument. Their child-tier inheritance was not established by that
probe. Do not pass invented arguments or claim prompt text sets the tier. Use a
verified host route before the first model turn, or ask for the needed host/user
setting when that route is unavailable. Do not take over an active session's
writer merely to alter settings. Keep allowance accounting consistent with the
selected tier as described in [resources](resources.md).

## Native helpers

For bounded temporary helpers, use the host's native sub-agent facility when
available and authorized. The user need not interact directly with these helpers.
Choose fresh focused context; account for their usage under the delegator. Native
send_message may queue without waking a completed agent; use the host's documented
wake/follow-up operation when needed.

Task hiding is documented in some Codex versions, but automatic hiding of helpers
has not been demonstrated by this package. Do not archive/delete running sessions
to approximate hiding. Preserve reports and evidence.

## Session retirement

Prefer reversible archiving for routine completed-role cleanup under the project's
grant. The exposed `set_thread_archived` operation can archive by immutable thread
ID. The [app-server API](https://learn.chatgpt.com/docs/app-server#api-overview)
also documents `thread/archive`, `thread/unarchive` and permanent `thread/delete`.
CLI 0.160.0 also exposes `codex archive UUID`, `codex unarchive UUID` and
`codex delete UUID`; prefer immutable IDs over display names. These are native
capabilities, not commands added to this package's session helper. Archive/delete can include spawned descendants; check actual native ancestry as
well as logical role ownership before acting. Restoring the parent alone does not
necessarily restore its descendants.

Follow [lifecycle closeout](lifecycle.md#end-or-replace) first. Archive retains
recoverable history; deletion removes it and requires the applicable explicit
retention/deletion authority. Neither is Git worktree cleanup. Do not edit Codex's
databases or remove session files manually. Archive/delete is documented and the
local schema includes it, but no live session was archived/deleted in this check.

## Limits

This package does not ship a daemon, unattended scheduler, remote-control server
or terminal multiplexer. It uses the user's existing runtime. Skills alone cannot
guarantee that an unloaded agent wakes or that a sleeping laptop executes work.
Choose and verify a supported active host/session arrangement before unattended
use. Logical supervisory changes do not imply native reparenting.
