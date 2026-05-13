# Harness Map

This file names the parts of the repo that help an agent produce better work.

## Context Layer

- `AGENTS.md` gives repo-specific working instructions.
- `docs/architecture.md` gives the system map and design rules.
- `tasks/` contains task briefs with acceptance criteria.

## Execution Layer

- The app uses only Python standard library modules.
- Commands run from the repo root.
- No external services are required.

## Feedback Layer

- `python3 scripts/check.py` runs all verification.
- `scripts/lint.py` checks formatting, docstrings, and architecture boundaries.
- Unit tests validate routing behavior.
- `scripts/harness_doctor.py` checks whether harness files are present.
- `scripts/check_docs.py` verifies key documentation contracts.

## Governance Layer

- Business rules belong in `TicketRouter`.
- The CLI must stay thin.
- `scripts/lint.py` fails if business-rule terms appear in the CLI.
- New classification behavior requires tests.
- The pull request template asks contributors to report verification.

## Memory Layer

- `docs/adr/` records architectural decisions.
- `docs/runbook.md` captures repeatable operating steps.
- `docs/harness-scorecard.md` explains the harness maturity target.
- `docs/prompt-recipes.md` preserves reusable teaching prompts.

## Teaching Prompt

Try this with a coding agent:

```text
Complete tasks/01-add-sla-classification.md.
```
