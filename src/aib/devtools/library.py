"""How this repository obtains the ``lup`` library, read and rewritten.

Three modes are reachable here, and the mode decides what upgrading even
means:

``git``
    The repository itself, resolved at a branch, tag, or commit. What this
    project runs. Upgrading is ``uv lock --upgrade-package lup``, which
    re-resolves the same ref rather than moving it.
``published``
    The release from the package index. Upgrading is the same command; what
    differs is that the version is a release rather than whatever the ref
    points at today.
``linked``
    An editable install of a lup checkout on the same disk. Library changes
    made while working here land in lup's own repository, which is how an
    improvement discovered downstream reaches the library instead of being
    reimplemented.

A fourth mode exists upstream — a copy vendored under ``packages/lup``, wired
as a uv workspace member — and this repository is not in it and cannot enter
it: there is no such directory to vendor. It is classified rather than
offered, so ``status`` answers correctly for a checkout that has one instead
of misreporting it as published.

Reading is a ``tomllib`` parse matched structurally; writing goes through
``tomlkit`` so comments and layout survive the edit.

Examples::

    $ uv run lup-devtools dev library status
    $ uv run lup-devtools dev library release
    $ uv run lup-devtools dev library git --branch dev
    $ uv run lup-devtools dev library link ../../lup.git/tree/dev
"""

import tomllib
import urllib.parse
from enum import StrEnum
from importlib.metadata import version as installed_version
from pathlib import Path
from typing import Literal

import httpx
import tomlkit
import tomlkit.items
import typer
from packaging.requirements import Requirement
from pydantic import BaseModel, ValidationError

from lup.workspace.paths import find_project_root

# lup: ignore[constant-declaration] — the name the library is published under
DISTRIBUTION = "lup"

PACKAGE_SUBDIRECTORY = "packages/lup"
"""Where the distribution sits inside its repository — a fixed fact about
lup's own layout, not a choice an adopter makes."""

REPOSITORY_URL = "https://github.com/joy-void-joy/lup"
"""Where the library is published as source. Overridable: a fork, a mirror, or
a private host serves the same package from the same layout."""

RELEASE_INDEX_URL = f"https://pypi.org/pypi/{DISTRIBUTION}/json"
"""Where a release is looked up. Overridable: a project resolving lup through
a private index asks that index the same question in the same shape."""

RELEASE_PROBE_SECONDS = 10.0
"""How long the look-up waits. An unreachable index is an answer this command
knows how to give, and giving it beats blocking whoever is waiting on it."""

UPGRADE_COMMAND = (
    "uv lock --upgrade-package lup"
    " && uv sync"
    " && uv run lup-devtools harness generate all"
)
"""What moving to the tip of a pinned ref takes, start to finish.

Three commands rather than one because the regeneration is not optional: a
newer lup ships newer skill, agent and policy declarations, and this project's
native trees compile from them — so until it runs, the upgrade is installed
but not in effect, and `harness check all` calls the trees stale.
"""


class LibraryMode(StrEnum):
    """Where the ``lup`` distribution is resolved from."""

    PUBLISHED = "published"
    GIT = "git"
    LOCAL = "local"
    LINKED = "linked"


type GitRefKind = Literal["branch", "tag", "rev"]
"""Which kind of ref a git source pins, spelled as uv spells it."""


class GitSource(BaseModel, frozen=True):
    """A repository and the single ref of it this project resolves ``lup`` at.

    The ref is one field pair rather than three optional ones, so a source
    naming both a branch and a tag cannot be constructed — uv accepts only
    one, and a model that can hold two only moves the error later.
    """

    url: str = REPOSITORY_URL
    ref_kind: GitRefKind = "branch"
    ref: str = "dev"

    def entry(self) -> tomlkit.items.InlineTable:
        """Render the ``[tool.uv.sources]`` value this source declares."""
        entry = tomlkit.inline_table()
        entry.update(
            {
                "git": self.url,
                self.ref_kind: self.ref,
                "subdirectory": PACKAGE_SUBDIRECTORY,
            }
        )
        return entry


class RefFlag(BaseModel, frozen=True):
    """One ref-kind flag, and the ref a command line gave it — or nothing."""

    kind: GitRefKind
    ref: str | None = None


def git_source(
    url: str,
    *,
    branch: str | None = None,
    tag: str | None = None,
    rev: str | None = None,
) -> GitSource:
    """Collapse the three ref flags into the one ref a git source may carry.

    A command line can spell all three; uv accepts one. Rejecting the excess
    here is what keeps :class:`GitSource` unable to represent the conflict.
    """
    named = [
        flag
        for flag in (
            RefFlag(kind="branch", ref=branch),
            RefFlag(kind="tag", ref=tag),
            RefFlag(kind="rev", ref=rev),
        )
        if flag.ref is not None
    ]
    match named:
        case []:
            return GitSource(url=url)
        case [only] if only.ref is not None:
            return GitSource(url=url, ref_kind=only.kind, ref=only.ref)
        case _:
            raise typer.BadParameter(
                "name one of --branch, --tag, or --rev, not "
                + " and ".join(f"--{flag.kind}" for flag in named)
            )


def read_mode(root: Path) -> LibraryMode:
    """Classify the acquisition mode ``pyproject.toml`` declares."""
    with (root / "pyproject.toml").open("rb") as handle:
        data = tomllib.load(handle)
    match data:
        case {"tool": {"uv": {"sources": {"lup": {"workspace": True}}}}}:
            return LibraryMode.LOCAL
        case {"tool": {"uv": {"sources": {"lup": {"path": str()}}}}}:
            return LibraryMode.LINKED
        case {"tool": {"uv": {"sources": {"lup": {"git": str()}}}}}:
            return LibraryMode.GIT
        case _:
            return LibraryMode.PUBLISHED


def read_git_source(root: Path) -> GitSource | None:
    """Return the repository and the ref it is pinned at, when git."""
    with (root / "pyproject.toml").open("rb") as handle:
        data = tomllib.load(handle)
    match data:
        case {"tool": {"uv": {"sources": {"lup": {"git": str(url), **rest}}}}}:
            declared = rest
        case _:
            return None
    match declared:
        case {"branch": str(ref)}:
            return GitSource(url=url, ref_kind="branch", ref=ref)
        case {"tag": str(ref)}:
            return GitSource(url=url, ref_kind="tag", ref=ref)
        case {"rev": str(ref)}:
            return GitSource(url=url, ref_kind="rev", ref=ref)
        case _:
            return GitSource(url=url)


def read_linked_path(root: Path) -> Path | None:
    """Return the checkout an editable source points at, when linked."""
    with (root / "pyproject.toml").open("rb") as handle:
        data = tomllib.load(handle)
    match data:
        case {"tool": {"uv": {"sources": {"lup": {"path": str(path)}}}}}:
            return Path(path)
        case _:
            return None


def locked_revision(root: Path) -> str:
    """The commit ``uv.lock`` actually resolved, for a ref that moves.

    A branch says where to look rather than what was found, so a project
    pinned to one cannot answer "which lup am I running" from the manifest
    alone. The lock can, and it is the file every session's environment was
    built from.

    uv writes the resolved commit as the fragment of the source URL, so the
    answer comes from parsing that URL rather than from carving the line it
    sits on.
    """
    with (root / "uv.lock").open("rb") as handle:
        lock = tomllib.load(handle)
    match lock:
        case {"package": [*packages]}:
            locked = packages
        case _:
            return ""
    for package in locked:
        match package:
            case {"name": str(name), "source": {"git": str(url)}} if (
                name == DISTRIBUTION
            ):
                return urllib.parse.urlsplit(url).fragment
    return ""


def requirement_for(entry: str, version: str | None) -> str:
    """Restate one requirement with, or without, a lower version bound.

    The extras the project asked for survive: only the specifier changes,
    because a source override supplies the version in every mode but
    ``published``.
    """
    requirement = Requirement(entry)
    extras = f"[{','.join(sorted(requirement.extras))}]" if requirement.extras else ""
    bound = f">={version}" if version is not None else ""
    return f"{requirement.name}{extras}{bound}"


def apply_dependency(document: tomlkit.TOMLDocument, version: str | None) -> list[str]:
    """Restate the ``lup`` requirement in ``[project].dependencies``."""
    dependencies = document["project"]["dependencies"]
    for index, entry in enumerate(dependencies):
        if Requirement(str(entry)).name != DISTRIBUTION:
            continue
        restated = requirement_for(str(entry), version)
        if restated == str(entry):
            return []
        dependencies[index] = restated
        return [f"dependency: {entry} -> {restated}"]
    raise KeyError(f"no {DISTRIBUTION} requirement in [project].dependencies")


def source_entry(
    mode: LibraryMode, checkout: Path | None, git: GitSource | None
) -> tomlkit.items.InlineTable | None:
    """The ``[tool.uv.sources]`` value one mode declares, or none for published.

    ``local`` raises rather than rendering: there is no ``packages/lup`` here
    to resolve through, so a manifest naming one would describe a workspace
    member that does not exist.
    """
    match mode:
        case LibraryMode.PUBLISHED:
            return None
        case LibraryMode.GIT:
            if git is None:
                raise ValueError("git mode needs a repository and ref")
            return git.entry()
        case LibraryMode.LINKED:
            if checkout is None:
                raise ValueError("linked mode needs a checkout path")
            entry = tomlkit.inline_table()
            entry.update({"path": str(checkout), "editable": True})
            return entry
        case LibraryMode.LOCAL:
            raise typer.BadParameter(
                f"there is no {PACKAGE_SUBDIRECTORY}/ in this repository, so "
                "there is no vendored library to resolve through. Use "
                "`dev library link <checkout>` to develop against one in place."
            )


def apply_source(
    document: tomlkit.TOMLDocument,
    mode: LibraryMode,
    checkout: Path | None = None,
    git: GitSource | None = None,
) -> list[str]:
    """Declare, or clear, the ``[tool.uv.sources]`` override for ``lup``."""
    sources = document["tool"]["uv"]["sources"]
    entry = source_entry(mode, checkout, git)
    if entry is None:
        if DISTRIBUTION not in sources:
            return []
        del sources[DISTRIBUTION]
        return ["source: resolved from the package index"]
    if DISTRIBUTION in sources and dict(sources[DISTRIBUTION]) == dict(entry):
        return []
    sources[DISTRIBUTION] = entry
    return [f"source: {tomlkit.dumps(entry).strip()}"]


def set_mode(
    root: Path,
    mode: LibraryMode,
    *,
    version: str | None = None,
    checkout: Path | None = None,
    git: GitSource | None = None,
    dry_run: bool = False,
) -> list[str]:
    """Rewrite ``pyproject.toml`` so ``lup`` resolves the way ``mode`` says."""
    pyproject = root / "pyproject.toml"
    document = tomlkit.parse(pyproject.read_text(encoding="utf-8"))
    changes = [
        *apply_dependency(document, version if mode is LibraryMode.PUBLISHED else None),
        *apply_source(document, mode, checkout, git),
    ]
    if changes and not dry_run:
        pyproject.write_text(tomlkit.dumps(document), encoding="utf-8")
    return changes


def report(changes: list[str], dry_run: bool, settled: str) -> None:
    """Print one mode change, or say the project already reads that way."""
    if not changes:
        typer.echo(settled)
        return
    typer.echo(f"Dry run — {len(changes)} change(s):" if dry_run else "Changed:")
    for change in changes:
        typer.echo(f"  {change}")
    if not dry_run:
        typer.echo(f"\nNext: {UPGRADE_COMMAND.removeprefix('uv lock ')}")


class ReleaseIndexInfo(BaseModel):
    """The one field of the index's document this reads."""

    version: str


class ReleaseIndexDocument(BaseModel):
    """A package index's answer about one distribution."""

    info: ReleaseIndexInfo


class ReleaseProbe(BaseModel, frozen=True):
    """What the package index holds for lup: a version, nothing, or no answer.

    The third outcome stays itself instead of collapsing into the second. An
    index that could not be reached has not said a release is absent, and
    reading it that way re-pins a project on the strength of a dropped
    connection.

    What this does not decide is the acquisition mode. Only one half of that
    is a fact — whether a release exists at all — and the other half is what
    this project is to the library: one that works on lup, dogfooding a branch
    and sending changes back, wants that branch whether or not a release was
    cut from it.
    """

    version: str = ""
    unreachable: str = ""

    def describe(self) -> list[str]:
        """What the index answered, and the command that takes it at its word."""
        if self.unreachable:
            return [
                f"index unreachable: {self.unreachable}",
                "A probe that did not land settles nothing. Retry, or declare "
                "the mode this project already knows it wants.",
            ]
        if not self.version:
            return [
                "no release published yet",
                f"dev library {LibraryMode.GIT} --branch <branch>",
            ]
        return [
            f"released: {self.version}",
            f"dev library use {LibraryMode.PUBLISHED} --version {self.version}",
            f"`{LibraryMode.GIT}` stays a live choice: a project that works on "
            "lup as well as with it runs the branch it is improving rather "
            "than the last release cut from it.",
        ]


def probe_release(
    url: str = RELEASE_INDEX_URL, timeout: float = RELEASE_PROBE_SECONDS
) -> ReleaseProbe:
    """Ask the package index whether a release of lup exists.

    A missing project is the index answering rather than failing: before the
    first release that is the true state of the world, and it is the answer
    that sends a project to the repository rather than to nothing.
    """
    try:
        response = httpx.get(url, timeout=timeout, follow_redirects=True)
    except httpx.HTTPError as error:
        return ReleaseProbe(unreachable=f"{type(error).__name__}: {error}")
    if response.status_code == httpx.codes.NOT_FOUND:
        return ReleaseProbe()
    if response.status_code != httpx.codes.OK:
        return ReleaseProbe(unreachable=f"{url} answered {response.status_code}")
    try:
        document = ReleaseIndexDocument.model_validate_json(response.content)
    except ValidationError:
        return ReleaseProbe(unreachable=f"{url} answered a document it could not read")
    return ReleaseProbe(version=document.info.version)


def status_lines(root: Path) -> list[str]:
    """What this checkout resolves lup through, as a person reads it."""
    mode = read_mode(root)
    match mode:
        case LibraryMode.LINKED:
            return [f"mode: {mode}", f"checkout: {read_linked_path(root)}"]
        case LibraryMode.LOCAL:
            return [f"mode: {mode}", f"vendored: {root / PACKAGE_SUBDIRECTORY}"]
        case LibraryMode.PUBLISHED:
            return [f"mode: {mode}", f"version: {installed_version(DISTRIBUTION)}"]
        case LibraryMode.GIT:
            source = read_git_source(root)
            if source is None:
                return [f"mode: {mode}"]
            revision = locked_revision(root)
            return [
                f"mode: {mode}",
                f"repository: {source.url}",
                f"{source.ref_kind}: {source.ref}",
                *([f"locked at: {revision}"] if revision else []),
                f"upgrade: {UPGRADE_COMMAND}",
            ]


def library_status() -> None:
    """CLI entry for ``lup-devtools dev library status``."""
    for line in status_lines(find_project_root()):
        typer.echo(line)


def library_release() -> None:
    """CLI entry for ``lup-devtools dev library release``."""
    for line in probe_release().describe():
        typer.echo(line)


def use_library(mode: LibraryMode, version: str | None, dry_run: bool) -> None:
    """CLI entry for ``lup-devtools dev library use``."""
    root = find_project_root()
    changes = set_mode(root, mode, version=version, dry_run=dry_run)
    report(changes, dry_run, f"Already resolving {DISTRIBUTION} as {mode}.")


def git_library(source: GitSource, dry_run: bool) -> None:
    """CLI entry for ``lup-devtools dev library git``."""
    root = find_project_root()
    changes = set_mode(root, LibraryMode.GIT, git=source, dry_run=dry_run)
    report(
        changes,
        dry_run,
        f"Already resolving {DISTRIBUTION} from {source.url} "
        f"at {source.ref_kind} {source.ref}.",
    )


def link_library(checkout: Path, dry_run: bool) -> None:
    """CLI entry for ``lup-devtools dev library link``."""
    root = find_project_root()
    package = (checkout / PACKAGE_SUBDIRECTORY).resolve()
    if not (package / "pyproject.toml").is_file():
        raise typer.BadParameter(f"no lup package at {package}")
    changes = set_mode(root, LibraryMode.LINKED, checkout=package, dry_run=dry_run)
    report(changes, dry_run, f"Already linked to {package}.")
