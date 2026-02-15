"""Development tools: worktree management and version tagging."""

import re
import shutil
from datetime import datetime
from pathlib import Path
from typing import Optional

import sh
import typer

app = typer.Typer(no_args_is_help=True)


# ---------------------------------------------------------------------------
# Worktree management
# ---------------------------------------------------------------------------

PLUGIN_CACHE_DIR = (
    Path.home() / ".claude" / "plugins" / "cache" / "local" / "aib-workflow"
)

GITIGNORED_DATA_DIRS = ["logs"]


def _get_tree_dir() -> Path:
    """Get the tree directory that contains worktrees."""
    cwd = Path.cwd().resolve()

    git_path = cwd / ".git"
    if git_path.exists() and git_path.is_file():
        if cwd.parent.name == "tree":
            return cwd.parent

    if cwd.name == "tree":
        return cwd

    for parent in cwd.parents:
        tree_dir = parent / "tree"
        if tree_dir.exists() and tree_dir.is_dir():
            return tree_dir

    typer.echo(f"Error: Could not find tree/ directory from {cwd}", err=True)
    raise typer.Exit(1)


@app.command("worktree")
def worktree_cmd(
    name: str = typer.Argument(..., help="Name for the new worktree/branch"),
    no_sync: bool = typer.Option(False, "--no-sync", help="Skip running uv sync"),
    no_plugin_refresh: bool = typer.Option(
        False, "--no-plugin-refresh", help="Skip plugin cache refresh and install"
    ),
    copy_data: bool = typer.Option(
        True,
        "--copy-data/--no-copy-data",
        help="Copy gitignored data directories to new worktree",
    ),
) -> None:
    """Create a new worktree with plugin cache refresh."""
    cwd = Path.cwd().resolve()
    tree_dir = _get_tree_dir()
    new_worktree_path = tree_dir / name

    if new_worktree_path.exists():
        typer.echo(f"Error: {new_worktree_path} already exists", err=True)
        raise typer.Exit(1)

    git = sh.Command("git")
    uv = sh.Command("uv")

    try:
        current_branch = str(git("branch", "--show-current", _tty_out=False)).strip()
    except sh.ErrorReturnCode:
        typer.echo("Error: Could not determine current branch", err=True)
        raise typer.Exit(1)

    branch_name = name

    typer.echo(f"Creating worktree '{name}' from branch '{current_branch}'...")
    typer.echo(f"  Location: {new_worktree_path}")
    typer.echo(f"  New branch: {branch_name}")
    typer.echo()

    try:
        git(
            "worktree", "add", str(new_worktree_path), "-b", branch_name, _tty_out=False
        )
        typer.echo("Worktree created")
    except sh.ErrorReturnCode as e:
        typer.echo(f"Error creating worktree: {e.stderr.decode()}", err=True)
        raise typer.Exit(1)

    env_local = cwd / ".env.local"
    if env_local.exists():
        shutil.copy2(env_local, new_worktree_path / ".env.local")
        typer.echo("Copied .env.local")

    if copy_data:
        for dir_name in GITIGNORED_DATA_DIRS:
            source_dir = cwd / dir_name
            target_dir = new_worktree_path / dir_name
            if source_dir.exists() and source_dir.is_dir():
                shutil.copytree(source_dir, target_dir)
                typer.echo(f"Copied {dir_name}/")

    if not no_sync:
        typer.echo("Running uv sync...")
        try:
            uv(
                "sync",
                "--all-groups",
                "--all-extras",
                _cwd=str(new_worktree_path),
                _tty_out=False,
            )
            typer.echo("Dependencies synced")
        except sh.ErrorReturnCode as e:
            typer.echo(f"Warning: uv sync failed: {e.stderr.decode()}", err=True)

    if not no_plugin_refresh:
        if PLUGIN_CACHE_DIR.exists():
            shutil.rmtree(PLUGIN_CACHE_DIR)
            typer.echo("Cleared plugin cache (aib-workflow)")

        claude = sh.Command("claude")
        try:
            claude(
                "plugin",
                "install",
                "aib-workflow@local",
                "--scope",
                "project",
                _cwd=str(new_worktree_path),
                _tty_out=False,
            )
            typer.echo("Installed aib-workflow plugin (project scope)")
        except sh.ErrorReturnCode as e:
            typer.echo(f"Warning: plugin install failed: {e.stderr.decode()}", err=True)

    typer.echo()
    cd_command = f"cd /; cd {new_worktree_path}; claude"

    try:
        xclip = sh.Command("xclip")
        xclip("-selection", "clipboard", _in=cd_command)
        typer.echo(f"Done! Copied to clipboard: {cd_command}")
    except (sh.CommandNotFound, sh.ErrorReturnCode):
        typer.echo("Done! To switch to the new worktree:")
        typer.echo(f"  {cd_command}")


# ---------------------------------------------------------------------------
# Version tagging
# ---------------------------------------------------------------------------

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


@app.command("version-bump")
def version_bump(
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
    typer.echo(f"Bumped {old_version} -> {new_version} ({level})")

    version_changelog(new_version, summary, details)


@app.command("version-tag")
def version_tag(
    commit: str = typer.Option("HEAD", "--commit", "-c", help="Commit to tag"),
    message: str = typer.Option("", "--message", "-m", help="Tag message"),
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
        short_hash = str(_git("rev-parse", "--short", commit)).strip()
        commit_msg = str(_git("log", "--format=%s", "-1", commit)).strip()
        message = f"Agent version {version} at {short_hash}: {commit_msg}"

    force_flag = ["-f"] if force else []
    _git("tag", *force_flag, "-a", tag_name, commit, "-m", message)
    typer.echo(f"Created tag {tag_name} at {commit}")


@app.command("version-list")
def version_list() -> None:
    """List all agent version tags with dates."""
    tags = _get_existing_tags()
    if not tags:
        typer.echo("No version tags found.")
        return

    for tag_name in sorted(
        tags, key=lambda t: [int(x) for x in t.lstrip("v").split(".")]
    ):
        try:
            date = str(_git("log", "-1", "--format=%ai", tag_name, "--")).strip()[:10]
            msg = str(_git("tag", "-l", "-n1", tag_name)).strip()
            typer.echo(f"  {msg:60s}  ({date})")
        except sh.ErrorReturnCode:
            typer.echo(f"  {tag_name}")


@app.command("version-history")
def version_history() -> None:
    """Show version bumps from git history."""
    try:
        log = str(_git("log", "--all", "--oneline", "--", "src/aib/version.py"))
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
        except typer.BadParameter:
            typer.echo(f"  {commit_hash}  ???       {line.split(' ', 1)[1]}")


@app.command("version-changelog")
def version_changelog(
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
