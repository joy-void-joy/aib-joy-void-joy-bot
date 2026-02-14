#!/usr/bin/env python3
"""Manage agent version bumps, tags, and changelog.

Bump the agent version, create git tags, and maintain a CHANGELOG.md
mapping versions to their key changes.

Usage:
    uv run python .claude/plugins/aib/scripts/version_tag.py bump <level> <summary> [--detail D]
    uv run python .claude/plugins/aib/scripts/version_tag.py tag [--commit HASH] [--message MSG]
    uv run python .claude/plugins/aib/scripts/version_tag.py list
    uv run python .claude/plugins/aib/scripts/version_tag.py history
    uv run python .claude/plugins/aib/scripts/version_tag.py changelog <version> <summary>
"""

import re
from datetime import datetime
from pathlib import Path
from typing import Optional

import sh
import typer

app = typer.Typer(help="Agent version tagging and changelog management.")
git = sh.git.bake("--no-pager", _tty_out=False)

CHANGELOG_PATH = Path("CHANGELOG.md")
VERSION_FILE = Path("src/aib/version.py")
VERSION_RE = re.compile(r'^AGENT_VERSION\s*=\s*"([^"]+)"', re.MULTILINE)


def _parse_version(content: str) -> str:
    """Extract AGENT_VERSION from file content."""
    match = VERSION_RE.search(content)
    if match:
        return match.group(1)
    raise typer.BadParameter("Could not parse AGENT_VERSION")


def _get_existing_tags() -> list[str]:
    """Get all existing git tags."""
    try:
        output = git("tag", "-l", "v*").strip()
        return output.splitlines() if output else []
    except sh.ErrorReturnCode:
        return []


def _get_version_at_commit(commit: str) -> str:
    """Get AGENT_VERSION at a specific commit."""
    try:
        content = str(git("show", f"{commit}:src/aib/version.py"))
        return _parse_version(content)
    except sh.ErrorReturnCode as e:
        raise typer.BadParameter(f"git show failed for {commit}: {e}") from e


def _get_current_version() -> str:
    """Read AGENT_VERSION from the working tree."""
    return _parse_version(VERSION_FILE.read_text())


def _increment_version(version: str, level: str) -> str:
    """Increment a semver string at the given level."""
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
    """Write AGENT_VERSION to version.py."""
    content = VERSION_FILE.read_text()
    updated = VERSION_RE.sub(f'AGENT_VERSION = "{new_version}"', content)
    VERSION_FILE.write_text(updated)


@app.command()
def bump(
    level: str = typer.Argument(help="Bump level: patch, minor, or major"),
    summary: str = typer.Argument(help="One-line summary of what changed"),
    details: Optional[str] = typer.Option(
        None, "--detail", "-d", help="Additional detail (comma-separated)"
    ),
) -> None:
    """Bump AGENT_VERSION, update version.py, and add a changelog entry."""
    if level not in ("patch", "minor", "major"):
        typer.echo(f"Invalid level '{level}'. Must be: patch, minor, major")
        raise typer.Exit(1)

    old_version = _get_current_version()
    new_version = _increment_version(old_version, level)

    _write_version(new_version)
    typer.echo(f"Bumped {old_version} → {new_version} ({level})")

    changelog(new_version, summary, details)


@app.command()
def tag(
    commit: str = typer.Option(
        "HEAD", "--commit", "-c", help="Commit to tag (default: HEAD)"
    ),
    message: str = typer.Option(
        "", "--message", "-m", help="Tag message (default: auto-generated)"
    ),
    force: bool = typer.Option(False, "--force", "-f", help="Overwrite existing tag"),
) -> None:
    """Create a git tag for the agent version at a commit."""
    version = _get_version_at_commit(commit)
    tag_name = f"v{version}"
    existing = _get_existing_tags()

    if tag_name in existing and not force:
        typer.echo(f"Tag {tag_name} already exists. Use --force to overwrite.")
        raise typer.Exit(1)

    if not message:
        short_hash = str(git("rev-parse", "--short", commit)).strip()
        commit_msg = str(git("log", "--format=%s", "-1", commit)).strip()
        message = f"Agent version {version} at {short_hash}: {commit_msg}"

    force_flag = ["-f"] if force else []
    git("tag", *force_flag, "-a", tag_name, commit, "-m", message)
    typer.echo(f"Created tag {tag_name} at {commit}")


@app.command()
def list() -> None:  # noqa: A001
    """List all agent version tags with dates."""
    tags = _get_existing_tags()
    if not tags:
        typer.echo("No version tags found.")
        return

    for tag_name in sorted(
        tags, key=lambda t: [int(x) for x in t.lstrip("v").split(".")]
    ):
        try:
            date = str(git("log", "-1", "--format=%ai", tag_name, "--")).strip()[:10]
            msg = str(git("tag", "-l", "-n1", tag_name)).strip()
            typer.echo(f"  {msg:60s}  ({date})")
        except sh.ErrorReturnCode:
            typer.echo(f"  {tag_name}")


@app.command()
def history() -> None:
    """Show version bumps from git history."""
    try:
        log = str(git("log", "--all", "--oneline", "--", "src/aib/version.py"))
    except sh.ErrorReturnCode:
        typer.echo("No version history found.")
        return

    typer.echo("Version bumps in git history:\n")
    for line in log.strip().splitlines():
        commit_hash = line.split()[0]
        try:
            version = _get_version_at_commit(commit_hash)
            tagged = f"v{version}" in _get_existing_tags()
            marker = " [tagged]" if tagged else ""
            typer.echo(
                f"  {commit_hash}  v{version:8s}  {line.split(' ', 1)[1]}{marker}"
            )
        except (typer.BadParameter, Exception):
            typer.echo(f"  {commit_hash}  ???       {line.split(' ', 1)[1]}")


@app.command()
def changelog(
    version: str = typer.Argument(help="Version (e.g., '0.10.0')"),
    summary: str = typer.Argument(help="One-line summary of key changes"),
    details: Optional[str] = typer.Option(
        None, "--detail", "-d", help="Additional detail (comma-separated)"
    ),
) -> None:
    """Add or update a changelog entry for a version."""
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
            # Replace existing entry — find start and next ## header
            start = content.index(header_marker)
            rest = content[start + len(header_marker) :]
            next_header = rest.find("\n## ")
            if next_header >= 0:
                end = start + len(header_marker) + next_header + 1
            else:
                end = len(content)
            content = content[:start] + new_entry + content[end:]
            CHANGELOG_PATH.write_text(content)
            typer.echo(f"Updated entry for v{version_clean}")
        else:
            # Insert after the main header
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
            typer.echo(f"Added entry for v{version_clean}")
    else:
        content = f"# Changelog\n\nAgent version history. Each version tracks a behavioral change.\n\n{new_entry}"
        CHANGELOG_PATH.write_text(content)
        typer.echo(f"Created CHANGELOG.md with entry for v{version_clean}")


@app.command()
def tag_all() -> None:
    """Retroactively tag all version bumps found in git history."""
    existing = _get_existing_tags()
    try:
        log = str(git("log", "--all", "--oneline", "--", "src/aib/version.py"))
    except sh.ErrorReturnCode:
        typer.echo("No version history found.")
        return

    # Collect version→commit mapping (first commit where version appears)
    version_commits: dict = {}
    for line in reversed(log.strip().splitlines()):
        commit_hash = line.split()[0]
        try:
            version = _get_version_at_commit(commit_hash)
            version_commits[version] = commit_hash
        except (typer.BadParameter, Exception):
            continue

    created = 0
    skipped = 0
    for version, commit_hash in sorted(
        version_commits.items(),
        key=lambda x: [int(p) for p in x[0].split(".")],
    ):
        tag_name = f"v{version}"
        if tag_name in existing:
            typer.echo(f"  {tag_name:10s} at {commit_hash} [already exists]")
            skipped += 1
        else:
            commit_msg = str(git("log", "--format=%s", "-1", commit_hash)).strip()
            msg = f"Agent version {version}: {commit_msg}"
            git("tag", "-a", tag_name, commit_hash, "-m", msg)
            typer.echo(f"  {tag_name:10s} at {commit_hash} [created]")
            created += 1

    typer.echo(f"\nDone: {created} created, {skipped} already existed")


if __name__ == "__main__":
    app()
