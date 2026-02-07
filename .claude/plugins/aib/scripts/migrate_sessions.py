#!/usr/bin/env python3
"""Archive old session directories.

Moves notes/sessions/<post_id>_<timestamp>/ to notes/archive/sessions/
These are old meta-reflections that shouldn't be accessible to the agent.
"""

import re
import shutil
from pathlib import Path

import typer

app = typer.Typer()

SESSIONS_PATH = Path("notes/sessions")
ARCHIVE_PATH = Path("notes/archive/sessions")

# Match old format: <post_id>_<timestamp> or just <post_id>
OLD_FORMAT_PATTERN = re.compile(r"^(\d+)_(.+)$")  # post_id_timestamp
BARE_ID_PATTERN = re.compile(r"^\d+$")  # just post_id (no timestamp)


@app.command()
def archive(
    dry_run: bool = typer.Option(
        True, "--dry-run/--execute", help="Show what would be archived"
    ),
    delete: bool = typer.Option(False, "--delete", help="Delete instead of archive"),
) -> None:
    """Archive or delete old session directories."""
    if not SESSIONS_PATH.exists():
        typer.echo(f"Sessions directory not found: {SESSIONS_PATH}")
        raise typer.Exit(1)

    to_archive: list[Path] = []

    for session_dir in sorted(SESSIONS_PATH.iterdir()):
        if not session_dir.is_dir():
            continue

        name = session_dir.name

        # Check if in old flat format
        if OLD_FORMAT_PATTERN.match(name) or BARE_ID_PATTERN.match(name):
            to_archive.append(session_dir)
        else:
            typer.echo(f"  [skip] {name} (not old format)")

    if not to_archive:
        typer.echo("No old directories found.")
        return

    action = "delete" if delete else "archive"
    typer.echo(
        f"\n{'Would ' + action if dry_run else action.title() + 'ing'} {len(to_archive)} directories:\n"
    )

    if not delete and not dry_run:
        ARCHIVE_PATH.mkdir(parents=True, exist_ok=True)

    for old_path in to_archive:
        if dry_run:
            typer.echo(f"  {old_path.name}")
        elif delete:
            shutil.rmtree(old_path)
            typer.echo(f"  [deleted] {old_path.name}")
        else:
            new_path = ARCHIVE_PATH / old_path.name
            old_path.rename(new_path)
            typer.echo(
                f"  [archived] {old_path.name} -> {new_path.relative_to(Path('notes'))}"
            )

    if dry_run:
        typer.echo(f"\nRun with --execute to {action}.")
    else:
        typer.echo(f"\n{action.title()}d {len(to_archive)} directories.")


if __name__ == "__main__":
    app()
