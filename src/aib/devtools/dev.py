"""What only this project adds to the `dev` tree the library already builds.

The workflow commands — worktrees, branches, PRs, the quality gate, the note
and issue passes — are the library's, wired over :func:`declared`. What is
added here is what the library's own guards do not cover, and all of it comes
from one fact about this repository: forecast data and code share a checkout
and reach `main` by different routes.

The hooks stay tracked in `.githooks/`, and `core.hooksPath` is what points
git at them — so one setting arms every clone and every worktree cut from it,
rather than each one remembering an install command. `dev git-hooks install`
writes the bodies there, because that directory is the one it asks git for.

A project that replaced `dev` to add one command would be restating every
argument the library's tree takes, which is the drift composing removes.
"""

from pathlib import Path
from typing import Annotated

import typer

import lup.devtools.dev.check as check
from lup.devtools.dev.app import DevDeclarations
from lup.devtools.dev.git_guards import DELETION_STANDDOWN, GitGuard
from lup.devtools.utils import git

import aib.devtools.guards as guards
import aib.devtools.harness.catalog as catalog
import aib.devtools.library as library

HOOKS_PATH = ".githooks"
"""Where this repository tracks the hooks git runs, named to `core.hooksPath`."""

SPLIT_COMMAND = "uv run lup-devtools dev data-split"
"""What the commit hook runs to refuse a commit belonging to neither route."""

BASE_COMMAND = "uv run lup-devtools dev pr-base"
"""What the push hook runs to refuse a request built on an unpublished main."""

GATE_COMMAND = "uv run lup-devtools dev gate"
"""What the push hook runs to hold a branch to this repository's bar."""

LIBRARY_HELP = "How this repository obtains lup, and how to change it"
"""What the `library` group answers, as the command tree lists it."""

DryRun = Annotated[
    bool,
    typer.Option("--dry-run", "-n", help="Show what would change, and change none"),
]
"""The flag every writing command here takes, spelled once.

A plain alias rather than a `type` statement: typer resolves the annotation at
decoration time and a PEP 695 alias reaches it as a name it cannot unwrap.
"""


def library_app() -> typer.Typer:
    """The `dev library` group: read the acquisition mode, or declare another.

    Built here rather than declared beside the module it drives, so the CLI
    surface stays in the file that mounts it and `library.py` stays a reader
    and writer of `pyproject.toml` that a test can call without a command line.
    """
    app = typer.Typer(help=LIBRARY_HELP, no_args_is_help=True)

    @app.command("status")
    def status_cmd() -> None:
        """Report where lup is resolved from, and what upgrading it takes."""
        library.library_status()

    @app.command("release")
    def release_cmd() -> None:
        """Ask the package index whether a release of lup is published yet."""
        library.library_release()

    @app.command("use")
    def use_cmd(
        mode: Annotated[library.LibraryMode, typer.Argument()],
        version: Annotated[str | None, typer.Option("--version")] = None,
        dry_run: DryRun = False,
    ) -> None:
        """Resolve lup as `published`, and pin the lower bound it needs."""
        library.use_library(mode, version, dry_run)

    @app.command("git")
    def git_cmd(
        url: Annotated[str, typer.Option("--url")] = library.REPOSITORY_URL,
        branch: Annotated[str | None, typer.Option("--branch")] = None,
        tag: Annotated[str | None, typer.Option("--tag")] = None,
        rev: Annotated[str | None, typer.Option("--rev")] = None,
        dry_run: DryRun = False,
    ) -> None:
        """Resolve lup from its repository, at one branch, tag, or commit."""
        library.git_library(
            library.git_source(url, branch=branch, tag=tag, rev=rev), dry_run
        )

    @app.command("link")
    def link_cmd(
        checkout: Annotated[Path, typer.Argument()],
        dry_run: DryRun = False,
    ) -> None:
        """Resolve lup from a checkout on this disk, editable.

        Takes the repository root rather than the package inside it, because
        that is the path somebody has in hand — `packages/lup` is lup's own
        layout and this appends it.
        """
        library.link_library(checkout, dry_run)

    return app


def declared() -> DevDeclarations:
    """What this repository tells the dev tree, read where a command runs.

    Four guards over two moments. The library's drift check and this
    repository's data/code split both belong at the commit; the stale-base
    check and the gate both belong at the push. Declaration order is running
    order, so each moment spends its nearly-free refusal first — which at the
    push is the difference between a wrong-base branch being told in a second
    and being told once the whole suite has run.

    The stale-base check and the gate's standdown both read git's pre-push
    ref list, and git delivers it once, so both say they read it and the
    composed hook hands each the same copy.
    """
    return DevDeclarations(
        project=catalog.dev_project(),
        hooks=catalog.declared_hook_set(),
        plugin=catalog.declared_plugin(),
        test_roots=[check.TestRoot(name="pytest", directory=Path.cwd())],
        git_guards=[
            GitGuard(),
            GitGuard(
                command=SPLIT_COMMAND,
                refusal=(
                    "Refuses a commit mixing forecast data with code. Data lands\n"
                    "# on main; code goes through a worktree and a PR."
                ),
            ),
            GitGuard(
                command=BASE_COMMAND,
                hook="pre-push",
                reads_stdin=True,
                refusal=(
                    "Refuses a branch whose PR would carry forecast data, which\n"
                    "# is what an unpublished main does. Publish main first."
                ),
            ),
            GitGuard(
                command=GATE_COMMAND,
                hook="pre-push",
                standdown=DELETION_STANDDOWN,
                reads_stdin=True,
                refusal=(
                    "Refuses this push while the gate fails. A commit is local\n"
                    f"# and rewritable; a push is neither. Run `{GATE_COMMAND}`."
                ),
            ),
        ],
    )


def install_hooks() -> bool:
    """Point git at the tracked hooks directory. Returns True if it changed."""
    current = git.out("config", "--get", "core.hooksPath", _ok_code=[0, 1])
    if current == HOOKS_PATH:
        return False
    git("config", "core.hooksPath", HOOKS_PATH)
    return True


def extend(app: typer.Typer) -> None:
    """Mount this project's own commands onto the inherited `dev` app."""

    @app.command("setup-hooks")
    def setup_hooks_cmd() -> None:
        """Point git at the tracked hooks (core.hooksPath -> .githooks).

        A different job from `dev git-hooks install`, which writes the bodies:
        this says where git looks, and the bodies are tracked, so a clone that
        runs this is armed by what it has already checked out.
        """
        if install_hooks():
            typer.echo(f"Installed git hooks: core.hooksPath -> {HOOKS_PATH}")
        else:
            typer.echo(f"Git hooks already installed (core.hooksPath -> {HOOKS_PATH})")

    @app.command("data-split")
    def data_split_cmd() -> None:
        """Refuse a commit carrying both forecast data and code."""
        guards.refuse_mixed_commit()

    @app.command("pr-base")
    def pr_base_cmd() -> None:
        """Refuse a push whose PR would carry data an unpublished main holds.

        Reads git's pre-push ref list on stdin, so running this by hand
        outside the hook judges an empty push and passes. That is the honest
        answer: which refs are being uploaded is a thing only the moment knows.
        """
        guards.refuse_stale_base(typer.get_text_stream("stdin").read())

    @app.command("gate")
    def gate_cmd() -> None:
        """Run the checks this repository holds a branch to before it leaves."""
        guards.run_gate()

    app.add_typer(library_app(), name="library", help=LIBRARY_HELP)
