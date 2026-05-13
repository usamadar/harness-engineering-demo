"""Runs dependency-free lint checks for the demo repository."""

from __future__ import annotations

import ast
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PYTHON_PATHS = (
    REPO_ROOT / "scripts",
    REPO_ROOT / "src",
    REPO_ROOT / "tests",
)
TEXT_SUFFIXES = {".md", ".py", ".toml", ".yml", ".yaml"}
MAX_LINE_LENGTH = 100
BUSINESS_RULE_TERMS = (
    "password",
    "credential",
    "permission",
    "suspicious access",
    "production",
    "outage",
    "cannot log in",
    "error",
    "downtime",
    "invoice",
    "payment",
    "refund",
    "subscription",
)
CLI_PATH = REPO_ROOT / "src/harness_demo/cli.py"
ROUTER_PATH = REPO_ROOT / "src/harness_demo/router.py"


@dataclass(frozen=True)
class LintViolation:
    """Represents a lint violation discovered by the repository linter.

    Args:
        path: File path containing the violation.
        line_number: One-based line number when the violation is line-specific.
        message: Human-readable lint violation.
    """

    path: Path
    line_number: int | None
    message: str

    def format(self) -> str:
        """Formats the violation for terminal output.

        Returns:
            Readable file, line, and message text.
        """

        relative_path = self.path.relative_to(REPO_ROOT)
        if self.line_number is None:
            return f"{relative_path}: {self.message}"

        return f"{relative_path}:{self.line_number}: {self.message}"


class LintError(Exception):
    """Raised when lint violations are found."""


def iter_text_files() -> list[Path]:
    """Finds text files that should follow repository formatting rules.

    Returns:
        Sorted text file paths, excluding Git internals.
    """

    paths = [
        path
        for path in REPO_ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.suffix in TEXT_SUFFIXES
    ]
    return sorted(paths)


def iter_python_files() -> list[Path]:
    """Finds Python files that should follow Python-specific lint rules.

    Returns:
        Sorted Python file paths from application, scripts, and tests.
    """

    paths = []
    for python_path in PYTHON_PATHS:
        paths.extend(python_path.rglob("*.py"))

    return sorted(paths)


def check_text_formatting() -> list[LintViolation]:
    """Checks repository text formatting rules.

    Returns:
        Lint violations for line length, tabs, trailing whitespace, and missing
        final newlines.
    """

    violations = []
    for path in iter_text_files():
        content = path.read_text(encoding="utf-8")
        if content and not content.endswith("\n"):
            violations.append(LintViolation(path, None, "missing final newline"))

        for line_number, line in enumerate(content.splitlines(), start=1):
            if "\t" in line:
                violations.append(LintViolation(path, line_number, "contains tab"))
            if line.rstrip() != line:
                violations.append(
                    LintViolation(path, line_number, "contains trailing whitespace")
                )
            if len(line) > MAX_LINE_LENGTH:
                violations.append(
                    LintViolation(
                        path,
                        line_number,
                        f"line is longer than {MAX_LINE_LENGTH} characters",
                    )
                )

    return violations


def check_python_docstrings() -> list[LintViolation]:
    """Checks that Python modules, classes, and functions have docstrings.

    Returns:
        Lint violations for missing docstrings.
    """

    violations = []
    for path in iter_python_files():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        if ast.get_docstring(tree) is None:
            violations.append(LintViolation(path, 1, "missing module docstring"))

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and ast.get_docstring(node) is None:
                violations.append(
                    LintViolation(path, node.lineno, "missing class docstring")
                )
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if should_require_function_docstring(path, node):
                    violations.append(
                        LintViolation(path, node.lineno, "missing function docstring")
                    )

    return violations


def should_require_function_docstring(
    path: Path,
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> bool:
    """Checks whether a function should have a docstring.

    Args:
        path: Python file containing the function.
        node: Function node parsed from the Python file.

    Returns:
        True when the function is expected to have a docstring.
    """

    if ast.get_docstring(node) is not None:
        return False
    if path.parts[-2] == "tests":
        return False
    if node.name.startswith("__") and node.name.endswith("__"):
        return False

    return True


def check_cli_has_no_business_rules() -> list[LintViolation]:
    """Checks that routing keywords do not drift into the CLI adapter.

    Returns:
        Lint violations for business-rule terms found in `cli.py`.
    """

    cli_content = CLI_PATH.read_text(encoding="utf-8").casefold()
    violations = []
    for term in BUSINESS_RULE_TERMS:
        if term in cli_content:
            violations.append(
                LintViolation(
                    CLI_PATH,
                    None,
                    f"business-rule term belongs in {ROUTER_PATH.name}: {term}",
                )
            )

    return violations


def find_violations() -> list[LintViolation]:
    """Finds all repository lint violations.

    Returns:
        Lint violations discovered by every lint rule.
    """

    violations = []
    violations.extend(check_text_formatting())
    violations.extend(check_python_docstrings())
    violations.extend(check_cli_has_no_business_rules())
    return violations


def main() -> None:
    """Runs the repository linter.

    Raises:
        LintError: Raised when lint violations are found.
    """

    violations = find_violations()
    if violations:
        formatted_violations = "\n".join(
            violation.format() for violation in violations
        )
        raise LintError(f"Lint violations found:\n{formatted_violations}")

    print("Lint: ok")


if __name__ == "__main__":
    main()
