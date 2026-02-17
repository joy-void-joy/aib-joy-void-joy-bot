"""Development tools: worktree management."""

import shutil
from pathlib import Path

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
