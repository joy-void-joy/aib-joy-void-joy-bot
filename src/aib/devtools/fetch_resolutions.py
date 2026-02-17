#!/usr/bin/env python3
"""Fetch resolution + CP data directly from /api2/ (unauthenticated).

Makes exactly 1 HTTP request per question. No auth token needed.
Saves results locally so downstream scripts (calibration_analysis,
scores_table, feedback_collect) can work entirely offline.

Usage:
    # Fetch resolutions for all unresolved minibench forecasts:
    uv run python .claude/plugins/aib/scripts/fetch_resolutions.py fetch --from-file minibench.json

    # Fetch resolutions for specific post IDs:
    uv run python .claude/plugins/aib/scripts/fetch_resolutions.py fetch --ids 41955,41960,41970

    # Fetch all unresolved forecasts (auto-detect from notes/forecasts/):
    uv run python .claude/plugins/aib/scripts/fetch_resolutions.py fetch

    # Apply cached results to forecast JSONs:
    uv run python .claude/plugins/aib/scripts/fetch_resolutions.py apply

    # Fetch and apply in one step:
    uv run python .claude/plugins/aib/scripts/fetch_resolutions.py fetch --apply
"""

import json
import logging
import time
from pathlib import Path

import httpx
import typer

app = typer.Typer(help="Fetch resolution + CP data from Metaculus (1 req/question)")
logger = logging.getLogger(__name__)

CACHE_DIR = Path("./data/api_cache")
FORECASTS_PATH = Path("./notes/forecasts")
RETRODICT_PATH = Path("./notes/retrodict")
OLD_API_BASE = "https://www.metaculus.com/api2/questions"


def get_unresolved_post_ids() -> list[int]:
    """Find post IDs of forecasts missing resolution data."""
    unresolved = []
    for base in (FORECASTS_PATH, RETRODICT_PATH):
        if not base.exists():
            continue
        for post_dir in base.iterdir():
            if not post_dir.is_dir() or not post_dir.name.isdigit():
                continue
            for f in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
                data = json.loads(f.read_text())
                if data.get("resolution") is None:
                    unresolved.append(int(post_dir.name))
    return sorted(set(unresolved))


def get_post_ids_from_file(filepath: str) -> list[int]:
    """Extract post IDs from a Metaculus API listing JSON."""
    data = json.loads(Path(filepath).read_text())
    results = data.get("results", data) if isinstance(data, dict) else data
    return sorted({r["id"] for r in results if "id" in r})


def extract_resolution(question: dict) -> str | float | None:
    """Extract typed resolution from /api2/ question data.

    The /api2/ endpoint returns resolution as "yes"/"no" strings for binary,
    while the /api/posts/ endpoint uses 1.0/0.0 floats. Handle both.
    """
    resolution = question.get("resolution")
    if resolution is None:
        return None

    q_type = question.get("type")
    if q_type == "binary":
        if resolution in (1.0, 1, "yes"):
            return "yes"
        elif resolution in (0.0, 0, "no"):
            return "no"
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


def extract_cp(question: dict) -> float | None:
    """Extract community prediction from /api2/ question data.

    The /api2/ endpoint stores aggregations under "unweighted" rather than
    "recency_weighted" like the /api/posts/ endpoint. Check both.
    """
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
def fetch(
    from_file: str | None = typer.Option(
        None, "--from-file", "-f", help="Listing JSON to get post IDs from"
    ),
    ids: str | None = typer.Option(None, "--ids", help="Comma-separated post IDs"),
    delay: float = typer.Option(5.0, "--delay", "-d", help="Seconds between requests"),
    apply_results: bool = typer.Option(
        False, "--apply", "-a", help="Apply results to forecast JSONs after fetching"
    ),
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Show what would be fetched"
    ),
) -> None:
    """Fetch resolution + CP from /api2/questions/ (unauthenticated, 1 req/question)."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    # Determine post IDs to fetch
    if ids:
        post_ids = [int(x.strip()) for x in ids.split(",")]
    elif from_file:
        all_ids = get_post_ids_from_file(from_file)
        unresolved = set(get_unresolved_post_ids())
        post_ids = [pid for pid in all_ids if pid in unresolved]
        typer.echo(
            f"From {from_file}: {len(all_ids)} total, {len(post_ids)} need resolution"
        )
    else:
        post_ids = get_unresolved_post_ids()
        typer.echo(f"Found {len(post_ids)} unresolved forecasts")

    # Filter out already-cached
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    already_cached = {int(f.stem) for f in CACHE_DIR.glob("*.json")}
    to_fetch = [pid for pid in post_ids if pid not in already_cached]
    typer.echo(
        f"To fetch: {len(to_fetch)} ({len(already_cached & set(post_ids))} already cached)"
    )

    if dry_run:
        for pid in to_fetch:
            typer.echo(f"  Would fetch: {OLD_API_BASE}/{pid}/")
        return

    if not to_fetch:
        typer.echo("Nothing to fetch")
        if apply_results:
            _apply_cached()
        return

    # Fetch one at a time with conservative rate limiting
    fetched = 0
    errors = 0

    with httpx.Client(timeout=30.0) as client:
        for i, post_id in enumerate(to_fetch):
            if i > 0:
                time.sleep(delay)

            typer.echo(f"[{i + 1}/{len(to_fetch)}] Fetching {post_id}...", nl=False)
            try:
                resp = client.get(f"{OLD_API_BASE}/{post_id}/")

                if resp.status_code == 429:
                    retry_after = resp.headers.get("Retry-After", "60")
                    wait = float(retry_after)
                    typer.echo(f" 429 — waiting {wait:.0f}s")
                    time.sleep(wait)
                    resp = client.get(f"{OLD_API_BASE}/{post_id}/")

                if resp.status_code == 200:
                    data = resp.json()
                    cache_file = CACHE_DIR / f"{post_id}.json"
                    cache_file.write_text(json.dumps(data, indent=2))

                    question = data.get("question") or {}
                    resolution = extract_resolution(question)
                    cp = extract_cp(question)
                    typer.echo(f" → res={resolution}, cp={cp}")
                    fetched += 1
                else:
                    typer.echo(f" HTTP {resp.status_code}")
                    errors += 1

            except httpx.HTTPError as e:
                typer.echo(f" Error: {e}")
                errors += 1

    typer.echo(
        f"\nDone: {fetched} fetched, {errors} errors, {len(already_cached & set(post_ids))} cached"
    )

    if apply_results:
        _apply_cached()


@app.command()
def apply() -> None:
    """Apply cached /api2/ data to forecast JSONs."""
    _apply_cached()


def _apply_cached() -> None:
    """Read cache dir and update forecast files with resolution + CP data."""
    if not CACHE_DIR.exists():
        typer.echo("No cache directory found. Run 'fetch' first.")
        raise typer.Exit(1)

    updated = 0
    cp_entries: dict[str, dict] = {}

    for cache_file in sorted(CACHE_DIR.glob("*.json")):
        post_id = cache_file.stem
        data = json.loads(cache_file.read_text())
        question = data.get("question") or {}

        resolution = extract_resolution(question)
        cp = extract_cp(question)

        if cp is not None:
            from datetime import datetime

            cp_entries[post_id] = {
                "cp": cp,
                "fetched_at": datetime.now().isoformat(),
                "question_status": question.get("status", "unknown"),
            }

        if resolution is None:
            continue

        for base in (FORECASTS_PATH, RETRODICT_PATH):
            post_dir = base / post_id
            if not post_dir.exists():
                continue
            for f in post_dir.glob("*.json"):
                forecast = json.loads(f.read_text())
                if forecast.get("resolution") != resolution:
                    forecast["resolution"] = resolution
                    f.write_text(json.dumps(forecast, indent=2))
                    updated += 1

    # Update feedback state CP cache
    if cp_entries:
        _update_cp_cache(cp_entries)

    typer.echo(
        f"Applied: {updated} forecast files updated, {len(cp_entries)} CP entries cached"
    )


def _update_cp_cache(cp_entries: dict[str, dict]) -> None:
    """Merge CP data into feedback_state.json."""
    import sh

    git = sh.Command("git")
    try:
        branch = str(git("branch", "--show-current")).strip() or "main"
    except Exception:
        branch = "main"

    state_file = Path(f"./notes/feedback_loop/{branch}/feedback_state.json")
    state_file.parent.mkdir(parents=True, exist_ok=True)

    if state_file.exists():
        state = json.loads(state_file.read_text())
    else:
        state = {}

    if "cp_cache" not in state:
        state["cp_cache"] = {}

    state["cp_cache"].update(cp_entries)
    state_file.write_text(json.dumps(state, indent=2))
    typer.echo(f"  CP cache updated in {state_file}")


if __name__ == "__main__":
    app()
