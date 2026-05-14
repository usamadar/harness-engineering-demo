"""Runs a smoke test through the command-line application path."""

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPO_ROOT / "src"
SMOKE_TEXT = "Cannot log in to production"
EXPECTED_LINES = (
    "queue=incident",
    "priority=high",
)


class SmokeCheckError(Exception):
    """Raised when the command-line smoke check fails."""


def run_cli_smoke_check() -> None:
    """Runs the CLI smoke check.

    Raises:
        SmokeCheckError: Raised when the CLI exits unsuccessfully or prints an
            unexpected routing decision.
    """

    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(SOURCE_ROOT)
    result = subprocess.run(
        [sys.executable, "-m", "harness_demo.cli", SMOKE_TEXT],
        cwd=REPO_ROOT,
        check=False,
        env=environment,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise SmokeCheckError("CLI smoke check failed to run.")

    missing_lines = [line for line in EXPECTED_LINES if line not in result.stdout]
    if missing_lines:
        formatted_lines = ", ".join(missing_lines)
        raise SmokeCheckError(f"CLI smoke output missing: {formatted_lines}")


def main() -> None:
    """Runs the CLI smoke check."""

    run_cli_smoke_check()
    print("Smoke check: ok")


if __name__ == "__main__":
    main()
