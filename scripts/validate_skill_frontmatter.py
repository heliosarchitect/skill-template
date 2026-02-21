#!/usr/bin/env python3
"""Minimal SKILL.md frontmatter validator for CI."""

from __future__ import annotations

import pathlib
import re
import sys

REQUIRED_KEYS = ("name", "description")


def fail(msg: str) -> None:
    print(f"ERROR: {msg}")
    sys.exit(1)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: validate_skill_frontmatter.py <SKILL.md>")

    path = pathlib.Path(sys.argv[1])
    if not path.exists():
        fail(f"file not found: {path}")

    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not m:
        fail("missing YAML frontmatter block")

    frontmatter = m.group(1)

    for key in REQUIRED_KEYS:
        if not re.search(rf"^{re.escape(key)}\s*:\s*.+$", frontmatter, flags=re.MULTILINE):
            fail(f"required key missing or empty: {key}")

    print("frontmatter validation passed")


if __name__ == "__main__":
    main()
