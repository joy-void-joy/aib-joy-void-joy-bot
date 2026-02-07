"""Tests for the auto_allow_edits PreToolUse hook."""

import sys
from pathlib import Path

_scripts_dir = str(
    Path(__file__).resolve().parents[2]
    / ".claude"
    / "plugins"
    / "aib"
    / "hooks"
    / "scripts"
)
sys.path.insert(0, _scripts_dir)

from auto_allow_edits import (  # noqa: E402
    EditInput,
    _allow_decision,
    _classify_trivial,
    count_real_additions,
    decide,
    is_protected_file,
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


# --- _classify_trivial ---


class TestClassifyTrivial:
    def test_blank_and_comments(self) -> None:
        lines = ["", "   ", "# comment", "    # indented"]
        assert _classify_trivial(lines) == [True, True, True, True]

    def test_imports(self) -> None:
        lines = ["import os", "from pathlib import Path"]
        assert _classify_trivial(lines) == [True, True]

    def test_pass(self) -> None:
        assert _classify_trivial(["    pass"]) == [True]

    def test_real_code(self) -> None:
        lines = ["x = 1", "return result", "def foo():"]
        assert _classify_trivial(lines) == [False, False, False]

    def test_single_line_docstring(self) -> None:
        assert _classify_trivial(['"""A docstring."""']) == [True]

    def test_multi_line_docstring(self) -> None:
        lines = ['"""', "This is content.", "More content.", '"""']
        assert _classify_trivial(lines) == [True, True, True, True]

    def test_single_quote_docstring(self) -> None:
        lines = ["'''", "content", "'''"]
        assert _classify_trivial(lines) == [True, True, True]

    def test_code_around_docstring(self) -> None:
        lines = ["x = 1", '"""', "docstring body", '"""', "y = 2"]
        result = _classify_trivial(lines)
        assert result == [False, True, True, True, False]

    def test_typed_dict_block(self) -> None:
        lines = [
            "class Foo(TypedDict):",
            "    name: str",
            "    age: int",
        ]
        assert _classify_trivial(lines) == [True, True, True]

    def test_base_model_block(self) -> None:
        lines = [
            "class Config(BaseModel):",
            "    host: str",
            "    port: int",
        ]
        assert _classify_trivial(lines) == [True, True, True]

    def test_type_def_ends_on_dedent(self) -> None:
        lines = [
            "class Foo(TypedDict):",
            "    name: str",
            "",
            "x = 1",
        ]
        result = _classify_trivial(lines)
        assert result == [True, True, True, False]

    def test_consecutive_type_defs(self) -> None:
        lines = [
            "class A(TypedDict):",
            "    x: int",
            "",
            "class B(BaseModel):",
            "    y: str",
        ]
        assert _classify_trivial(lines) == [True, True, True, True, True]

    def test_regular_class_not_trivial(self) -> None:
        lines = [
            "class Foo:",
            "    def method(self):",
            "        pass",
        ]
        result = _classify_trivial(lines)
        assert result == [False, False, True]

    def test_mixed_context(self) -> None:
        lines = [
            "import os",
            "class Cfg(BaseModel):",
            "    x: int",
            "def run():",
            '    """Do stuff."""',
            "    return 42",
        ]
        result = _classify_trivial(lines)
        assert result == [True, True, True, False, True, False]


# --- count_real_additions ---


class TestCountRealAdditions:
    def test_identical(self) -> None:
        assert count_real_additions("x = 1", "x = 1") == 0

    def test_single_real_addition(self) -> None:
        assert count_real_additions("x = 1", "x = 2") == 1

    def test_trivial_only(self) -> None:
        assert count_real_additions("", "import os\nimport sys") == 0

    def test_mixed_trivial_and_real(self) -> None:
        old = "x = 1"
        new = "import os\nx = 2\n# comment"
        assert count_real_additions(old, new) == 1

    def test_multi_line_docstring_is_trivial(self) -> None:
        old = "x = 1"
        new = 'x = 1\n"""\nThis is a docstring.\nWith multiple lines.\n"""'
        assert count_real_additions(old, new) == 0

    def test_many_real_additions(self) -> None:
        old = "a = 1\nb = 2\nc = 3\nd = 4"
        new = "a = 10\nb = 20\nc = 30\nd = 40"
        assert count_real_additions(old, new) == 4

    def test_pure_removal_is_zero(self) -> None:
        old = "a = 1\nb = 2\nc = 3"
        new = "a = 1"
        assert count_real_additions(old, new) == 0

    def test_typed_dict_addition_is_zero(self) -> None:
        old = ""
        new = "class Foo(TypedDict):\n    name: str\n    age: int"
        assert count_real_additions(old, new) == 0

    def test_addition_with_removal_only_counts_adds(self) -> None:
        old = "x = 1\ny = 2\nz = 3"
        new = "x = 1\nw = 99"
        assert count_real_additions(old, new) == 1


# --- decide ---


class TestDecide:
    def test_protected_file_defers(self) -> None:
        inp = EditInput(file_path=".claude/settings.json", old_string="x", new_string="y")
        assert decide(inp) is None

    def test_pure_deletion_allows(self) -> None:
        inp = EditInput(file_path="foo.py", old_string="x = 1", new_string="")
        assert decide(inp) == ALLOW

    def test_replace_all_single_line_allows(self) -> None:
        inp = EditInput(
            file_path="foo.py",
            old_string="old_name",
            new_string="new_name",
            replace_all=True,
        )
        assert decide(inp) == ALLOW

    def test_replace_all_multi_line_defers(self) -> None:
        inp = EditInput(
            file_path="foo.py",
            old_string="line1\nline2",
            new_string="new1\nnew2",
            replace_all=True,
        )
        assert decide(inp) is None

    def test_small_edit_allows(self) -> None:
        inp = EditInput(file_path="foo.py", old_string="x = 1", new_string="x = 2")
        assert decide(inp) == ALLOW

    def test_large_edit_defers(self) -> None:
        old = "a = 1\nb = 2\nc = 3\nd = 4"
        new = "a = 10\nb = 20\nc = 30\nd = 40"
        inp = EditInput(file_path="foo.py", old_string=old, new_string=new)
        assert decide(inp) is None

    def test_import_only_edit_allows(self) -> None:
        old = "import os"
        new = "import os\nimport sys\nfrom pathlib import Path"
        inp = EditInput(file_path="foo.py", old_string=old, new_string=new)
        assert decide(inp) == ALLOW

    def test_typed_dict_allows(self) -> None:
        new = "class Foo(TypedDict):\n    name: str"
        inp = EditInput(file_path="foo.py", old_string="", new_string=new)
        assert decide(inp) == ALLOW

    def test_empty_input_allows(self) -> None:
        inp = EditInput()
        result = decide(inp)
        assert result == ALLOW
