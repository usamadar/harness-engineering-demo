"""Checks whether the teaching repo still has a useful agent harness."""

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
REQUIRED_PATHS = (
    ".github/ISSUE_TEMPLATE/agent-task.md",
    ".github/pull_request_template.md",
    ".github/workflows/quality.yml",
    "AGENTS.md",
    "Makefile",
    "README.md",
    "docs/adr/0001-keep-demo-standard-library-only.md",
    "docs/adr/0002-route-business-rules-through-router.md",
    "docs/architecture.md",
    "docs/harness-map.md",
    "docs/harness-scorecard.md",
    "docs/prompt-recipes.md",
    "docs/runbook.md",
    "docs/testing-strategy.md",
    "tasks/01-add-sla-classification.md",
    "tasks/02-add-customer-success-routing.md",
    "scripts/check.py",
    "scripts/check_docs.py",
    "scripts/harness_doctor.py",
    "tests/test_cli.py",
    "tests/test_harness_doctor.py",
    "tests/test_router.py",
)


class HarnessDoctorError(Exception):
    """Raised when a required harness file is missing."""


def find_missing_paths() -> list[str]:
    """Finds required harness paths that are missing.

    Returns:
        A list of missing path strings relative to the repository root.
    """

    return [path for path in REQUIRED_PATHS if not (REPO_ROOT / path).exists()]


def main() -> None:
    """Runs the harness readiness check.

    Raises:
        HarnessDoctorError: Raised when required harness files are missing.
    """

    missing_paths = find_missing_paths()
    if missing_paths:
        formatted_paths = ", ".join(missing_paths)
        raise HarnessDoctorError(f"Missing harness files: {formatted_paths}")

    print("Harness doctor: ok")


if __name__ == "__main__":
    main()
