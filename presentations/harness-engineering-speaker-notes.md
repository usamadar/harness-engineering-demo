# Harness Engineering Workshop Speaker Notes

## 1. Harness engineering is the work around the agent.

Open by separating the model from the system around it. The agent may write the
code, but the harness gives it context, tools, checks, and boundaries.

## 2. A harness gives an agent five kinds of traction.

Walk through the five layers: context, execution, feedback, governance, and
memory. Emphasize that each layer reduces ambiguity for both humans and agents.

## 3. The prompt gets shorter as the harness gets stronger.

Say the goal clearly: durable instructions should move out of prompts and into
the repo. The best demo prompt is simply `Complete tasks/01-add-sla-classification.md`.

## 4. Our demo repo keeps the app tiny and the harness visible.

Explain that the app is intentionally small: a ticket router. The repo is the
teaching object because the harness is easy to inspect.

## 5. The harness tells the agent what to read and where to change code.

Show how the task brief, `AGENTS.md`, architecture docs, router, and tests form
a path. This narrows the search space before the agent edits.

## 6. The quality gate makes standards executable.

Run `python3 scripts/check.py`. Point out the sequence: lint, harness doctor,
docs checks, tests, and CLI smoke test.

## 7. Coding standards become rules, not wishes.

Use the CLI architecture rule as the concrete example. The standard says
business rules belong in `TicketRouter`; the linter enforces that boundary.

## 8. The live demo should need only one short task prompt.

Use this prompt: `Complete tasks/01-add-sla-classification.md`. After the agent
finishes, show `git diff` and run `python3 scripts/check.py`.

## 9. Failure is a feature when the harness catches drift.

Optional live moment: move `docs/runbook.md` temporarily and run the quality
gate. Restore it afterwards. The point is that drift becomes visible.

## 10. Build the harness in layers.

Give the team a practical path: first instructions and one command, then CI and
runbooks, then architecture checks and recurring cleanup.

## 11. Less prompt ritual. More engineering leverage.

Close with the operating principle: treat bad agent output as feedback about
the harness. Improve the system, not just the prompt.
