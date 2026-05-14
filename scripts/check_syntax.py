"""Checks that Python source files compile successfully."""

import compileall
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPO_ROOT / "src"
SCRIPT_ROOT = REPO_ROOT / "scripts"
TEST_ROOT = REPO_ROOT / "tests"
COMPILE_PATHS = (SOURCE_ROOT, SCRIPT_ROOT, TEST_ROOT)


class SyntaxCheckError(Exception):
    """Raised when Python compilation fails."""


def compile_python_paths() -> None:
    """Compiles repository Python paths.

    Raises:
        SyntaxCheckError: Raised when any Python file fails to compile.
    """

    for path in COMPILE_PATHS:
        if not compileall.compile_dir(path, quiet=1):
            relative_path = path.relative_to(REPO_ROOT)
            raise SyntaxCheckError(f"Python syntax check failed in {relative_path}.")


def main() -> None:
    """Runs the syntax check."""

    compile_python_paths()
    print("Syntax check: ok")


if __name__ == "__main__":
    main()
