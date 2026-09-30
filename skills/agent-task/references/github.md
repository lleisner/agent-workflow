# GitHub records

Use an existing authorized GitHub connection or gh CLI. The optional
scripts/github_records.py helper uses gh without exposing credentials. It has no
background polling and sends no conversational messages.

## Starter labels and identity

Initialize the small vocabulary with init-labels in the chosen repository:
aw:task, aw:coordination, aw:draft, aw:ready, aw:active, aw:review, aw:paused.
Closed issues represent accepted completion or cancellation, with the reason and
actual integration evidence recorded. A scoped blocker need not pause the entire
task when other authorized work can proceed.

Only open aw:task issues with aw:ready are eligible for pickup. An issue's native
number supplies the numeric part of its project task ID: issue 21 becomes PCT021.
Coordination issues also have GitHub numbers but never receive task IDs.

## Mechanical helpers

~~~sh
python3 scripts/github_records.py init-labels --repo OWNER/REPO
python3 scripts/github_records.py create-task --repo OWNER/REPO --prefix PCT \
  --key export-validation --title "Export validation" --body-file /path/task.md
python3 scripts/github_records.py report --repo OWNER/REPO --issue 21 \
  --key W1-tests --body-file /path/report.md
~~~

Creation uses a stable caller-chosen key. Retry with the same key after an
uncertain result rather than creating another issue. Dispatching/creating multiple
tasks with the same key concurrently is not supported; the coordinator owns that
operation. Existing issue content is preserved on a creation retry.

Reports use one marker and editable comment per assignment key. The helper
updates the existing comment and returns its direct URL. Duplicate matching
records fail visibly instead of choosing arbitrarily. Each assignment's owner is
the normal writer; replacement can continue that record. Empty reports fail.

Use the same report mechanism for TC contributions to an AC coordination issue,
and AC contributions to an EL coordination issue. Higher levels synthesize the
implication at their scope; they do not copy raw child content.

The helper operates on the explicitly selected repository/issue. Skills and the
project agreement govern authorization. Do not export private evidence to GitHub.
Avoid mentioning unrelated people or sending notifications outside the task scope.

## Updates and integration

Use native gh/connector operations for phase changes, PRs and review. Keep one
phase label at a time and preserve unrelated labels. Verify current status/owner
before dispatch; a read-then-write claim requires coordination, not an assertion
of collision-proof locking.

Choose a GitHub Project table/board if useful; it is a view over these issues.
Define each field's authority once, avoiding duplicated mutable status in repo
files. The initial helper does not create a Project or copy live state locally.
