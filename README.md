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
- `scripts/check.py` runs the repo's quality gate.
- `scripts/lint.py` enforces style and architecture rules without dependencies.
- `scripts/harness_doctor.py` checks whether the repo remains agent-ready.
- `.github/` contains CI and collaboration templates.

## Quick Start

```bash
python3 scripts/check.py
PYTHONPATH=src python3 -m harness_demo.cli "Cannot log in to production"
```

## Teaching Flow

1. Show the team the tiny app in `src/harness_demo`.
2. Show the harness files: `AGENTS.md`, `docs/`, `tasks/`, and `scripts/`.
3. Ask Codex or another coding agent to complete `tasks/01-add-sla-classification.md`.
4. Run `python3 scripts/check.py`.
5. Review `docs/harness-scorecard.md` and discuss why this is an 8/10 harness.
6. Discuss what made the agent effective: clear intent, local context, fast tests,
   mechanical verification, governance, and repo memory.

## The Lesson

Prompting gives an agent intent. A harness gives it traction.
