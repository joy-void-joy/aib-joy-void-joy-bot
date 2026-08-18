"""What only this project adds to the `dev` tree the library already builds.

The workflow commands — worktrees, branches, PRs, the quality gate, the note
and issue passes — are the library's, wired over :func:`declared`. What is
added here is the one moment lup's own guards do not cover: this repository
keeps its hooks tracked in `.githooks/` and arms them by pointing
`core.hooksPath` at that directory, where `dev git-hooks` installs hook
*bodies* lup wrote. Both are needed and neither is the other.

A project that replaced `dev` to add one command would be restating every
argument the library's tree takes, which is the drift composing removes.
"""

from pathlib import Path

import sh
import typer

import lup.devtools.dev.check as check
from lup.devtools.dev.app import DevDeclarations

import aib.devtools.harness.catalog as catalog

HOOKS_PATH = ".githooks"


def declared() -> DevDeclarations:
    """What this repository tells the dev tree, read where a command runs.

    No `GitGuard`, because this repository does not install its hooks that
    way: they are tracked in `.githooks/` and armed by pointing
    `core.hooksPath` there, so one setting arms every clone instead of each
    one remembering an install command. Left unstated, the field defaults to
    the pair lup writes, and the declaration said this repository armed two
    hooks it does not have while `dev git-hooks` read the two it does have as
    foreign.

    # lup: defer: express the three moments as GitGuard declarations and let
    # lup write them, once its guard vocabulary has a word for refusing a
    # commit that mixes data with code — the tracked hooks are the honest
    # interim, not the end state
    """
    return DevDeclarations(
        project=catalog.dev_project(),
        hooks=catalog.declared_hook_set(),
        plugin=catalog.declared_plugin(),
        test_roots=[check.TestRoot(name="pytest", directory=Path.cwd())],
        git_guards=[],
    )


def install_hooks() -> bool:
    """Point git at the tracked hooks directory. Returns True if it changed."""
    git = sh.Command("git")
    current = str(git.config("--get", "core.hooksPath", _ok_code=[0, 1])).strip()
    if current == HOOKS_PATH:
        return False
    git.config("core.hooksPath", HOOKS_PATH)
    return True


def extend(app: typer.Typer) -> None:
    """Mount this project's own commands onto the inherited `dev` app."""

    @app.command("setup-hooks")
    def setup_hooks_cmd() -> None:
        """Install the tracked git hooks (core.hooksPath -> .githooks)."""
        if install_hooks():
            typer.echo(f"Installed git hooks: core.hooksPath -> {HOOKS_PATH}")
        else:
            typer.echo(f"Git hooks already installed (core.hooksPath -> {HOOKS_PATH})")
