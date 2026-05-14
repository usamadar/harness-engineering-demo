# Runbook

Use this runbook during live demos or when repairing the repo.

## Run the App

```bash
PYTHONPATH=src python3 -m harness_demo.cli "Cannot log in to production"
```

Expected result:

```text
queue=incident
priority=high
```

## Run the Quality Gate

```bash
python3 scripts/check.py
```

Expected result:

```text
Syntax check: ok
Lint: ok
Harness doctor: ok
Documentation checks: ok
Unit tests: ok
Smoke check: ok
Quality gate: ok
```

## Run Individual Feedback Checks

Use these during teaching to show that the quality gate is a chain of smaller
signals:

```bash
python3 scripts/check_syntax.py
python3 scripts/lint.py
python3 scripts/harness_doctor.py
python3 scripts/check_docs.py
python3 scripts/check_tests.py
python3 scripts/check_smoke.py
```

## Common Failures

If imports fail, confirm the command is running from the repo root. The quality
gate sets `PYTHONPATH=src` automatically.

If the syntax check fails, inspect the Python file named by the compiler before
running deeper checks.

If lint fails, inspect the reported file and line. The linter enforces basic
formatting, docstrings, and the rule that business logic stays out of the CLI.

If the harness doctor fails, restore the missing harness file or update
`scripts/harness_doctor.py` only when the harness contract intentionally changes.

If tests fail after a rule change, inspect `tests/test_router.py` before changing
the CLI. Business rules should stay in `TicketRouter`.

If the smoke check fails, the CLI path is disconnected from the application or
prints an unexpected routing decision.
