# Profile assembly and startup

## Author once, assemble complete profiles

[Role selection](roles.md) maps logical responsibilities to concrete profiles.
Sources and the packaging manifest live in `references/profile-sources/`.
The manifest selects ordered sources and the agreed reasoning default; it is not
a second project agreement or a general settings editor. Role sources own the
role policy; the shared contract owns supervision policy. Skill references own
procedures, while project records hold assignments, gates, resources and occupants.

From this skill directory:

~~~sh
python3 scripts/profiles.py --write
python3 scripts/profiles.py --check
~~~

The assembler writes complete TOML files under `assets/agents/` and nothing else.
It does not install, launch, rename, message or reconfigure any agent. Generated
files contain the applicable instructions, including both role definitions for
combined profiles; they do not depend on undocumented native profile inheritance.
Edit sources and regenerate, rather than editing generated assets. Check mode
detects missing, edited and unexpected TOML assets without modifying them. Write
mode preserves unrecognized files by failing for manual review rather than deleting
them. Copies of the installed skill remain self-contained.

## Settings and adoption

The pilot assets inherit the selected model and project permissions by omitting
model, sandbox and approval-policy overrides. They request Standard service tier.
Worker/reviewer request medium reasoning, TC/AC and AC+TC high, and EL, PL+EL and
UL xhigh. UL's xhigh is a fallback: preserve any already agreed project-specific
setting on adoption. Standalone executive PL inherits effort pending a separate
decision before an authorized multi-EL deployment. See [resource policy](resources.md).

Custom profile effort settings take precedence over explicit spawn effort settings
in the documented native route. Do not promise that a contrary launch argument
overrides a profile. If an agreed project exception differs from an asset, prepare
and review a project-specific copy, record that exception in the existing project
agreement, then verify effective settings. Do not silently overwrite customized
copies when updating bundled assets or change account-wide defaults.

According to [official custom-agent documentation](https://learn.chatgpt.com/docs/agent-configuration/subagents#custom-agents),
Codex discovers standalone files in project `.codex/agents/` or personal
`~/.codex/agents/`. Installing this skill does not by itself install its assets
there. During authorized adoption, inspect existing files and copy only the required
reviewed profiles to the chosen location without clobbering local customizations.
The generated `name` identifies the native profile; it is not the occupant's title.
Prefer project scope for project-specific policy. Leave unrelated profiles intact.

## Guided startup procedure

1. Reuse the current project agreement and occupants. Identify required active
   roles and select their profile with the role table. Combined PL+EL means the
   executive combination; keep UL separate. Do not create every role merely
   because an asset exists.
2. Establish actual launch authority and permissions, inherited model and any
   settings exceptions. Use the existing records; no new settings system is needed.
3. Inspect the chosen host's supported launch/configuration route. Native custom
   agents are documented as configuration layers for spawned sessions. This does
   not prove that an independently addressable human-facing session can load them.
   If the launcher exposes no profile selector, do not invent an argument or claim
   a role name in a prompt loaded the file. Use a documented configuration route
   only after verifying it carries the assembled instructions/settings; otherwise
   report that specific limitation and keep the launch pending.
4. Supply a focused assignment separately from the reusable profile: actual scope,
   active duties, supervisor/contacts, project/worktree, authoritative records,
   grants/resource policy, immediate objective and first useful response. Locate
   the installed skill and relevant procedure references for the new session.
   Do not copy an entire parent conversation or all project history.
5. During the separately authorized runtime check, verify effective instructions,
   settings, owned workspace, session identity and required user/message access.
   Record observed support and unresolved limitations. A valid TOML file or a
   successful message queue operation is not evidence of all these behaviors.

For resuming or splitting, follow [lifecycle](lifecycle.md). Existing sessions do
not automatically adopt an edited profile. A combined occupant may retain its
profile after explicitly relinquishing an upper role; current assignments determine
active duties. Logical transfer is not native reparenting or an automatic permission
change. Preserve running work and the agreed one-time transfer confirmation.

## Validation boundary

The repository checks source/output consistency, TOML roundtrips, composition and
settings without model calls. Python 3.9+ runs the assembler; use Python 3.11+ for
the standard-library TOML parsing tests. Native loading, direct human access and
split behavior on the chosen session route remain runtime checks, not assertions
made by this packaging step. The CLI 0.162.0 configuration schema was inspected
for the requested effort and service-tier fields; runtime policy may still constrain
them. No SDK or additional orchestration service is required by this assembly.
