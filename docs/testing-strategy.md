# Testing Strategy

The test suite is intentionally small, but it demonstrates the feedback loop an
agent needs before it can make reliable changes.

## Test Layers

- `scripts/check_syntax.py` catches broken Python before deeper checks run.
- `scripts/lint.py` catches formatting issues, missing docstrings, and
  architecture drift.
- `scripts/harness_doctor.py` verifies the repo still contains the context
  agents need.
- `scripts/check_docs.py` verifies required documentation sections remain
  present.
- `scripts/check_tests.py` runs unit tests for routing and adapter behavior.
- `scripts/check_smoke.py` verifies the command-line adapter stays connected to
  the app.

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
It is intentionally an orchestrator: learners can inspect each smaller feedback
script to understand what signal it provides.
