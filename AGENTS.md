# Working agreement

Read README.md and docs/DESIGN.md before changing behavior. Check Git status and
branch first, preserve existing work, and keep every installable skill
self-contained. Changes to one capability must not make the other mandatory.

Keep the skill entrypoints short. Put role-specific guidance and mechanical
details in linked references/scripts. Coordinators decide operational tactics;
do not turn examples into universal policies.

Run python3 -m unittest discover -s tests -v and python3 scripts/validate.py after
changing helpers. Use synthetic fixtures. Do not start live agents, spend model
allowances, alter account settings or access a user's other projects as incidental
validation; use the current task's explicit scope and allowance.

Record observed runtime limitations in docs/VALIDATION.md. Skill prose and unit
tests do not establish that native sessions remain alive, wake unattended, accept
direct input or support hiding. Keep hidden helper usage in parent budgets.
