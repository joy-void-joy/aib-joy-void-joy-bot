"""Agent version management: show, bump, and list versions.

The version itself lives in ``[tool.lup] agent_version`` in pyproject.toml,
which is where :func:`lup.workspace.paths.agent_version` reads it from and
what therefore decides the ``notes/traces/<version>/`` directory every run
writes to. What this module adds on top of lup's own reader is the release
ritual: writing the CHANGELOG entry, tagging, and listing what has shipped.
"""

import ast
import re
import tomllib
from datetime import datetime
from pathlib import Path
from typing import Optional

import sh
import tomlkit
import typer

from lup.workspace.paths import project_root

app = typer.Typer(no_args_is_help=True)

# Anchored on the project root rather than the working directory: `bump`
# writes both, and run from a subdirectory it used to create a new manifest
# and changelog there instead of editing the real ones.
CHANGELOG_PATH = project_root() / "CHANGELOG.md"
VERSION_FILE = project_root() / "pyproject.toml"

VERSION_HISTORY_PATHS = ("pyproject.toml", "src/aib/version.py")
"""Where the agent version has been declared, current spelling first.

`list` walks git history, and history predating the move to ``[tool.lup]``
still carries the version in the module that used to hold it. Reading only
the current location would silently shorten the list to this migration."""

CHANGELOG_VERSION_RE = re.compile(r"^## v(\d+\.\d+\.\d+)\s+\((\d{4}-\d{2}-\d{2})\)")

git = sh.Command("git").bake("--no-pager", _tty_out=False)


def load_version_dates(
    path: Path = CHANGELOG_PATH,
) -> dict[str, str]:
    """Parse CHANGELOG.md for version release dates.

    Returns ``{version: date}`` e.g. ``{"3.2.0": "2026-02-24"}``.
    """
    if not path.exists():
        return {}
    result: dict[str, str] = {}
    for line in path.read_text().splitlines():
        m = CHANGELOG_VERSION_RE.match(line)
        if m:
            result[m.group(1)] = m.group(2)
    return result


def _parse_version(content: str) -> str:
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


def _get_existing_tags() -> list[str]:
    try:
        output = str(git("tag", "-l", "v*")).strip()
        return output.splitlines() if output else []
    except sh.ErrorReturnCode:
        return []


def _get_version_at_commit(commit: str) -> str:
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
            return _parse_version(content)
        except (typer.BadParameter, tomllib.TOMLDecodeError):
            continue
    raise typer.BadParameter(f"no agent version declared at {commit}")


def _get_current_version() -> str:
    return _parse_version(VERSION_FILE.read_text())


def _increment_version(version: str, level: str) -> str:
    parts = [int(p) for p in version.split(".")]
    while len(parts) < 3:
        parts.append(0)
    if level == "major":
        parts = [parts[0] + 1, 0, 0]
    elif level == "minor":
        parts = [parts[0], parts[1] + 1, 0]
    else:
        parts = [parts[0], parts[1], parts[2] + 1]
    return ".".join(str(p) for p in parts)


def _write_version(new_version: str) -> None:
    """Set ``[tool.lup] agent_version``, leaving the rest of the manifest alone.

    tomlkit rather than tomllib+dump, because a round-trip through a plain
    parser would rewrite the whole manifest — reordering tables and dropping
    every comment in a file that is mostly comments and dependency pins.
    """
    document = tomlkit.parse(VERSION_FILE.read_text())
    match document:
        case {"tool": {"lup": dict() as lup_table}}:
            lup_table["agent_version"] = new_version
        case _:
            raise typer.BadParameter(f"No [tool.lup] table in {VERSION_FILE}")
    VERSION_FILE.write_text(tomlkit.dumps(document))


def _write_changelog(
    version: str,
    summary: str,
    details: Optional[str] = None,
) -> None:
    today = datetime.now().strftime("%Y-%m-%d")
    version_clean = version.lstrip("v")

    entry_lines = [f"## v{version_clean} ({today})\n", f"\n{summary}\n"]
    if details:
        for detail in details.split(","):
            entry_lines.append(f"- {detail.strip()}\n")
    entry_lines.append("\n")
    new_entry = "".join(entry_lines)

    if CHANGELOG_PATH.exists():
        content = CHANGELOG_PATH.read_text()
        header_marker = f"## v{version_clean}"
        if header_marker in content:
            start = content.index(header_marker)
            rest = content[start + len(header_marker) :]
            next_header = rest.find("\n## ")
            if next_header >= 0:
                end = start + len(header_marker) + next_header + 1
            else:
                end = len(content)
            content = content[:start] + new_entry + content[end:]
            CHANGELOG_PATH.write_text(content)
            typer.echo(f"Updated changelog for v{version_clean}")
        else:
            lines = content.splitlines(keepends=True)
            insert_idx = 0
            for i, line in enumerate(lines):
                if line.startswith("## "):
                    insert_idx = i
                    break
            else:
                insert_idx = len(lines)
            lines.insert(insert_idx, new_entry)
            CHANGELOG_PATH.write_text("".join(lines))
            typer.echo(f"Added changelog for v{version_clean}")
    else:
        content = f"# Changelog\n\nAgent version history. Each version tracks a behavioral change.\n\n{new_entry}"
        CHANGELOG_PATH.write_text(content)
        typer.echo(f"Created CHANGELOG.md with entry for v{version_clean}")


@app.command()
def show() -> None:
    """Display the current AGENT_VERSION."""
    typer.echo(f"v{_get_current_version()}")


@app.command()
def bump(
    level: str = typer.Argument(help="Bump level: patch, minor, or major"),
    summary: str = typer.Argument(help="One-line summary of what changed"),
    details: Optional[str] = typer.Option(
        None, "--detail", "-d", help="Additional detail (comma-separated)"
    ),
    no_tag: bool = typer.Option(False, "--no-tag", help="Skip creating a git tag"),
) -> None:
    """Bump AGENT_VERSION, update changelog, and create a git tag."""
    if level not in ("patch", "minor", "major"):
        typer.echo(f"Invalid level '{level}'. Must be: patch, minor, major")
        raise typer.Exit(1)

    old_version = _get_current_version()
    new_version = _increment_version(old_version, level)

    _write_version(new_version)
    typer.echo(f"Bumped {old_version} -> {new_version} ({level})")

    _write_changelog(new_version, summary, details)

    if not no_tag:
        tag_name = f"v{new_version}"
        message = f"Agent version {new_version}: {summary}"
        existing = _get_existing_tags()
        if tag_name in existing:
            typer.echo(f"Tag {tag_name} already exists, skipping auto-tag")
        else:
            git("tag", "-a", tag_name, "HEAD", "-m", message)
            typer.echo(f"Created tag {tag_name}")


@app.command("list")
def list_cmd() -> None:
    """List all agent versions from git history."""
    try:
        log = str(
            git("log", "--all", "--oneline", "--", *VERSION_HISTORY_PATHS)
        )
    except sh.ErrorReturnCode:
        typer.echo("No version history found.")
        return

    existing_tags = _get_existing_tags()
    seen_versions: set[str] = set()

    for line in log.strip().splitlines():
        commit_hash = line.split()[0]
        try:
            version = _get_version_at_commit(commit_hash)
        except typer.BadParameter:
            continue

        if version in seen_versions:
            continue
        seen_versions.add(version)

        tagged = f"v{version}" in existing_tags
        marker = " [tagged]" if tagged else ""
        try:
            date = str(git("log", "-1", "--format=%ai", commit_hash, "--")).strip()[:10]
        except sh.ErrorReturnCode:
            date = "????"
        commit_msg = line.split(" ", 1)[1] if " " in line else ""
        typer.echo(f"  v{version:8s}  {date}  {commit_msg}{marker}")
