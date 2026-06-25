#!/usr/bin/env python3
"""Public-readiness checks for the Hypergravity Habitat repository.

The script checks Markdown files for issues that make the repository harder to
review publicly:

- unfinished formula markup,
- explicit unverified-source markers,
- known stale internal paths,
- optional missing project footers.

Use --fix-footers to add the standard footer to Markdown files. Use
--require-footers to fail when a Markdown file has no footer.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

RAW_FORMULA_PATTERNS = (
    "\\[",
    "\\]",
    "\\(",
    "\\)",
)

# Keep these markers deliberately specific. Broad phrases such as "to verify"
# can appear in normal prose, for example "programme to verify the research gap".
UNVERIFIED_PATTERNS = (
    "DOI to verify",
    "metadata to verify",
    "reference to verify",
    "citation to verify",
)

STALE_PATHS = {
    "docs/physics.md": "docs/physics-reference.md",
    "docs/design-requirements.md": "docs/engineering/design-requirements.md",
}
FOOTER_MARKER = "<!-- project-footer -->"


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        if path.name.startswith("."):
            continue
        yield path


def footer_for(path: Path, root: Path) -> str:
    rel = path.relative_to(root)
    depth = len(rel.parts) - 1
    readme = "README.md" if depth <= 0 else "/".join([".."] * depth + ["README.md"])
    return (
        "\n---\n\n"
        f"{FOOTER_MARKER}\n"
        f"**Project:** [Hypergravity Habitat]({readme}) · "
        "**Status:** exploratory research documentation · "
        "**License:** see repository license and file-level notes\n"
    )


def check_file(path: Path, root: Path, require_footers: bool) -> list[str]:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(root)
    issues: list[str] = []

    for pattern in RAW_FORMULA_PATTERNS:
        if pattern in text:
            issues.append(f"unfinished formula markup `{pattern}`")

    for pattern in UNVERIFIED_PATTERNS:
        if pattern in text:
            issues.append(f"unverified marker `{pattern}`")

    for stale, replacement in STALE_PATHS.items():
        if stale in text:
            issues.append(f"stale path `{stale}`; use `{replacement}`")

    if require_footers and FOOTER_MARKER not in text:
        issues.append("missing project footer")

    return [f"{rel}: {issue}" for issue in issues]


def fix_footer(path: Path, root: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if FOOTER_MARKER in text:
        return False
    path.write_text(text.rstrip() + footer_for(path, root), encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Check public-release readiness of Markdown docs.")
    parser.add_argument("root", nargs="?", default=".", help="Repository root; default: current directory")
    parser.add_argument("--fix-footers", action="store_true", help="Add missing standard project footers")
    parser.add_argument("--require-footers", action="store_true", help="Fail when Markdown files lack project footers")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.exists():
        raise SystemExit(f"Root does not exist: {root}")

    changed = 0
    all_issues: list[str] = []

    for path in iter_markdown_files(root):
        if args.fix_footers:
            if fix_footer(path, root):
                changed += 1
        all_issues.extend(check_file(path, root, require_footers=args.require_footers))

    if changed:
        print(f"Added project footer to {changed} Markdown file(s).")

    if all_issues:
        print("Public-readiness issues:")
        for issue in all_issues:
            print(f"- {issue}")
        return 1

    print("No public-readiness issues found by this script.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
