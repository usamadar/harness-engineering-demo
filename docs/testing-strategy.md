# Testing Strategy

The test suite is intentionally small, but it demonstrates the feedback loop an
agent needs before it can make reliable changes.

## Test Layers

- Syntax compilation catches broken Python before tests run.
- Lint checks catch formatting issues, missing docstrings, and architecture drift.
- Unit tests validate routing behavior in `TicketRouter`.
- CLI smoke tests verify the command-line adapter stays connected to the app.
- Harness checks verify the repo still contains the context agents need.

## Test Ownership

Routing behavior belongs in `tests/test_router.py`. When a classification rule
changes, update that file first or alongside the code change.

CLI behavior belongs in `tests/test_cli.py`. Keep these tests focused on adapter
behavior, not business logic.

Harness behavior belongs in `tests/test_harness_doctor.py`. These tests protect
the teaching repo itself.

## Local Command

```bash
python3 scripts/check.py
```

This is the only command a contributor or agent needs before finishing a task.
