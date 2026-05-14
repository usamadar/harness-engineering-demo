# Harness Engineering Demo

This is a tiny repo for teaching harness engineering: the practice of shaping
the environment around an AI coding agent so it can understand, change, test,
and verify software reliably.

The application is intentionally small. It classifies support tickets into
workflow queues. The important part is the harness around it:

- `AGENTS.md` tells an agent how to work in this repo.
- `docs/architecture.md` explains the design in one page.
- `docs/harness-map.md` explains the feedback loops available to the agent.
- `docs/harness-scorecard.md` defines the 8/10 harness target.
- `docs/adr/` records architectural decisions.
- `tasks/01-add-sla-classification.md` is a ready-made practice task.
- `scripts/check.py` orchestrates the repo's quality gate.
- `scripts/check_syntax.py` verifies Python files compile.
- `scripts/lint.py` enforces style and architecture rules without dependencies.
- `scripts/harness_doctor.py` checks whether the repo remains agent-ready.
- `scripts/check_docs.py` checks documentation contracts.
- `scripts/check_tests.py` runs unit tests.
- `scripts/check_smoke.py` verifies the CLI path.
- `.github/` contains CI and collaboration templates.

## Quick Start

```bash
python3 scripts/check.py
PYTHONPATH=src python3 -m harness_demo.cli "Cannot log in to production"
```

## The Lesson

Prompting gives an agent intent. A harness gives it traction.
