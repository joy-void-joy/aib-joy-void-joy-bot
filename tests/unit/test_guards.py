"""What the two refusals this repository adds actually refuse.

Both are read over a real repository rather than over a stubbed git, because
each is a claim about what git reports at a moment — which files are staged,
which refs a push carries — and a stub would be the same reading twice.
"""

from pathlib import Path

import pytest
import sh
import typer

import aib.devtools.guards as guards

IDENTITY = ("-c", "user.email=test@example.test", "-c", "user.name=Test")
"""Carried per invocation, so a misbound fixture writes into no shared config."""

ZERO = guards.ZERO_OID


def repository(root: Path) -> sh.Command:
    """An initialized repository with no hooks of its own, bound to `root`."""
    root.mkdir(parents=True, exist_ok=True)
    hooks = root.parent / "hooks"
    hooks.mkdir(parents=True, exist_ok=True)
    git = sh.Command("git").bake(
        "-C",
        str(root),
        "-c",
        "commit.gpgsign=false",
        "-c",
        f"core.hooksPath={hooks}",
        *IDENTITY,
        _tty_out=False,
    )
    git("init", "-b", "main")
    return git


def write(root: Path, name: str, content: str = "x\n") -> None:
    """Create a file, and whatever directories its path names."""
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


@pytest.fixture
def checkout(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> sh.Command:
    """A repository the guards read, with the process standing inside it."""
    root = tmp_path / "repo"
    git = repository(root)
    monkeypatch.chdir(root)
    return git


def test_a_commit_of_only_data_is_allowed(checkout: sh.Command) -> None:
    """The route data actually takes, which must not be the thing refused."""
    write(Path.cwd(), "notes/traces/7.2.0/forecasts/1/report.md")
    checkout("add", "-A")

    guards.refuse_mixed_commit()


def test_a_commit_of_only_code_is_allowed(checkout: sh.Command) -> None:
    """The other route, for the same reason."""
    write(Path.cwd(), "src/aib/thing.py")
    checkout("add", "-A")

    guards.refuse_mixed_commit()


def test_a_commit_mixing_data_with_code_is_refused(checkout: sh.Command) -> None:
    """The commit belonging to neither route.

    It cannot land on `main` without skipping review, and it cannot open a
    pull request without dragging forecast output into one — so it is refused
    where it is still one `git reset` from being two commits.
    """
    write(Path.cwd(), "notes/traces/7.2.0/forecasts/1/report.md")
    write(Path.cwd(), "src/aib/thing.py")
    checkout("add", "-A")

    with pytest.raises(typer.Exit):
        guards.refuse_mixed_commit()


def test_a_merge_carrying_both_is_allowed(checkout: sh.Command) -> None:
    """A merge is not authoring either side; it records that two histories met.

    Refusing one would leave a merge of `main` into a feature branch — the
    ordinary way a branch catches up — impossible to conclude.
    """
    write(Path.cwd(), "notes/traces/7.2.0/forecasts/1/report.md")
    write(Path.cwd(), "src/aib/thing.py")
    checkout("add", "-A")
    git_dir = Path(str(checkout("rev-parse", "--git-dir")).strip())
    (git_dir / "MERGE_HEAD").write_text(f"{'a' * 40}\n", encoding="utf-8")

    guards.refuse_mixed_commit()


def test_a_file_named_notes_outside_the_data_root_is_code(
    checkout: sh.Command,
) -> None:
    """`notes/` is a root, not a word — a module named for it is still code."""
    assert not guards.is_data(Path("src/aib/notes.py"))
    assert not guards.is_data(Path("notes"))
    assert guards.is_data(Path("notes/worldview/forecasts/x.json"))


def test_the_ref_list_is_read_as_git_writes_it() -> None:
    """Git's own pre-push protocol, including the shape that says deletion."""
    updates = guards.pushed_refs(
        f"refs/heads/feat abc123 refs/heads/feat def456\n"
        f"refs/heads/spent {ZERO} refs/heads/spent 000abc\n"
        "a line that is not four fields\n"
    )

    assert [update.remote_ref for update in updates] == [
        "refs/heads/feat",
        "refs/heads/spent",
    ]
    assert not updates[0].deletion
    assert updates[1].deletion


def push_setup(root: Path) -> sh.Command:
    """A checkout with an origin, one published commit, and a branch off it."""
    origin = root.parent / "origin.git"
    sh.Command("git")("init", "--bare", "-b", "main", str(origin))
    git = repository(root)
    git("remote", "add", "origin", str(origin))
    write(root, "src/aib/base.py")
    git("add", "-A")
    git("commit", "-m", "chore: base")
    git("push", "origin", "main")
    return git


def branch_carrying_data(git: sh.Command, root: Path) -> str:
    """A feature branch cut from a `main` holding an unpublished data commit."""
    write(root, "notes/traces/7.2.0/forecasts/1/report.md")
    git("add", "-A")
    git("commit", "-m", "data(forecasts): a batch the remote has not seen")
    git("checkout", "-b", "feat")
    write(root, "src/aib/feature.py")
    git("add", "-A")
    git("commit", "-m", "feat(aib): a change")
    return str(git("rev-parse", "HEAD")).strip()


def test_a_branch_built_on_an_unpublished_main_is_refused(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The moment that put 506 data files into one pull request.

    The branch itself authored no data. It inherits a commit `origin/main`
    has never seen, so the request's merge base is computed against a remote
    without it and every inherited file is folded in as a fresh addition.
    """
    root = tmp_path / "repo"
    git = push_setup(root)
    monkeypatch.chdir(root)
    head = branch_carrying_data(git, root)

    with pytest.raises(typer.Exit):
        guards.refuse_stale_base(f"refs/heads/feat {head} refs/heads/feat {ZERO}\n")


def test_the_same_branch_is_allowed_once_main_is_published(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Publishing `main` is the fix, so it has to be the whole fix.

    Once the remote holds those commits the merge base is correct by
    construction, and the branch that was refused a moment ago is the same
    branch.
    """
    root = tmp_path / "repo"
    git = push_setup(root)
    monkeypatch.chdir(root)
    head = branch_carrying_data(git, root)
    git("push", "origin", "main")

    guards.refuse_stale_base(f"refs/heads/feat {head} refs/heads/feat {ZERO}\n")


def test_pushing_main_itself_is_how_data_is_meant_to_reach_the_remote(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """The refusal must not block the one push that settles it."""
    root = tmp_path / "repo"
    git = push_setup(root)
    monkeypatch.chdir(root)
    branch_carrying_data(git, root)
    main = str(git("rev-parse", "main")).strip()

    guards.refuse_stale_base(f"refs/heads/main {main} refs/heads/main {ZERO}\n")


def test_deleting_a_branch_carries_nothing_to_judge(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """A deletion uploads no tree, so there is nothing for this to read."""
    root = tmp_path / "repo"
    git = push_setup(root)
    monkeypatch.chdir(root)
    branch_carrying_data(git, root)

    guards.refuse_stale_base(f"refs/heads/spent {ZERO} refs/heads/spent 000abc\n")
