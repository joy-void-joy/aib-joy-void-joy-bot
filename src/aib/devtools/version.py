"""Agent version management: show, bump, and list versions."""

import re
from datetime import datetime
from pathlib import Path
from typing import Optional

import sh
import typer

app = typer.Typer(no_args_is_help=True)

CHANGELOG_PATH = Path("CHANGELOG.md")
VERSION_FILE = Path("src/aib/version.py")
VERSION_RE = re.compile(r'^AGENT_VERSION\s*=\s*"([^"]+)"', re.MULTILINE)

_git = sh.Command("git").bake("--no-pager", _tty_out=False)


def _parse_version(content: str) -> str:
    match = VERSION_RE.search(content)
    if match:
        return match.group(1)
    raise typer.BadParameter("Could not parse AGENT_VERSION")


def _get_existing_tags() -> list[str]:
    try:
        output = str(_git("tag", "-l", "v*")).strip()
        return output.splitlines() if output else []
    except sh.ErrorReturnCode:
        return []


def _get_version_at_commit(commit: str) -> str:
    try:
        content = str(_git("show", f"{commit}:src/aib/version.py"))
        return _parse_version(content)
    except sh.ErrorReturnCode as e:
        raise typer.BadParameter(f"git show failed for {commit}: {e}") from e


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
    content = VERSION_FILE.read_text()
    updated = VERSION_RE.sub(f'AGENT_VERSION = "{new_version}"', content)
    VERSION_FILE.write_text(updated)


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
            _git("tag", "-a", tag_name, "HEAD", "-m", message)
            typer.echo(f"Created tag {tag_name}")


@app.command("list")
def list_cmd() -> None:
    """List all agent versions from git history."""
    try:
        log = str(_git("log", "--all", "--oneline", "--", "src/aib/version.py"))
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
            date = str(_git("log", "-1", "--format=%ai", commit_hash, "--")).strip()[
                :10
            ]
        except sh.ErrorReturnCode:
            date = "????"
        commit_msg = line.split(" ", 1)[1] if " " in line else ""
        typer.echo(f"  v{version:8s}  {date}  {commit_msg}{marker}")
