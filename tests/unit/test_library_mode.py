"""What `dev library` reads out of a manifest, and what it writes back.

Read over manifests written into a temporary directory rather than over this
checkout's own, because every case here is a claim about a *different* mode
than the one this repository is in — and a test that could only see `git`
would be reading one answer four times.
"""

from pathlib import Path

import pytest
import typer

import aib.devtools.library as library

MANIFEST = """\
[project]
name = "aib"
dependencies = [
    "httpx>=0.28.1",
    "lup[claude,codex,docker,web]",
]

[tool.uv.sources]
lup = {{ git = "https://github.com/joy-void-joy/lup", subdirectory = "packages/lup", {ref} }}
"""
"""A manifest in git mode, with the ref kind left open for one test to fill."""

PUBLISHED_MANIFEST = """\
[project]
name = "aib"
dependencies = [
    "httpx>=0.28.1",
    "lup[claude,codex,docker,web]",
]

[tool.uv.sources]
"""
"""The same manifest with no override, which is what `published` looks like."""


def manifest(root: Path, text: str) -> Path:
    """Write one `pyproject.toml` into a directory and hand back the root."""
    (root / "pyproject.toml").write_text(text, encoding="utf-8")
    return root


@pytest.mark.parametrize(
    ("ref", "kind", "value"),
    [
        ('rev = "dev"', "rev", "dev"),
        ('branch = "main"', "branch", "main"),
        ('tag = "v0.2.0"', "tag", "v0.2.0"),
    ],
)
def test_a_git_source_reports_the_one_ref_kind_it_pins(
    tmp_path: Path, ref: str, kind: str, value: str
) -> None:
    """Each ref kind is read back as itself rather than flattened to a branch."""
    root = manifest(tmp_path, MANIFEST.format(ref=ref))
    source = library.read_git_source(root)
    assert source is not None
    assert (source.ref_kind, source.ref) == (kind, value)
    assert library.read_mode(root) is library.LibraryMode.GIT


def test_an_absent_override_reads_as_published(tmp_path: Path) -> None:
    """No `[tool.uv.sources]` entry is the index, not a mode that failed to parse."""
    root = manifest(tmp_path, PUBLISHED_MANIFEST)
    assert library.read_mode(root) is library.LibraryMode.PUBLISHED
    assert library.read_git_source(root) is None


def test_a_workspace_member_reads_as_local(tmp_path: Path) -> None:
    """A vendored copy is classified even though this repository cannot enter it.

    Reported rather than refused, so a checkout that does vendor lup gets its
    own mode back instead of being told it resolves from the index.
    """
    root = manifest(tmp_path, PUBLISHED_MANIFEST + "lup = { workspace = true }\n")
    assert library.read_mode(root) is library.LibraryMode.LOCAL


def test_a_path_override_reads_as_linked(tmp_path: Path) -> None:
    """An editable source names the checkout it points at."""
    root = manifest(
        tmp_path,
        PUBLISHED_MANIFEST
        + 'lup = { path = "../lup/packages/lup", editable = true }\n',
    )
    assert library.read_mode(root) is library.LibraryMode.LINKED
    assert library.read_linked_path(root) == Path("../lup/packages/lup")


def test_moving_to_published_keeps_the_extras_and_adds_the_bound(
    tmp_path: Path,
) -> None:
    """The extras a project asked for survive; only the specifier changes."""
    root = manifest(tmp_path, MANIFEST.format(ref='rev = "dev"'))
    library.set_mode(root, library.LibraryMode.PUBLISHED, version="0.3.0")
    assert library.read_mode(root) is library.LibraryMode.PUBLISHED
    assert "lup[claude,codex,docker,web]>=0.3.0" in (root / "pyproject.toml").read_text(
        encoding="utf-8"
    )


def test_a_dry_run_changes_nothing_on_disk(tmp_path: Path) -> None:
    """The report a dry run prints is the only thing it produces."""
    root = manifest(tmp_path, MANIFEST.format(ref='rev = "dev"'))
    before = (root / "pyproject.toml").read_text(encoding="utf-8")
    changes = library.set_mode(
        root,
        library.LibraryMode.GIT,
        git=library.GitSource(ref_kind="branch", ref="main"),
        dry_run=True,
    )
    assert changes
    assert (root / "pyproject.toml").read_text(encoding="utf-8") == before


def test_restating_the_mode_a_project_is_in_is_no_change(tmp_path: Path) -> None:
    """Declaring what the manifest already says reports nothing to do."""
    root = manifest(tmp_path, MANIFEST.format(ref='rev = "dev"'))
    changes = library.set_mode(
        root,
        library.LibraryMode.GIT,
        git=library.GitSource(ref_kind="rev", ref="dev"),
    )
    assert changes == []


def test_vendoring_is_refused_where_there_is_nothing_to_vendor(
    tmp_path: Path,
) -> None:
    """`local` names a workspace member, and this layout has none."""
    root = manifest(tmp_path, MANIFEST.format(ref='rev = "dev"'))
    with pytest.raises(typer.BadParameter):
        library.set_mode(root, library.LibraryMode.LOCAL)


def test_two_ref_flags_are_rejected_rather_than_silently_ordered() -> None:
    """uv accepts one ref; a command line that names two is told so."""
    with pytest.raises(typer.BadParameter):
        library.git_source(library.REPOSITORY_URL, branch="dev", tag="v0.2.0")


def test_no_ref_flag_falls_back_to_the_declared_default() -> None:
    """Naming none is the ordinary case, not an error."""
    source = library.git_source(library.REPOSITORY_URL)
    assert (source.ref_kind, source.ref) == ("branch", "dev")


def test_the_locked_revision_is_the_commit_uv_resolved(tmp_path: Path) -> None:
    """A branch says where to look; the lock says what was found.

    Parsed out of the source URL's fragment, so a lock whose formatting
    changes is still read rather than scraped.
    """
    (tmp_path / "uv.lock").write_text(
        "[[package]]\n"
        'name = "lup"\n'
        'version = "0.2.0"\n'
        'source = { git = "https://github.com/joy-void-joy/lup'
        '?subdirectory=packages%2Flup&rev=dev#7423e94c" }\n',
        encoding="utf-8",
    )
    assert library.locked_revision(tmp_path) == "7423e94c"


def test_a_lock_without_lup_reports_no_revision(tmp_path: Path) -> None:
    """An empty answer, rather than a guess at which package was meant."""
    (tmp_path / "uv.lock").write_text(
        '[[package]]\nname = "httpx"\nversion = "0.28.1"\n', encoding="utf-8"
    )
    assert library.locked_revision(tmp_path) == ""


def test_an_unreachable_index_is_not_an_absent_release() -> None:
    """The two outcomes stay apart, because they call for different answers."""
    unreachable = library.ReleaseProbe(unreachable="connection refused")
    absent = library.ReleaseProbe()
    assert "settles nothing" in " ".join(unreachable.describe())
    assert "no release published yet" in absent.describe()
