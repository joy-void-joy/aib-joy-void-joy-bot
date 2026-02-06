#!/usr/bin/env python3
"""PreToolUse hook that auto-allows small, safe Edit operations.

Decision order:
1. Protected files (.claude/, pyproject.toml, .env*) → always defer
2. Pure deletion (new_string is empty) → allow
3. TypedDict/BaseModel class definition → allow
4. replace_all: single-line rename → allow, multi-line → defer
5. Count "real" changed lines (ignoring imports, comments, whitespace,
   docstrings, blank lines) → allow if ≤ MAX_REAL_CHANGES
"""

import difflib
import json
import re
import sys

MAX_REAL_CHANGES = 3

PROTECTED_PATTERNS = [
    r"(^|/)\.claude/",
    r"(^|/)pyproject\.toml$",
    r"(^|/)\.env($|\.)",
]


def is_protected_file(file_path: str) -> bool:
    return any(re.search(p, file_path) for p in PROTECTED_PATTERNS)


def is_trivial_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    if s.startswith("#"):
        return True
    if s in ('"""', "'''") or s.startswith('"""') or s.startswith("'''"):
        return True
    if s.startswith("import ") or s.startswith("from "):
        return True
    if s == "pass":
        return True
    return False


def is_type_definition_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    if re.match(r"class\s+\w+\s*\(.*(?:TypedDict|BaseModel).*\)\s*:", s):
        return True
    if s.startswith("#") or s.startswith('"""') or s.startswith("'''"):
        return True
    if s in ('"""', "'''", "pass"):
        return True
    if s.startswith("@"):
        return True
    if re.match(r"\w+\s*:", s):
        return True
    return False


def is_type_definition_block(text: str) -> bool:
    if not text or not text.strip():
        return False
    lines = [ln for ln in text.splitlines() if ln.strip()]
    has_class = any(
        re.match(r"\s*class\s+\w+\s*\(.*(?:TypedDict|BaseModel).*\)\s*:", ln)
        for ln in lines
    )
    if not has_class:
        return False
    return all(is_type_definition_line(ln) for ln in lines)


def strip_docstrings(lines: list[str]) -> list[str]:
    result: list[str] = []
    in_docstring = False
    delimiter = ""
    for line in lines:
        stripped = line.strip()
        if in_docstring:
            result.append("")
            if delimiter in stripped:
                in_docstring = False
            continue
        for delim in ('"""', "'''"):
            if delim in stripped:
                count = stripped.count(delim)
                if count == 1:
                    in_docstring = True
                    delimiter = delim
                    result.append("")
                    break
        else:
            result.append(line)
    return result


def count_real_changes(old_string: str, new_string: str) -> int:
    old_lines = strip_docstrings(old_string.splitlines()) if old_string else []
    new_lines = strip_docstrings(new_string.splitlines()) if new_string else []

    matcher = difflib.SequenceMatcher(
        None,
        [ln.strip() for ln in old_lines],
        [ln.strip() for ln in new_lines],
    )

    real = 0
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            continue
        removed_real = sum(
            1 for i in range(i1, i2) if not is_trivial_line(old_lines[i])
        )
        added_real = sum(1 for j in range(j1, j2) if not is_trivial_line(new_lines[j]))
        real += max(removed_real, added_real)

    return real


AllowDecision = dict[str, dict[str, str]]


def _allow_decision() -> AllowDecision:
    return {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "allow",
            "permissionDecisionReason": "Auto-allowed: safe edit pattern detected",
        }
    }


def decide(tool_input: dict[str, object]) -> AllowDecision | None:
    file_path = str(tool_input.get("file_path", ""))
    old_string = str(tool_input.get("old_string", ""))
    new_string = str(tool_input.get("new_string", ""))
    replace_all = bool(tool_input.get("replace_all", False))

    if is_protected_file(file_path):
        return None

    if old_string and not new_string:
        return _allow_decision()

    if is_type_definition_block(new_string):
        return _allow_decision()

    if replace_all:
        old_n = len(old_string.splitlines()) if old_string else 0
        new_n = len(new_string.splitlines()) if new_string else 0
        if old_n <= 1 and new_n <= 1:
            return _allow_decision()
        return None

    if count_real_changes(old_string, new_string) <= MAX_REAL_CHANGES:
        return _allow_decision()

    return None


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        sys.exit(0)

    if data.get("tool_name") != "Edit":
        sys.exit(0)

    result = decide(data.get("tool_input", {}))
    if result:
        json.dump(result, sys.stdout)


if __name__ == "__main__":
    main()
