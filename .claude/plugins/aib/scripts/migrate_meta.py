#!/usr/bin/env python3
"""Migrate meta-reflection files from notes/meta/ to notes/sessions/<session_id>/.

Matches each meta file to its corresponding forecast by post_id and timestamp,
then moves it to the session directory.

Session ID format: <post_id>_<forecast_timestamp>
"""

import re
import shutil
from datetime import datetime
from pathlib import Path

import typer

app = typer.Typer(help="Migrate meta files to session directories")

META_PATH = Path("./notes/meta")
FORECASTS_PATH = Path("./notes/forecasts")
SESSIONS_PATH = Path("./notes/sessions")


def extract_post_id_from_meta(filepath: Path) -> int | None:
    """Extract post_id from meta filename or content.

    Filename patterns:
    - 20260202_143000_q41604_sinners_oscars.md -> 41604
    - 20260202_143000_q91_trump_nyc_funding.md -> 91

    Content patterns:
    - **Post ID**: 41604
    - **Question ID:** 41604
    """
    # Try filename first
    match = re.search(r"_q(\d+)_", filepath.name)
    if match:
        return int(match.group(1))

    # Try content - various patterns
    try:
        content = filepath.read_text()
        # Look for Post ID or Question ID in various formats
        patterns = [
            r"\*\*(?:Post ID|Question ID)[:\*]*\s*(\d+)",
            r"Post ID[:\s]+(\d+)",
            r"Question ID[:\s]+(\d+)",
            r"post[_\s]?id[:\s]+(\d+)",
        ]
        for pattern in patterns:
            match = re.search(pattern, content, re.IGNORECASE)
            if match:
                return int(match.group(1))
    except Exception:
        pass

    return None


def extract_timestamp_from_meta(filepath: Path) -> str | None:
    """Extract timestamp from meta filename.

    Filename pattern: 20260202_143000_... -> 20260202_143000
    """
    match = re.match(r"(\d{8}_\d{6})", filepath.name)
    if match:
        return match.group(1)
    return None


def find_matching_forecast(
    post_id: int, meta_timestamp: str
) -> tuple[str, Path] | None:
    """Find the forecast that best matches this meta file.

    Returns (forecast_timestamp, forecast_path) or None.
    """
    forecast_dir = FORECASTS_PATH / str(post_id)
    if not forecast_dir.exists():
        return None

    forecasts = list(forecast_dir.glob("*.json"))
    if not forecasts:
        return None

    # Parse meta timestamp
    try:
        meta_dt = datetime.strptime(meta_timestamp, "%Y%m%d_%H%M%S")
    except ValueError:
        return None

    # Find closest forecast by timestamp
    best_match = None
    best_diff = None

    for forecast_path in forecasts:
        # Extract timestamp from forecast filename
        ts_match = re.match(r"(\d{8}_\d{6})", forecast_path.name)
        if not ts_match:
            continue

        try:
            forecast_dt = datetime.strptime(ts_match.group(1), "%Y%m%d_%H%M%S")
            diff = abs((forecast_dt - meta_dt).total_seconds())

            if best_diff is None or diff < best_diff:
                best_diff = diff
                best_match = (ts_match.group(1), forecast_path)
        except ValueError:
            continue

    return best_match


def get_session_dir(post_id: int, timestamp: str) -> Path:
    """Get session directory: notes/sessions/<post_id>/<timestamp>/."""
    return SESSIONS_PATH / str(post_id) / timestamp


@app.command()
def migrate(
    dry_run: bool = typer.Option(
        True,
        "--dry-run/--execute",
        help="Show what would be done without making changes",
    ),
    verbose: bool = typer.Option(False, "-v", "--verbose", help="Show detailed output"),
    include_unmatched: bool = typer.Option(
        True,
        "--include-unmatched/--skip-unmatched",
        help="Include files without post_id using filename as session",
    ),
) -> None:
    """Migrate meta files from notes/meta/ to notes/sessions/<post_id>/<timestamp>/."""

    if not META_PATH.exists():
        typer.echo("No notes/meta/ directory found")
        raise typer.Exit(1)

    meta_files = list(META_PATH.glob("*.md"))
    typer.echo(f"Found {len(meta_files)} meta files to migrate")

    migrated = 0
    skipped = []
    seen_destinations: set[Path] = set()

    for meta_file in sorted(meta_files):
        post_id = extract_post_id_from_meta(meta_file)
        meta_timestamp = extract_timestamp_from_meta(meta_file)

        if post_id and meta_timestamp:
            forecast_match = find_matching_forecast(post_id, meta_timestamp)
            if forecast_match:
                forecast_ts = forecast_match[0]
                session_dir = get_session_dir(post_id, forecast_ts)
            else:
                session_dir = get_session_dir(post_id, meta_timestamp)
                if verbose:
                    typer.echo(
                        f"  No forecast for {meta_file.name}, using meta timestamp"
                    )
        elif post_id:
            session_dir = get_session_dir(post_id, "unknown")
            if verbose:
                typer.echo(f"  No timestamp for {meta_file.name}")
        elif include_unmatched:
            session_dir = SESSIONS_PATH / "unmatched" / meta_file.stem
            if verbose:
                typer.echo(f"  No post_id for {meta_file.name}, storing in unmatched/")
        else:
            skipped.append((meta_file, "no post_id found"))
            continue

        dest_path = session_dir / "meta.md"

        # Handle collisions: if meta.md already exists or already targeted
        if dest_path.exists() or dest_path in seen_destinations:
            dest_path = session_dir / f"meta_{meta_file.stem}.md"
            if verbose or dry_run:
                typer.echo(f"  Collision! Using {dest_path.name}")

        seen_destinations.add(dest_path)

        if verbose or dry_run:
            typer.echo(f"{meta_file.name} -> {dest_path}")

        if not dry_run:
            session_dir.mkdir(parents=True, exist_ok=True)
            shutil.move(str(meta_file), str(dest_path))
            migrated += 1

    # Report results
    typer.echo("")
    if dry_run:
        typer.echo(f"DRY RUN: Would migrate {len(meta_files) - len(skipped)} files")
        typer.echo("Run with --execute to perform migration")
    else:
        typer.echo(f"Migrated {migrated} files")

    if skipped:
        typer.echo(f"\nSkipped files ({len(skipped)}):")
        for meta_file, reason in skipped:
            typer.echo(f"  {meta_file.name}: {reason}")


@app.command()
def check() -> None:
    """Check which meta files can be matched to forecasts."""

    if not META_PATH.exists():
        typer.echo("No notes/meta/ directory found")
        raise typer.Exit(1)

    meta_files = list(META_PATH.glob("*.md"))

    matched = 0
    unmatched = 0

    for meta_file in sorted(meta_files):
        post_id = extract_post_id_from_meta(meta_file)
        meta_timestamp = extract_timestamp_from_meta(meta_file)

        if not post_id or not meta_timestamp:
            typer.echo(f"✗ {meta_file.name}: missing post_id or timestamp")
            unmatched += 1
            continue

        forecast_match = find_matching_forecast(post_id, meta_timestamp)

        if forecast_match:
            forecast_ts = forecast_match[0]
            diff = abs(
                (
                    datetime.strptime(forecast_ts, "%Y%m%d_%H%M%S")
                    - datetime.strptime(meta_timestamp, "%Y%m%d_%H%M%S")
                ).total_seconds()
            )
            typer.echo(
                f"✓ {meta_file.name} -> post {post_id}, forecast {forecast_ts} (diff: {diff:.0f}s)"
            )
            matched += 1
        else:
            typer.echo(f"? {meta_file.name}: post_id {post_id} has no forecasts")
            unmatched += 1

    typer.echo(f"\nMatched: {matched}, Unmatched: {unmatched}")


if __name__ == "__main__":
    app()
