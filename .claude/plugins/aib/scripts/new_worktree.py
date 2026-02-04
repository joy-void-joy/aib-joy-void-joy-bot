#!/usr/bin/env python3
"""
Create a new worktree with Claude session migration.

This script:
1. Creates a new git worktree branching from the current branch
2. Runs uv sync in the new worktree
3. Migrates the most recent Claude session to the new worktree

Usage:
    uv run python .claude/scripts/new_worktree.py <worktree-name>

Examples:
    uv run python .claude/scripts/new_worktree.py my-feature
    uv run python .claude/scripts/new_worktree.py fix-bug --session-id abc123
"""

import json
import shutil
from pathlib import Path

import sh
import typer

app = typer.Typer(help="Create a new worktree with Claude session migration")


def path_to_project_dir(path: Path) -> str:
    """Convert a filesystem path to Claude's project directory name format.

    Claude Code converts paths by replacing both / and . with -, and keeps
    the leading dash.
    """
    return str(path.resolve()).replace("/", "-").replace(".", "-")


def get_claude_projects_dir() -> Path:
    """Get the Claude projects directory."""
    return Path.home() / ".claude" / "projects"


def get_tree_dir() -> Path:
    """Get the tree directory that contains worktrees."""
    cwd = Path.cwd().resolve()

    # Check if we're in a worktree (has .git file pointing to worktree dir)
    git_path = cwd / ".git"
    if git_path.exists() and git_path.is_file():
        # We're in a worktree, go up to tree/ directory
        if cwd.parent.name == "tree":
            return cwd.parent

    # Check if we're directly in a tree/ directory
    if cwd.name == "tree":
        return cwd

    # Check if parent is the bare repo and has a tree/ subdirectory
    for parent in cwd.parents:
        tree_dir = parent / "tree"
        if tree_dir.exists() and tree_dir.is_dir():
            return tree_dir

    typer.echo(f"Error: Could not find tree/ directory from {cwd}", err=True)
    raise typer.Exit(1)


def get_most_recent_session(project_dir: Path) -> dict | None:
    """Get the most recently modified session from a project directory."""
    if not project_dir.exists():
        return None

    # First try sessions-index.json
    index_path = project_dir / "sessions-index.json"
    if index_path.exists():
        with open(index_path) as f:
            index = json.load(f)
        entries = index.get("entries", [])
        if entries:
            # Sort by modified time, most recent first
            sorted_entries = sorted(
                entries, key=lambda e: e.get("modified", ""), reverse=True
            )
            return sorted_entries[0]

    # Fallback: find most recent .jsonl file
    jsonl_files = list(project_dir.glob("*.jsonl"))
    if not jsonl_files:
        return None

    most_recent = max(jsonl_files, key=lambda f: f.stat().st_mtime)
    session_id = most_recent.stem

    return {
        "sessionId": session_id,
        "fullPath": str(most_recent),
        "summary": "Session (from file)",
    }


GITIGNORED_DATA_DIRS = ["logs"]


@app.command()
def create(
    name: str = typer.Argument(..., help="Name for the new worktree/branch"),
    session_id: str | None = typer.Option(
        None,
        "--session-id",
        "-s",
        help="Specific session ID to migrate (default: most recent)",
    ),
    no_sync: bool = typer.Option(False, "--no-sync", help="Skip running uv sync"),
    no_session: bool = typer.Option(
        False, "--no-session", help="Skip session migration"
    ),
    copy_data: bool = typer.Option(
        True,
        "--copy-data/--no-copy-data",
        help="Copy gitignored data directories (notes/, logs/) to new worktree",
    ),
) -> None:
    """Create a new worktree and migrate Claude session."""
    cwd = Path.cwd().resolve()
    tree_dir = get_tree_dir()
    new_worktree_path = tree_dir / name

    if new_worktree_path.exists():
        typer.echo(f"Error: {new_worktree_path} already exists", err=True)
        raise typer.Exit(1)

    git = sh.Command("git")
    uv = sh.Command("uv")

    # Get current branch name
    try:
        current_branch = str(git("branch", "--show-current", _tty_out=False)).strip()
    except sh.ErrorReturnCode:
        typer.echo("Error: Could not determine current branch", err=True)
        raise typer.Exit(1)

    branch_name = name if "/" in name else name

    typer.echo(f"Creating worktree '{name}' from branch '{current_branch}'...")
    typer.echo(f"  Location: {new_worktree_path}")
    typer.echo(f"  New branch: {branch_name}")
    typer.echo()

    # Create the worktree with a new branch
    try:
        git(
            "worktree", "add", str(new_worktree_path), "-b", branch_name, _tty_out=False
        )
        typer.echo("✓ Worktree created")
    except sh.ErrorReturnCode as e:
        typer.echo(f"Error creating worktree: {e.stderr.decode()}", err=True)
        raise typer.Exit(1)

    # Copy .env.local if it exists
    env_local = cwd / ".env.local"
    if env_local.exists():
        shutil.copy2(env_local, new_worktree_path / ".env.local")
        typer.echo("✓ Copied .env.local")

    # Copy gitignored data directories (notes/, logs/)
    if copy_data:
        for dir_name in GITIGNORED_DATA_DIRS:
            source_dir = cwd / dir_name
            target_dir = new_worktree_path / dir_name
            if source_dir.exists() and source_dir.is_dir():
                shutil.copytree(source_dir, target_dir)
                typer.echo(f"✓ Copied {dir_name}/")

    # Run uv sync in the new worktree
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
            typer.echo("✓ Dependencies synced")
        except sh.ErrorReturnCode as e:
            typer.echo(f"Warning: uv sync failed: {e.stderr.decode()}", err=True)

    # Migrate Claude session
    if not no_session:
        projects_dir = get_claude_projects_dir()
        source_project_name = path_to_project_dir(cwd)
        target_project_name = path_to_project_dir(new_worktree_path)

        source_project_dir = projects_dir / source_project_name
        target_project_dir = projects_dir / target_project_name

        # Find session to migrate
        if session_id:
            session = {"sessionId": session_id}
            source_jsonl = source_project_dir / f"{session_id}.jsonl"
            if not source_jsonl.exists():
                typer.echo(f"Warning: Session {session_id} not found", err=True)
                session = None
        else:
            session = get_most_recent_session(source_project_dir)

        if session:
            sid = session["sessionId"]
            typer.echo(f"Migrating session: {session.get('summary', sid)[:50]}...")

            # Create target project directory
            target_project_dir.mkdir(parents=True, exist_ok=True)

            # Copy session jsonl
            source_jsonl = source_project_dir / f"{sid}.jsonl"
            target_jsonl = target_project_dir / f"{sid}.jsonl"

            if source_jsonl.exists():
                shutil.copy2(source_jsonl, target_jsonl)

            # Copy session subdirectory if exists
            source_session_dir = source_project_dir / sid
            target_session_dir = target_project_dir / sid

            if source_session_dir.exists() and source_session_dir.is_dir():
                if target_session_dir.exists():
                    shutil.rmtree(target_session_dir)
                shutil.copytree(source_session_dir, target_session_dir)

            # Create/update sessions-index.json
            target_index_path = target_project_dir / "sessions-index.json"
            if target_index_path.exists():
                with open(target_index_path) as f:
                    target_index = json.load(f)
            else:
                target_index = {
                    "version": 1,
                    "entries": [],
                    "originalPath": str(new_worktree_path),
                }

            # Create new entry with updated paths
            new_entry = session.copy()
            new_entry["fullPath"] = str(target_jsonl)
            new_entry["projectPath"] = str(new_worktree_path)
            new_entry["gitBranch"] = branch_name

            # Check if session already exists
            existing_ids = {e["sessionId"] for e in target_index.get("entries", [])}
            if sid not in existing_ids:
                target_index["entries"].append(new_entry)
                with open(target_index_path, "w") as f:
                    json.dump(target_index, f, indent=2)

            typer.echo("✓ Session migrated")
        else:
            typer.echo("No session to migrate (none found in source)")

    typer.echo()
    cd_command = f"cd {new_worktree_path}"

    # Try to copy to clipboard
    try:
        xclip = sh.Command("xclip")
        xclip("-selection", "clipboard", _in=cd_command)
        typer.echo(f"Done! Copied to clipboard: {cd_command}")
    except (sh.CommandNotFound, sh.ErrorReturnCode):
        typer.echo("Done! To switch to the new worktree:")
        typer.echo(f"  {cd_command}")

    typer.echo()
    typer.echo("Then start Claude Code to continue with the migrated session:")
    typer.echo("  claude --resume")


if __name__ == "__main__":
    app()
