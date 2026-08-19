"""The two refusals this repository adds to the ones the library declares.

Both exist because forecast data and code live in the same checkout and reach
`main` by different routes: data is committed straight to it, code goes
through a worktree and a pull request. Everything that goes wrong here is a
consequence of that split, and both moments where it goes wrong are moments
git already stops at.

Written as commands rather than as shell inside a hook so they are reviewed,
tested, and reachable by hand — the hook is then one line naming one of them,
which is the shape the library's own guards already have.
"""

import shlex
from pathlib import Path

import sh
import typer
from pydantic import BaseModel

from lup.devtools.utils import decode_stderr, git, uv

DATA_ROOT = Path("notes")
"""Where forecast output lives, and the whole of what makes a commit data."""

ZERO_OID = "0" * 40
"""What git writes as a push's local object id where a ref is being deleted."""


class RefUpdate(BaseModel, frozen=True):
    """One ref a push would update, as git names it on the hook's stdin."""

    local_oid: str
    remote_ref: str

    @property
    def deletion(self) -> bool:
        """Whether this update removes the remote ref rather than uploading."""
        return self.local_oid == ZERO_OID


def merging() -> bool:
    """Whether this commit concludes a merge, which spans both trees.

    A merge legitimately carries data and code together: it is not authoring
    either, it is recording that two histories already holding them met.
    """
    return (Path(git.out("rev-parse", "--git-dir")) / "MERGE_HEAD").exists()


def staged() -> list[Path]:
    """Every path this commit would carry, in the states a commit can carry."""
    return [
        Path(name)
        for name in git.lines(
            "diff", "--cached", "--name-only", "--diff-filter=ACMRD", _ok_code=[0]
        )
        if name
    ]


def is_data(path: Path) -> bool:
    """Whether a path is forecast output rather than something review reads."""
    return DATA_ROOT in path.parents


def sample(paths: list[Path], limit: int = 3) -> list[str]:
    """The first few paths, then a line saying how many were not shown."""
    shown = [f"    {path}" for path in paths[:limit]]
    if len(paths) > limit:
        shown.append(f"    … and {len(paths) - limit} more")
    return shown


def pushed_refs(protocol: str) -> list[RefUpdate]:
    """Each ref this push updates, read from git's own pre-push protocol.

    Git names one update per line as `<local ref> <local oid> <remote ref>
    <remote oid>`. A line that does not parse is dropped: the question here
    is which refs carry forecast data, and a line nothing can be read out of
    names no ref to answer it about.
    """
    updates = [line.split() for line in protocol.splitlines()]
    return [
        RefUpdate(local_oid=fields[1], remote_ref=fields[2])
        for fields in updates
        if len(fields) == 4
    ]


def unpushed_main() -> int:
    """How many commits local `main` holds that `origin/main` has never seen."""
    return len(git.lines("rev-list", "origin/main..main", _ok_code=[0]))


def unpublished_data() -> list[Path]:
    """The data files local `main` holds that `origin/main` has never seen."""
    return [
        Path(name)
        for name in git.lines(
            "diff",
            "--name-only",
            "origin/main..main",
            "--",
            f"{DATA_ROOT}/",
            _ok_code=[0],
        )
        if name
    ]


def inherited_data(local_oid: str) -> list[Path]:
    """The data files this ref would carry in *because* main is unpublished.

    Two readings, and only their overlap is the hazard. What a request would
    show as added is the diff from the merge base it is computed against;
    what it would show *wrongly* is the part of that which arrived from
    commits the remote has never seen.

    Intersected rather than taking the first alone, because a branch may
    author a data file of its own — a config registry the code reads — and
    such a file sits in the diff at every moment, published main or not.
    Refusing over it names a cause that is not there, and a guard that fires
    on a cause that is not there is one people learn to pass `--no-verify`
    to, which costs the refusal that was right.

    The unpushed count alone cannot stand in for this. A forecast loop
    commits to local main continuously, so main is unpublished through most
    of a working day, and a branch carrying one authored data file would be
    refused on every push until somebody stopped the loop.
    """
    try:
        base = git.out("merge-base", local_oid, "origin/main")
    except sh.ErrorReturnCode:
        return []
    unpublished = dict.fromkeys(unpublished_data())
    return [
        path
        for name in git.lines(
            "diff", "--name-only", base, local_oid, "--", f"{DATA_ROOT}/", _ok_code=[0]
        )
        if name and (path := Path(name)) in unpublished
    ]


def refuse_mixed_commit() -> None:
    """Refuse a commit carrying both forecast data and code.

    Data lands on `main` and code goes through a worktree and a pull request,
    so a commit holding both belongs to neither route: it cannot land on
    `main` without skipping review, and it cannot open a request without
    dragging forecast output into one.
    """
    if merging():
        return
    paths = staged()
    data = [path for path in paths if is_data(path)]
    code = [path for path in paths if not is_data(path)]
    if not data or not code:
        return
    typer.echo(
        f"\n  ✘ commit blocked: this mixes {len(data)} data file(s) with "
        f"{len(code)} code file(s).\n\n"
        f"    Data ({DATA_ROOT}/) is committed to main; code goes through a "
        "worktree and a PR.\n    Split them:\n\n"
        "        git reset\n"
        f"        git add {DATA_ROOT}/ && git commit -m 'data(forecasts): …'\n"
        "        git add <code paths> && git commit -m 'feat(scope): …'\n\n"
        "    Data:",
        err=True,
    )
    for line in sample(data):
        typer.echo(line, err=True)
    typer.echo("\n    Code:", err=True)
    for line in sample(code):
        typer.echo(line, err=True)
    typer.echo("", err=True)
    raise typer.Exit(1)


def refuse_stale_base(protocol: str) -> None:
    """Refuse pushing a branch whose pull request would carry forecast data.

    The forecast loop commits data straight to local `main`, so a feature
    branch cut from it inherits those commits. While they have not reached
    `origin/main`, a request's merge base is computed against a remote that
    has never seen them, and every inherited file is folded in as a fresh
    addition with no shared ancestry — after which the next pull collides on
    every one of them.

    The drift itself is harmless; opening a request on top of it is not. So
    this refuses that moment rather than the drift, and publishing `main` is
    what settles it.
    """
    try:
        git.out("rev-parse", "--verify", "--quiet", "origin/main")
    except sh.ErrorReturnCode:
        return
    unpushed = unpushed_main()
    if not unpushed:
        return
    for update in pushed_refs(protocol):
        if update.deletion or update.remote_ref == "refs/heads/main":
            continue
        data = inherited_data(update.local_oid)
        if not data:
            continue
        typer.echo(
            f"\n  ✘ push blocked: this branch would carry {len(data)} "
            f"{DATA_ROOT}/ data file(s) into its PR.\n\n"
            f"    Local main is {unpushed} commit(s) ahead of origin/main, so "
            "this branch is\n    built on data commits the remote has never "
            "seen. GitHub would merge them\n    into the PR as new files and "
            "duplicate the data store.\n\n"
            "    Fix — publish main, then re-push:\n\n"
            "        git -C ../main push origin main\n"
            "        git fetch origin\n"
            "        git rebase origin/main\n"
            "        git push\n\n"
            "    Sample of the data files that would leak:",
            err=True,
        )
        for line in sample(data, limit=5):
            typer.echo(line, err=True)
        typer.echo(
            f"\n    Deliberately reshaping {DATA_ROOT}/? Re-run with --no-verify.\n",
            err=True,
        )
        raise typer.Exit(1)


GATE_STEPS = [
    ["run", "ruff", "format", "--check", "."],
    ["run", "ruff", "check", "."],
    ["run", "pyright"],
    ["run", "pytest", "-m", "not integration", "-q"],
    ["run", "lup-devtools", "harness", "check", "all"],
]
"""What this repository holds a branch to before it leaves the checkout.

Read-only, deliberately: a gate that reformatted the tree would leave the
push carrying content nobody reviewed, and `ruff format` is one command away
for whoever it stops.

# lup: defer: converge this on `lup-devtools dev check`, once that command's
# antipatterns and seam-boundary rows are green here — it is the same gate
# the pipeline runs and a longer one, so running the shorter list states
# this repository's debt rather than anything about the moment
"""


def run_gate() -> None:
    """Run each step in order, refusing the push at the first one that fails."""
    for step in GATE_STEPS:
        spelled = shlex.join(["uv", *step])
        typer.echo(f"  → {spelled}", err=True)
        try:
            uv(*step)
        except sh.ErrorReturnCode as error:
            typer.echo(decode_stderr(error), err=True)
            typer.echo(
                f"\n  ✘ push blocked: the quality gate failed at `{spelled}`.\n\n"
                "    A commit is local and rewritable; a push is neither. Fix "
                "it here\n    rather than finding out from CI several minutes "
                "from now.\n\n"
                "    Deliberately pushing a red branch? Re-run with --no-verify.\n",
                err=True,
            )
            raise typer.Exit(1) from error
