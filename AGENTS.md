# Agent Instructions

You are working in a teaching repo for harness engineering. Keep changes small,
clear, and easy to explain to a team learning how agents work.

## Project Shape

- Application code lives in `src/harness_demo`.
- Tests live in `tests`.
- Repo context lives in `docs`.
- Agent practice tasks live in `tasks`.
- Quality gates live in `scripts`.

## Required Workflow

Before changing code:

1. Read `docs/architecture.md`.
2. Read the task file in `tasks/` if one is referenced.
3. Identify the smallest code change that satisfies the acceptance criteria.

Before finishing:

1. Run `python3 scripts/check.py`.
2. Mention any command that failed and why.
3. Keep explanations focused on behavior, tests, and verification.

## Coding Standards

- Prefer small functions with one responsibility.
- Use type hints on public functions.
- Use dataclasses for simple value objects.
- Raise specific exceptions for invalid application states.
- Avoid hidden network calls, environment dependencies, or global mutable state.
- Do not add third-party dependencies unless a task explicitly requires them.

## Testing Standards

- Use `unittest` from the standard library.
- Test names should describe behavior.
- Add or update tests when changing classification rules.
- The quality gate is `python3 scripts/check.py`.
