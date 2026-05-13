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
Harness doctor: ok
Quality gate: ok
```

## Common Failures

If imports fail, confirm the command is running from the repo root. The quality
gate sets `PYTHONPATH=src` automatically.

If the harness doctor fails, restore the missing harness file or update
`scripts/harness_doctor.py` only when the harness contract intentionally changes.

If tests fail after a rule change, inspect `tests/test_router.py` before changing
the CLI. Business rules should stay in `TicketRouter`.
