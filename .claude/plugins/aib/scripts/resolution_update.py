#!/usr/bin/env python3
"""Fetch resolutions from Metaculus and update saved forecasts.

Queries Metaculus API for resolved questions and updates the
corresponding saved forecasts with resolution outcomes.
"""

import asyncio
import json
from pathlib import Path

import httpx
import typer

app = typer.Typer(help="Update forecasts with resolution data")

FORECASTS_PATH = Path("./notes/forecasts")
METACULUS_API = "https://www.metaculus.com/api"


async def fetch_question(post_id: int) -> dict | None:
    """Fetch question data from Metaculus API."""
    url = f"{METACULUS_API}/posts/{post_id}/"
    async with httpx.AsyncClient(timeout=30) as client:
        try:
            resp = await client.get(url)
            if resp.status_code == 200:
                return resp.json()
        except Exception as e:
            typer.echo(f"  Error fetching {post_id}: {e}")
    return None


def get_resolution(question_data: dict) -> str | None:
    """Extract resolution from question data.

    Returns: 'yes', 'no', 'ambiguous', or None if unresolved.
    """
    # Check if resolved
    question = question_data.get("question", {})
    if not question:
        return None

    resolution = question.get("resolution")
    if resolution is None:
        return None

    # Binary questions: 1.0 = yes, 0.0 = no
    q_type = question.get("type")
    if q_type == "binary":
        if resolution == 1.0:
            return "yes"
        elif resolution == 0.0:
            return "no"
        else:
            return "ambiguous"

    # Numeric/discrete: resolution is the actual value
    if q_type in ("numeric", "discrete"):
        return str(resolution)

    # Multiple choice: resolution is the option index or value
    if q_type == "multiple_choice":
        return str(resolution)

    return str(resolution) if resolution is not None else None


def update_forecast_file(filepath: Path, resolution: str) -> bool:
    """Update a forecast file with resolution."""
    try:
        data = json.loads(filepath.read_text())
        if data.get("resolution") == resolution:
            return False  # Already set
        data["resolution"] = resolution
        filepath.write_text(json.dumps(data, indent=2))
        return True
    except Exception as e:
        typer.echo(f"  Error updating {filepath}: {e}")
        return False


@app.command("check")
def check(
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Don't update files"),
) -> None:
    """Check for and apply resolution updates."""
    if not FORECASTS_PATH.exists():
        typer.echo("No forecasts directory found")
        raise typer.Exit(1)

    # Find all forecasts without resolution
    unresolved = []
    for post_dir in FORECASTS_PATH.iterdir():
        if not post_dir.is_dir():
            continue
        for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
            try:
                data = json.loads(forecast_file.read_text())
                if data.get("resolution") is None:
                    unresolved.append(
                        {
                            "post_id": int(post_dir.name),
                            "file": forecast_file,
                            "title": data.get("question_title", "Unknown")[:50],
                        }
                    )
            except Exception:
                continue

    if not unresolved:
        typer.echo("All forecasts already have resolutions")
        return

    typer.echo(f"Checking {len(unresolved)} unresolved forecasts...")

    async def check_all() -> tuple[int, int]:
        updated = 0
        still_open = 0

        for item in unresolved:
            post_id = item["post_id"]
            typer.echo(f"  Checking post {post_id}...")

            question_data = await fetch_question(post_id)
            if not question_data:
                continue

            resolution = get_resolution(question_data)
            if resolution:
                typer.echo(f"    Resolved: {resolution}")
                if not dry_run:
                    # Update all forecasts for this post
                    post_dir = FORECASTS_PATH / str(post_id)
                    for f in post_dir.glob("*.json"):
                        if update_forecast_file(f, resolution):
                            updated += 1
                else:
                    updated += 1
            else:
                still_open += 1

        return updated, still_open

    updated, still_open = asyncio.run(check_all())

    typer.echo("\nResults:")
    typer.echo(f"  Updated: {updated}")
    typer.echo(f"  Still open: {still_open}")
    if dry_run:
        typer.echo("  (dry run - no files changed)")


@app.command("status")
def status() -> None:
    """Show resolution status of all forecasts."""
    if not FORECASTS_PATH.exists():
        typer.echo("No forecasts directory found")
        raise typer.Exit(1)

    resolved_yes = 0
    resolved_no = 0
    resolved_other = 0
    unresolved = 0

    for post_dir in FORECASTS_PATH.iterdir():
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
            except Exception:
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
    resolution: str = typer.Argument(..., help="Resolution value (yes/no/ambiguous/value)"),
) -> None:
    """Manually set resolution for a forecast."""
    post_dir = FORECASTS_PATH / str(post_id)
    if not post_dir.exists():
        typer.echo(f"No forecasts found for post {post_id}")
        raise typer.Exit(1)

    updated = 0
    for f in post_dir.glob("*.json"):
        if update_forecast_file(f, resolution):
            updated += 1

    typer.echo(f"Updated {updated} forecast files for post {post_id}")


if __name__ == "__main__":
    app()
