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

## Native helpers

For bounded temporary helpers, use the host's native sub-agent facility when
available and authorized. The user need not interact directly with these helpers.
Choose fresh focused context; account for their usage under the delegator. Native
send_message may queue without waking a completed agent; use the host's documented
wake/follow-up operation when needed.

Task hiding is documented in some Codex versions, but automatic hiding of helpers
has not been demonstrated by this package. Do not archive/delete running sessions
to approximate hiding. Preserve reports and evidence.

## Limits

This package does not ship a daemon, unattended scheduler, remote-control server
or terminal multiplexer. It uses the user's existing runtime. Skills alone cannot
guarantee that an unloaded agent wakes or that a sleeping laptop executes work.
Choose and verify a supported active host/session arrangement before unattended
use. Logical supervisory changes do not imply native reparenting.
