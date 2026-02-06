#!/usr/bin/env python3
"""PreToolUse hook that auto-allows small, safe Edit operations.

Auto-allows edits when ANY condition is met:
1. Pure deletion (new_string is empty)
2. Small edit (both old_string and new_string are ≤3 lines)
3. Import-only changes (all old lines are import/from statements)
4. Adding comments or docstrings to existing code
5. Whitespace-only changes

Always defers to user for:
- Protected files (.claude/, pyproject.toml, .env*)
- Large edits (>50 lines in either old or new string)
"""

import json
import re
import sys


def count_lines(s: str) -> int:
    if not s:
        return 0
    return len(s.splitlines())


def is_protected_file(file_path: str) -> bool:
    protected_patterns = [
        r"/.claude/",
        r"/\.claude/",
        r"pyproject\.toml$",
        r"\.env",
    ]
    return any(re.search(p, file_path) for p in protected_patterns)


def is_pure_deletion(old_string: str, new_string: str) -> bool:
    return bool(old_string) and not new_string


def is_small_edit(old_string: str, new_string: str) -> bool:
    return count_lines(old_string) <= 3 and count_lines(new_string) <= 3


def is_import_only(old_string: str) -> bool:
    if not old_string.strip():
        return False
    lines = [line.strip() for line in old_string.splitlines() if line.strip()]
    return all(line.startswith("import ") or line.startswith("from ") for line in lines)


def _is_comment_or_docstring_line(line: str) -> bool:
    s = line.strip()
    return (
        s.startswith("#")
        or s.startswith('"""')
        or s.startswith("'''")
        or s == '"""'
        or s == "'''"
        or not s
    )


def is_adding_comments_or_docstrings(old_string: str, new_string: str) -> bool:
    if not old_string or not new_string:
        return False
    old_lines = old_string.splitlines()
    new_lines = new_string.splitlines()
    if len(new_lines) < len(old_lines):
        return False

    old_stripped = [line.strip() for line in old_lines]
    j = 0
    added_lines = []
    for new_line in new_lines:
        if j < len(old_stripped) and new_line.strip() == old_stripped[j]:
            j += 1
        else:
            added_lines.append(new_line)

    if j != len(old_stripped):
        return False
    if not added_lines:
        return False
    return all(_is_comment_or_docstring_line(line) for line in added_lines)


def is_whitespace_only_change(old_string: str, new_string: str) -> bool:
    if not old_string or not new_string:
        return False
    old_stripped = re.sub(r"\s+", "", old_string)
    new_stripped = re.sub(r"\s+", "", new_string)
    return old_stripped == new_stripped


def allow() -> None:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "allow",
                "permissionDecisionReason": "Auto-allowed: safe edit pattern detected",
            }
        },
        sys.stdout,
    )
    sys.exit(0)


def passthrough() -> None:
    sys.exit(0)


def main() -> None:
    data = json.load(sys.stdin)

    tool_input = data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")
    old_string = tool_input.get("old_string", "")
    new_string = tool_input.get("new_string", "")

    if is_protected_file(file_path):
        passthrough()

    if count_lines(old_string) > 50 or count_lines(new_string) > 50:
        passthrough()

    if is_pure_deletion(old_string, new_string):
        allow()

    if is_small_edit(old_string, new_string):
        allow()

    if is_import_only(old_string):
        allow()

    if is_adding_comments_or_docstrings(old_string, new_string):
        allow()

    if is_whitespace_only_change(old_string, new_string):
        allow()

    passthrough()


if __name__ == "__main__":
    main()
