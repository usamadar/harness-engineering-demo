"""Checks lightweight documentation contracts for the demo harness."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_DOC_SNIPPETS = {
    "AGENTS.md": ("Required Workflow", "Coding Standards", "Testing Standards"),
    "docs/architecture.md": ("Modules", "Design Rules", "Classification Model"),
    "docs/harness-map.md": (
        "Context Layer",
        "Execution Layer",
        "Feedback Layer",
        "Governance Layer",
        "Memory",
    ),
    "docs/harness-scorecard.md": ("Overall harness comprehensiveness", "8/10"),
    "docs/testing-strategy.md": ("Test Layers", "Local Command"),
    "docs/runbook.md": ("Run the App", "Run the Quality Gate", "Common Failures"),
    "docs/prompt-recipes.md": ("Complete a Task", "Ask for a Harness Review"),
}


class DocumentationCheckError(Exception):
    """Raised when required documentation content is missing."""


def find_missing_snippets() -> list[str]:
    """Finds missing required documentation snippets.

    Returns:
        Human-readable descriptions of missing documentation content.
    """

    missing_snippets = []
    for relative_path, snippets in REQUIRED_DOC_SNIPPETS.items():
        content = (REPO_ROOT / relative_path).read_text(encoding="utf-8")
        for snippet in snippets:
            if snippet not in content:
                missing_snippets.append(f"{relative_path}: {snippet}")

    return missing_snippets


def main() -> None:
    """Runs documentation contract checks.

    Raises:
        DocumentationCheckError: Raised when required snippets are missing.
    """

    missing_snippets = find_missing_snippets()
    if missing_snippets:
        formatted_snippets = ", ".join(missing_snippets)
        raise DocumentationCheckError(f"Missing documentation: {formatted_snippets}")

    print("Documentation checks: ok")


if __name__ == "__main__":
    main()
