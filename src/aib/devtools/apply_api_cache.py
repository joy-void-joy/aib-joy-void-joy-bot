#!/usr/bin/env python3
"""Apply resolution and CP data from locally cached API responses.

Reads individual post JSONs from a cache file (downloaded via browser)
and updates forecast JSONs with resolution values and CP data. Avoids
all Metaculus API calls.

Usage:
    # Apply from a combined JSON file (array of post objects):
    uv run python .claude/plugins/aib/scripts/apply_api_cache.py apply minibench_posts.json

    # Apply from a directory of individual JSON files:
    uv run python .claude/plugins/aib/scripts/apply_api_cache.py apply data/api_cache/

    # Show what would change without modifying files:
    uv run python .claude/plugins/aib/scripts/apply_api_cache.py apply minibench_posts.json --dry-run

    # Just show resolution + CP summary from cached data:
    uv run python .claude/plugins/aib/scripts/apply_api_cache.py inspect minibench_posts.json
"""

import json
from datetime import datetime
from pathlib import Path

import typer

from aib.agent.history import update_forecast_file
from aib.paths import iter_forecast_dirs, iter_retrodict_dirs

app = typer.Typer(help="Apply cached API data to forecast files")


def load_cache(source: str) -> list[dict]:
    """Load cached post data from a file or directory.

    Supports:
    - A JSON file containing an array of post objects
    - A JSON file with {"results": [...]} (listing endpoint format)
    - A directory of individual {post_id}.json files
    """
    path = Path(source)

    if path.is_dir():
        posts = []
        for f in sorted(path.glob("*.json")):
            data = json.loads(f.read_text())
            if "id" in data:
                posts.append(data)
            elif "results" in data:
                posts.extend(data["results"])
        return posts

    data = json.loads(path.read_text())
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "results" in data:
        return data["results"]
    if isinstance(data, dict) and "id" in data:
        return [data]

    typer.echo(f"Unrecognized format in {source}")
    raise typer.Exit(1)


def extract_resolution(post: dict) -> str | float | None:
    """Extract typed resolution from a post's question data."""
    question = post.get("question") or {}
    resolution = question.get("resolution")
    if resolution is None:
        return None

    q_type = question.get("type")
    if q_type == "binary":
        if resolution in (1.0, 1, "yes"):
            return "yes"
        elif resolution in (0.0, 0, "no"):
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


def extract_cp(post: dict) -> float | None:
    """Extract community prediction from a post's aggregation data.

    Checks both recency_weighted (/api/posts/) and unweighted (/api2/) formats.
    """
    question = post.get("question") or {}
    if question.get("type") != "binary":
        return None

    aggregations = question.get("aggregations") or {}

    for method in ("recency_weighted", "unweighted"):
        agg = aggregations.get(method) or {}
        latest = agg.get("latest") or {}

        centers = latest.get("centers")
        if centers and len(centers) > 0:
            return float(centers[0])

        forecast_values = latest.get("forecast_values")
        if forecast_values and len(forecast_values) > 1:
            return float(forecast_values[1])

    return None


@app.command()
def apply(
    source: str = typer.Argument(..., help="Path to cached JSON file or directory"),
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Show changes without applying"
    ),
) -> None:
    """Apply resolution and CP data from cached API responses to forecast files."""
    posts = load_cache(source)
    typer.echo(f"Loaded {len(posts)} posts from {source}")

    resolution_applied = 0
    resolution_skipped = 0
    already_set = 0
    cp_found = 0
    no_resolution = 0
    no_forecast = 0

    cp_data: dict[str, dict] = {}

    for post in posts:
        post_id = post.get("id")
        if post_id is None:
            continue

        # Extract resolution
        resolution = extract_resolution(post)
        title = (post.get("question") or {}).get("title", post.get("title", "?"))[:60]

        if resolution is None:
            no_resolution += 1
            continue

        # Extract CP
        cp = extract_cp(post)
        if cp is not None:
            cp_data[str(post_id)] = {
                "cp": cp,
                "fetched_at": datetime.now().isoformat(),
                "question_status": (post.get("question") or {}).get(
                    "status", "unknown"
                ),
            }
            cp_found += 1

        # Find matching forecast directories
        found_any = False
        post_dirs = list(iter_forecast_dirs(post_id))
        post_dirs.extend(iter_retrodict_dirs(post_id))
        for post_dir in post_dirs:
            found_any = True

            for f in post_dir.glob("*.json"):
                data = json.loads(f.read_text())
                if data.get("resolution") == resolution:
                    already_set += 1
                    continue

                if dry_run:
                    typer.echo(f"  Would set {post_id} ({title}) → {resolution}")
                    resolution_applied += 1
                else:
                    if update_forecast_file(f, resolution):
                        resolution_applied += 1
                    else:
                        resolution_skipped += 1

        if not found_any:
            no_forecast += 1

    # Save CP cache for feedback_collect.py
    if cp_data and not dry_run:
        feedback_path = Path("./notes/feedback_loop") / _get_branch()
        feedback_path.mkdir(parents=True, exist_ok=True)
        state_file = feedback_path / "feedback_state.json"

        if state_file.exists():
            state = json.loads(state_file.read_text())
        else:
            state = {"cp_cache": {}}

        if "cp_cache" not in state:
            state["cp_cache"] = {}

        state["cp_cache"].update(cp_data)
        state_file.write_text(json.dumps(state, indent=2))
        typer.echo(f"\nUpdated CP cache with {len(cp_data)} entries in {state_file}")

    typer.echo(f"\n{'DRY RUN - ' if dry_run else ''}Results:")
    typer.echo(f"  Resolutions applied: {resolution_applied}")
    typer.echo(f"  Already correct:     {already_set}")
    typer.echo(f"  No resolution in API: {no_resolution}")
    typer.echo(f"  No forecast found:   {no_forecast}")
    typer.echo(f"  CP values cached:    {cp_found}")

    if dry_run:
        typer.echo("\n(No files were modified)")


@app.command()
def inspect(
    source: str = typer.Argument(..., help="Path to cached JSON file or directory"),
) -> None:
    """Show resolution and CP data from cached API responses."""
    posts = load_cache(source)

    for post in posts:
        post_id = post.get("id")
        q = post.get("question") or {}
        title = q.get("title", post.get("title", "?"))[:60]
        q_type = q.get("type", "?")
        resolution = extract_resolution(post)
        cp = extract_cp(post)

        # Check if we have a forecast for this
        has_forecast = any(True for _ in iter_forecast_dirs(post_id)) or any(
            True for _ in iter_retrodict_dirs(post_id)
        )

        marker = "*" if has_forecast else " "
        res_str = str(resolution) if resolution is not None else "unresolved"
        cp_str = f"CP={cp:.1%}" if cp is not None else ""

        typer.echo(
            f"  {marker} [{post_id}] ({q_type:8s}) {res_str:>10s}  {cp_str:>10s}  {title}"
        )

    typer.echo(f"\n  * = has forecast  ({len(posts)} posts total)")


def _get_branch() -> str:
    """Get current git branch."""
    import sh

    git = sh.Command("git")
    try:
        return str(git("branch", "--show-current")).strip() or "main"
    except Exception:
        return "main"


if __name__ == "__main__":
    app()
