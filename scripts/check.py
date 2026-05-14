"""Orchestrates the full quality gate for the harness engineering demo."""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CHECK_COMMANDS = (
    ("syntax", "scripts/check_syntax.py"),
    ("lint and architecture", "scripts/lint.py"),
    ("harness doctor", "scripts/harness_doctor.py"),
    ("documentation contracts", "scripts/check_docs.py"),
    ("unit tests", "scripts/check_tests.py"),
    ("CLI smoke", "scripts/check_smoke.py"),
)


class QualityGateError(Exception):
    """Raised when one or more quality-gate steps fail."""


def run_check(name: str, script_path: str) -> None:
    """Runs one quality-gate check from the repository root.

    Args:
        name: Human-readable check name.
        script_path: Script path relative to the repository root.

    Raises:
        QualityGateError: Raised when the command exits unsuccessfully.
    """

    command = [sys.executable, script_path]
    result = subprocess.run(command, cwd=REPO_ROOT, check=False)
    if result.returncode != 0:
        raise QualityGateError(f"{name} check failed: {script_path}")


def main() -> None:
    """Runs all local verification for the repository."""

    for name, script_path in CHECK_COMMANDS:
        run_check(name, script_path)

    print("Quality gate: ok")


if __name__ == "__main__":
    main()
