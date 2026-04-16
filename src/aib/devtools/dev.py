"""Development tools: worktree management and plugin versioning."""

import json
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

PLUGIN_DIR = Path(".claude/plugins/aib")
PLUGIN_JSON = PLUGIN_DIR / ".claude-plugin" / "plugin.json"
PLUGIN_CHANGELOG = PLUGIN_DIR / "CHANGELOG.md"
PLUGIN_VERSION_RE = re.compile(r'"version"\s*:\s*"([^"]+)"')

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
# Plugin versioning
# ---------------------------------------------------------------------------


def get_plugin_version() -> str:
    """Read current version from plugin.json."""
    data = json.loads(PLUGIN_JSON.read_text())
    return data["version"]


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


def _write_plugin_version(new_version: str) -> None:
    content = PLUGIN_JSON.read_text()
    updated = PLUGIN_VERSION_RE.sub(f'"version": "{new_version}"', content)
    PLUGIN_JSON.write_text(updated)


def _write_plugin_changelog(
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

    changelog_version_re = re.compile(r"^## v(\d+\.\d+\.\d+)\s+\((\d{4}-\d{2}-\d{2})\)")

    if PLUGIN_CHANGELOG.exists():
        content = PLUGIN_CHANGELOG.read_text()
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
            PLUGIN_CHANGELOG.write_text(content)
            typer.echo(f"Updated plugin changelog for v{version_clean}")
        else:
            lines = content.splitlines(keepends=True)
            insert_idx = 0
            for i, line in enumerate(lines):
                if changelog_version_re.match(line):
                    insert_idx = i
                    break
            else:
                insert_idx = len(lines)
            lines.insert(insert_idx, new_entry)
            PLUGIN_CHANGELOG.write_text("".join(lines))
            typer.echo(f"Added plugin changelog for v{version_clean}")
    else:
        content = (
            f"# Plugin Changelog\n\naib-workflow plugin version history.\n\n{new_entry}"
        )
        PLUGIN_CHANGELOG.write_text(content)
        typer.echo(f"Created plugin CHANGELOG.md with entry for v{version_clean}")


@app.command("plugin-bump")
def plugin_bump_cmd(
    level: str = typer.Argument(help="Bump level: patch, minor, or major"),
    summary: str = typer.Argument(help="One-line summary of what changed"),
    details: Optional[str] = typer.Option(
        None, "--detail", "-d", help="Additional detail (comma-separated)"
    ),
) -> None:
    """Bump plugin version and update plugin changelog."""
    if level not in ("patch", "minor", "major"):
        typer.echo(f"Invalid level '{level}'. Must be: patch, minor, major")
        raise typer.Exit(1)

    if not PLUGIN_JSON.exists():
        typer.echo(f"Error: {PLUGIN_JSON} not found", err=True)
        raise typer.Exit(1)

    old_version = get_plugin_version()
    new_version = _increment_version(old_version, level)

    _write_plugin_version(new_version)
    typer.echo(f"Plugin: {old_version} -> {new_version} ({level})")

    _write_plugin_changelog(new_version, summary, details)

    if PLUGIN_CACHE_DIR.exists():
        shutil.rmtree(PLUGIN_CACHE_DIR)
        typer.echo("Cleared plugin cache (reinstall to pick up changes)")


@app.command("plugin-version")
def plugin_version_cmd() -> None:
    """Display the current plugin version."""
    if not PLUGIN_JSON.exists():
        typer.echo(f"Error: {PLUGIN_JSON} not found", err=True)
        raise typer.Exit(1)
    typer.echo(f"v{get_plugin_version()}")
