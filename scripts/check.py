"""Runs the full quality gate for the harness engineering demo."""

import compileall
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPO_ROOT / "src"


class QualityGateError(Exception):
    """Raised when one or more quality-gate steps fail."""


def run_command(command: list[str]) -> None:
    """Runs a quality-gate command from the repository root.

    Args:
        command: Command and arguments to execute.

    Raises:
        QualityGateError: Raised when the command exits unsuccessfully.
    """

    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(SOURCE_ROOT)
    result = subprocess.run(command, cwd=REPO_ROOT, check=False, env=environment)
    if result.returncode != 0:
        formatted_command = " ".join(command)
        raise QualityGateError(f"Command failed: {formatted_command}")


def compile_source() -> None:
    """Compiles Python source files to catch syntax errors.

    Raises:
        QualityGateError: Raised when source compilation fails.
    """

    if not compileall.compile_dir(SOURCE_ROOT, quiet=1):
        raise QualityGateError("Source compilation failed.")


def main() -> None:
    """Runs all local verification for the repository."""

    compile_source()
    run_command([sys.executable, "scripts/harness_doctor.py"])
    run_command([sys.executable, "-m", "unittest", "discover", "-s", "tests"])
    print("Quality gate: ok")


if __name__ == "__main__":
    main()
