"""Fetch resolutions from Metaculus and update saved forecasts.

Scans both live forecasts (notes/forecasts/) and retrodictions (notes/retrodict/).
Uses batch tournament listing to minimize API calls.
"""

import asyncio
import json
from pathlib import Path

import typer

from aib.clients.metaculus import get_client

app = typer.Typer(no_args_is_help=True)

FORECASTS_PATH = Path("./notes/forecasts")
RETRODICT_PATH = Path("./notes/retrodict")

TOURNAMENT_IDS = [
    32916,  # AIB Spring 2026
    32715,  # MiniBench
    32585,  # Metaculus Cup
]


def get_resolution(question_data: dict) -> str | float | None:
    """Extract resolution from question data."""
    question = question_data.get("question", {})
    if not question:
        return None

    resolution = question.get("resolution")
    if resolution is None:
        return None

    q_type = question.get("type")
    if q_type == "binary":
        if resolution == 1.0:
            return "yes"
        elif resolution == 0.0:
            return "no"
        else:
            return "ambiguous"

    if q_type in ("numeric", "discrete"):
        if (
            isinstance(resolution, str)
            and not resolution.replace(".", "").replace("-", "").isdigit()
        ):
            return resolution
        return float(resolution)

    if q_type == "multiple_choice":
        return str(resolution)

    return str(resolution) if resolution is not None else None


def update_forecast_file(filepath: Path, resolution: str | float) -> bool:
    """Update a forecast file with resolution."""
    try:
        data = json.loads(filepath.read_text())
        if data.get("resolution") == resolution:
            return False
        data["resolution"] = resolution
        filepath.write_text(json.dumps(data, indent=2))
        return True
    except (json.JSONDecodeError, OSError) as e:
        typer.echo(f"  Error updating {filepath}: {e}")
        return False


def find_unresolved(base_path: Path) -> list[dict]:
    """Find all forecast files without resolution in a directory tree."""
    unresolved: list[dict] = []
    if not base_path.exists():
        return unresolved
    for post_dir in base_path.iterdir():
        if not post_dir.is_dir():
            continue
        for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
            try:
                data = json.loads(forecast_file.read_text())
                if data.get("resolution") is None:
                    unresolved.append(
                        {
                            "post_id": data.get("post_id") or int(post_dir.name),
                            "file": forecast_file,
                            "dir": post_dir,
                            "title": data.get("question_title", "Unknown")[:50],
                        }
                    )
            except (json.JSONDecodeError, OSError, ValueError):
                continue
    return unresolved


async def batch_fetch_resolved_ids(
    tournament_ids: list[int],
) -> set[int]:
    """Fetch post IDs of all resolved questions from tournaments."""
    resolved_ids: set[int] = set()

    mc = get_client()
    for tid in tournament_ids:
        offset = 0
        limit = 100
        while True:
            results = await mc.fetch_posts_list(
                {
                    "order_by": "-resolve_time",
                    "status": "resolved",
                    "tournaments": tid,
                    "offset": offset,
                    "limit": limit,
                }
            )

            if not results:
                break

            for item in results:
                post_id = item.get("id")
                if post_id is not None:
                    resolved_ids.add(post_id)

            if len(results) < limit:
                break
            offset += limit

    return resolved_ids


@app.command("check")
def check(
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Don't update files"),
) -> None:
    """Check for and apply resolution updates (live + retrodict)."""
    unresolved = find_unresolved(FORECASTS_PATH) + find_unresolved(RETRODICT_PATH)

    if not unresolved:
        typer.echo("All forecasts already have resolutions")
        return

    unresolved_ids = {item["post_id"] for item in unresolved}
    typer.echo(f"Found {len(unresolved)} unresolved forecasts")

    async def check_all() -> tuple[int, int]:
        updated = 0
        still_open = 0

        typer.echo("Batch-fetching resolved question IDs from tournaments...")
        resolved_ids = await batch_fetch_resolved_ids(TOURNAMENT_IDS)
        typer.echo(f"  Found {len(resolved_ids)} resolved questions across tournaments")

        needs_fetch = unresolved_ids & resolved_ids
        skipped = unresolved_ids - resolved_ids
        typer.echo(
            f"  {len(needs_fetch)} of our forecasts have resolved, "
            f"{len(skipped)} still open (skipping)"
        )
        still_open = len(skipped)

        if not needs_fetch:
            typer.echo("  No new resolutions to apply")
            return updated, still_open

        items_by_id = {item["post_id"]: item for item in unresolved}

        typer.echo(f"\nFetching resolution values for {len(needs_fetch)} questions...")
        client = get_client()
        for post_id in sorted(needs_fetch):
            typer.echo(f"  Fetching {post_id}...")
            try:
                question_data = await client.fetch_post_json(post_id)
            except (OSError, ValueError) as e:
                typer.echo(f"    Error: {e}")
                continue

            resolution = get_resolution(question_data)
            if resolution is not None:
                typer.echo(f"    Resolved: {resolution}")
                if not dry_run:
                    post_dir = items_by_id[post_id]["dir"]
                    for f in post_dir.glob("*.json"):
                        if update_forecast_file(f, resolution):
                            updated += 1
                else:
                    updated += 1

            await asyncio.sleep(2.0)

        return updated, still_open

    updated, still_open = asyncio.run(check_all())

    typer.echo("\nResults:")
    typer.echo(f"  Updated: {updated} files")
    typer.echo(f"  Still open: {still_open}")
    if dry_run:
        typer.echo("  (dry run - no files changed)")


@app.command("status")
def status() -> None:
    """Show resolution status of all forecasts (live + retrodict)."""
    resolved_yes = 0
    resolved_no = 0
    resolved_other = 0
    unresolved = 0

    for base in (FORECASTS_PATH, RETRODICT_PATH):
        if not base.exists():
            continue
        for post_dir in base.iterdir():
            if not post_dir.is_dir():
                continue
            for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
                try:
                    data = json.loads(forecast_file.read_text())
                    resolution = data.get("resolution")
                    if resolution == "yes":
                        resolved_yes += 1
                    elif resolution == "no":
                        resolved_no += 1
                    elif resolution is not None:
                        resolved_other += 1
                    else:
                        unresolved += 1
                except (json.JSONDecodeError, OSError):
                    continue

    total = resolved_yes + resolved_no + resolved_other + unresolved

    typer.echo(f"\n=== Resolution Status ({total} forecasts) ===\n")
    typer.echo(f"Resolved YES:   {resolved_yes}")
    typer.echo(f"Resolved NO:    {resolved_no}")
    typer.echo(f"Resolved other: {resolved_other}")
    typer.echo(f"Unresolved:     {unresolved}")


@app.command("set")
def set_resolution(
    post_id: int = typer.Argument(..., help="Post ID"),
    resolution: str = typer.Argument(
        ..., help="Resolution value (yes/no/ambiguous/value)"
    ),
) -> None:
    """Manually set resolution for a forecast."""
    updated = 0
    for base in (FORECASTS_PATH, RETRODICT_PATH):
        post_dir = base / str(post_id)
        if post_dir.exists():
            for f in post_dir.glob("*.json"):
                if update_forecast_file(f, resolution):
                    updated += 1

    if updated == 0:
        typer.echo(f"No forecasts found for post {post_id}")
        raise typer.Exit(1)

    typer.echo(f"Updated {updated} forecast files for post {post_id}")
