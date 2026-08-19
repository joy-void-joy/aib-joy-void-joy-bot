"""The one version command that is this repository's own, and its history.

The version lives in ``[tool.lup] agent_version``, which is what
:func:`lup.workspace.paths.agent_version` reads to key the
``notes/traces/<version>/`` directory every run writes to. Showing it,
recording a release, and tagging are the library's — this repository composes
that tree rather than restating it.

What stays is ``list``, and it stays because of what it has to know: where the
version has been declared *in this repository's past*. History predating the
move to ``[tool.lup]`` still carries it in the module that used to hold it, so
walking that history means reading a spelling only this repository ever had.
That is the placement test — another project would want the command and could
not use the answer.
"""

import ast
import datetime as dt
import tomllib
from pathlib import Path

import sh
import typer
from lup.devtools.changelog import Changelog
from lup.workspace.paths import project_root
from pydantic import BaseModel

CHANGELOG_PATH = project_root() / "CHANGELOG.md"
VERSION_FILE = project_root() / "pyproject.toml"

VERSION_HISTORY_PATHS = ("pyproject.toml", "src/aib/version.py")
"""Where the agent version has been declared, current spelling first.

`list` walks git history, and history predating the move to ``[tool.lup]``
still carries the version in the module that used to hold it. Reading only
the current location would silently shorten the list to this migration."""

git = sh.Command("git").bake("--no-pager", _tty_out=False)


class VersionRelease(BaseModel, frozen=True):
    """One released version and the day it shipped."""

    version: str
    day: dt.date


class VersionHistory(BaseModel, frozen=True):
    """Every release this repository's changelog records.

    A model rather than a mapping of version to date string, because a date
    is a date: the score plots that read this join a version against when it
    shipped, and a comparison between two of those is wrong the moment either
    is a string. Parsing happens once, here, where the changelog is read.
    """

    releases: list[VersionRelease] = []

    @classmethod
    def read(cls, path: Path = CHANGELOG_PATH) -> "VersionHistory":
        """The releases the changelog records, or none where it has none.

        Read as the releases a document holds rather than scanned for
        headings — the same reading the library's bump writes them with.
        """
        return cls(
            releases=[
                VersionRelease(version=version, day=day)
                for version, day in Changelog.read(path).dates().items()
            ]
        )

    def shipped(self, version: str) -> dt.date | None:
        """When one version shipped, or None where nothing records it."""
        for release in self.releases:
            if release.version == version:
                return release.day
        return None


def parse_version(content: str) -> str:
    """The agent version one file's text declares, however it spells it.

    Takes the text rather than a path because `list` reads historical
    revisions through ``git show``, where there is no file to open — and
    those revisions predate ``[tool.lup]``, so both spellings have to be
    understood. Nothing on disk is in the legacy one any more.
    """

    def assigned_in_module() -> str | None:
        """The AGENT_VERSION a pre-migration `src/aib/version.py` assigned."""
        try:
            module = ast.parse(content)
        except SyntaxError:
            return None
        for node in module.body:
            match node:
                case ast.Assign(
                    targets=[ast.Name(id="AGENT_VERSION")],
                    value=ast.Constant(value=str(version)),
                ):
                    return version
        return None

    try:
        match tomllib.loads(content):
            case {"tool": {"lup": {"agent_version": str(version)}}}:
                return version
    except tomllib.TOMLDecodeError:
        pass

    legacy = assigned_in_module()
    if legacy is not None:
        return legacy
    raise typer.BadParameter("no agent version declared")


def existing_tags() -> list[str]:
    """Every release tag this repository carries."""
    try:
        output = str(git("tag", "-l", "v*")).strip()
        return output.splitlines() if output else []
    except sh.ErrorReturnCode:
        return []


def version_at_commit(commit: str) -> str:
    """The agent version as of one commit, wherever it was declared then.

    Tried in VERSION_HISTORY_PATHS order, so a commit carrying both — the one
    that moved the declaration — answers with the current spelling.
    """
    for path in VERSION_HISTORY_PATHS:
        try:
            content = str(git("show", f"{commit}:{path}"))
        except sh.ErrorReturnCode:
            continue
        try:
            return parse_version(content)
        except (typer.BadParameter, tomllib.TOMLDecodeError):
            continue
    raise typer.BadParameter(f"no agent version declared at {commit}")


def list_cmd() -> None:
    """List all agent versions from git history."""
    try:
        log = str(git("log", "--all", "--oneline", "--", *VERSION_HISTORY_PATHS))
    except sh.ErrorReturnCode:
        typer.echo("No version history found.")
        return

    tags = existing_tags()
    seen_versions: set[str] = set()

    for line in log.strip().splitlines():
        commit_hash = line.split()[0]
        try:
            version = version_at_commit(commit_hash)
        except typer.BadParameter:
            continue

        if version in seen_versions:
            continue
        seen_versions.add(version)

        marker = " [tagged]" if f"v{version}" in tags else ""
        try:
            date = str(git("log", "-1", "--format=%ai", commit_hash, "--")).strip()[:10]
        except sh.ErrorReturnCode:
            date = "????"
        commit_msg = line.split(" ", 1)[1] if " " in line else ""
        typer.echo(f"  v{version:8s}  {date}  {commit_msg}{marker}")


def extend(app: typer.Typer) -> None:
    """Mount the one version moment that is this repository's own.

    Composed onto the library's tree the way `dev` is, rather than replacing
    it: showing a version, recording a release and tagging are not this
    repository's to hold an opinion about, and the entry that once replaced
    them took a whole release ritual with it.
    """
    app.command("list")(list_cmd)
