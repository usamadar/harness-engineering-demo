"""Runs the repository unit test feedback check."""

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPO_ROOT / "src"


class UnitTestCheckError(Exception):
    """Raised when the unit test feedback check fails."""


def run_unit_tests() -> None:
    """Runs the unit test suite.

    Raises:
        UnitTestCheckError: Raised when the test command exits unsuccessfully.
    """

    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(SOURCE_ROOT)
    result = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        cwd=REPO_ROOT,
        check=False,
        env=environment,
    )
    if result.returncode != 0:
        raise UnitTestCheckError("Unit tests failed.")


def main() -> None:
    """Runs the unit test check."""

    run_unit_tests()
    print("Unit tests: ok")


if __name__ == "__main__":
    main()
