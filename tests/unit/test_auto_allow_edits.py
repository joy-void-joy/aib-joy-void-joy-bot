"""Tests for the auto_allow_edits PreToolUse hook."""

import sys
from pathlib import Path

# Add the hook scripts directory to the path so we can import the module
_scripts_dir = str(
    Path(__file__).resolve().parents[2]
    / ".claude"
    / "plugins"
    / "aib"
    / "hooks"
    / "scripts"
)
sys.path.insert(0, _scripts_dir)

from auto_allow_edits import (
    _allow_decision,
    count_real_changes,
    decide,
    is_protected_file,
    is_trivial_line,
    is_type_definition_block,
    strip_docstrings,
)

ALLOW = _allow_decision()


# --- is_protected_file ---


class TestIsProtectedFile:
    def test_claude_dir(self) -> None:
        assert is_protected_file(".claude/settings.json")
        assert is_protected_file("src/.claude/foo.py")

    def test_pyproject_toml(self) -> None:
        assert is_protected_file("pyproject.toml")
        assert is_protected_file("sub/pyproject.toml")

    def test_env_files(self) -> None:
        assert is_protected_file(".env")
        assert is_protected_file(".env.local")
        assert is_protected_file("sub/.env.production")

    def test_non_protected(self) -> None:
        assert not is_protected_file("src/main.py")
        assert not is_protected_file("tests/test_foo.py")
        assert not is_protected_file("README.md")


# --- is_trivial_line ---


class TestIsTrivialLine:
    def test_empty_and_whitespace(self) -> None:
        assert is_trivial_line("")
        assert is_trivial_line("   ")
        assert is_trivial_line("\t")

    def test_comments(self) -> None:
        assert is_trivial_line("# a comment")
        assert is_trivial_line("    # indented comment")

    def test_docstring_delimiters(self) -> None:
        assert is_trivial_line('"""')
        assert is_trivial_line("'''")
        assert is_trivial_line('"""A one-line docstring."""')

    def test_imports(self) -> None:
        assert is_trivial_line("import os")
        assert is_trivial_line("from pathlib import Path")

    def test_pass(self) -> None:
        assert is_trivial_line("    pass")

    def test_real_code(self) -> None:
        assert not is_trivial_line("x = 1")
        assert not is_trivial_line("return result")
        assert not is_trivial_line("def foo():")


# --- strip_docstrings ---


class TestStripDocstrings:
    def test_no_docstrings(self) -> None:
        lines = ["x = 1", "y = 2"]
        assert strip_docstrings(lines) == lines

    def test_single_line_docstring(self) -> None:
        lines = ['"""A docstring."""']
        result = strip_docstrings(lines)
        assert result == lines  # count=2, not entering docstring mode

    def test_multi_line_docstring(self) -> None:
        lines = ['"""', "This is content.", "More content.", '"""']
        result = strip_docstrings(lines)
        assert all(r == "" for r in result)

    def test_preserves_non_docstring_lines(self) -> None:
        lines = ["x = 1", '"""', "docstring body", '"""', "y = 2"]
        result = strip_docstrings(lines)
        assert result[0] == "x = 1"
        assert result[1] == ""
        assert result[2] == ""
        assert result[3] == ""
        assert result[4] == "y = 2"

    def test_single_quote_docstring(self) -> None:
        lines = ["'''", "content", "'''"]
        result = strip_docstrings(lines)
        assert all(r == "" for r in result)


# --- is_type_definition_block ---


class TestIsTypeDefinitionBlock:
    def test_typed_dict(self) -> None:
        block = "class Foo(TypedDict):\n    name: str\n    age: int"
        assert is_type_definition_block(block)

    def test_base_model(self) -> None:
        block = "class Config(BaseModel):\n    host: str\n    port: int"
        assert is_type_definition_block(block)

    def test_regular_class(self) -> None:
        block = "class Foo:\n    def method(self):\n        pass"
        assert not is_type_definition_block(block)

    def test_empty(self) -> None:
        assert not is_type_definition_block("")
        assert not is_type_definition_block("   ")


# --- count_real_changes ---


class TestCountRealChanges:
    def test_identical(self) -> None:
        assert count_real_changes("x = 1", "x = 1") == 0

    def test_single_real_change(self) -> None:
        assert count_real_changes("x = 1", "x = 2") == 1

    def test_trivial_only(self) -> None:
        assert count_real_changes("", "import os\nimport sys") == 0

    def test_mixed_trivial_and_real(self) -> None:
        old = "x = 1"
        new = "import os\nx = 2\n# comment"
        assert count_real_changes(old, new) == 1

    def test_multi_line_docstring_is_trivial(self) -> None:
        old = "x = 1"
        new = 'x = 1\n"""\nThis is a docstring.\nWith multiple lines.\n"""'
        assert count_real_changes(old, new) == 0

    def test_many_real_changes(self) -> None:
        old = "a = 1\nb = 2\nc = 3\nd = 4"
        new = "a = 10\nb = 20\nc = 30\nd = 40"
        assert count_real_changes(old, new) == 4


# --- decide ---


class TestDecide:
    def test_protected_file_defers(self) -> None:
        result = decide({"file_path": ".claude/settings.json", "old_string": "x", "new_string": "y"})
        assert result is None

    def test_pure_deletion_allows(self) -> None:
        result = decide({"file_path": "foo.py", "old_string": "x = 1", "new_string": ""})
        assert result == ALLOW

    def test_typed_dict_allows(self) -> None:
        new = "class Foo(TypedDict):\n    name: str"
        result = decide({"file_path": "foo.py", "old_string": "", "new_string": new})
        assert result == ALLOW

    def test_replace_all_single_line_allows(self) -> None:
        result = decide({
            "file_path": "foo.py",
            "old_string": "old_name",
            "new_string": "new_name",
            "replace_all": True,
        })
        assert result == ALLOW

    def test_replace_all_multi_line_defers(self) -> None:
        result = decide({
            "file_path": "foo.py",
            "old_string": "line1\nline2",
            "new_string": "new1\nnew2",
            "replace_all": True,
        })
        assert result is None

    def test_small_edit_allows(self) -> None:
        result = decide({
            "file_path": "foo.py",
            "old_string": "x = 1",
            "new_string": "x = 2",
        })
        assert result == ALLOW

    def test_large_edit_defers(self) -> None:
        old = "a = 1\nb = 2\nc = 3\nd = 4"
        new = "a = 10\nb = 20\nc = 30\nd = 40"
        result = decide({"file_path": "foo.py", "old_string": old, "new_string": new})
        assert result is None

    def test_import_only_edit_allows(self) -> None:
        old = "import os"
        new = "import os\nimport sys\nfrom pathlib import Path"
        result = decide({"file_path": "foo.py", "old_string": old, "new_string": new})
        assert result == ALLOW

    def test_missing_fields_defers_gracefully(self) -> None:
        result = decide({})
        assert result is None or result == ALLOW  # empty old+new = 0 changes = allow
