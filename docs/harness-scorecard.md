# Harness Scorecard

This repo is designed to demonstrate an 8/10 harness: comprehensive enough to
teach the discipline, small enough to understand in one sitting.

## Score

| Dimension | Score | Evidence |
| --- | ---: | --- |
| Context | 8 | `AGENTS.md`, architecture docs, prompt recipes, task briefs |
| Execution | 8 | Standard-library app, `Makefile`, one-command local quality gate |
| Feedback | 8 | Unit tests, syntax compilation, CLI smoke test, harness doctor |
| Governance | 8 | PR template, issue template, design constraints, ADR expectation |
| Memory | 8 | Architecture docs, ADRs, runbook, scorecard, task archive |

Overall harness comprehensiveness: **8/10**.

## What Makes It an 8

The harness does more than document intentions. It gives an agent a repeatable
path from context to implementation to verification:

1. Read `AGENTS.md`.
2. Read the architecture and task brief.
3. Change the smallest relevant module.
4. Add tests.
5. Run `python3 scripts/check.py`.
6. Explain the result using the PR template or final response.

## What Would Make It a 10

- Real application telemetry and logs.
- Mutation or coverage thresholds.
- Static typing with `mypy` or `pyright`.
- Formatting and linting with pinned tool versions.
- Multiple services with realistic setup scripts.
- Production-like data fixtures and failure traces.
