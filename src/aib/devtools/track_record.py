"""Track record display and CDF backfill.

Scraping logic has moved to `aib.devtools.scores` (see `scores scrape`).

Usage:
    uv run aib-devtools track-record show
    uv run aib-devtools track-record backfill-cdf
"""

import json
from pathlib import Path

import httpx
import typer

app = typer.Typer(no_args_is_help=True)


@app.command()
def show(
    version: str | None = typer.Option(
        None, "--version", "-v", help="Filter by agent version"
    ),
    all_versions: bool = typer.Option(
        False, "--all-versions", help="Include all versions"
    ),
) -> None:
    """Display peer and baseline scores from forecast JSONs."""
    from aib.paths import (
        load_all_forecast_jsons,
        load_all_retrodict_jsons,
        resolve_version,
    )
    from aib.version import AGENT_VERSION

    effective_version = version if version is not None else AGENT_VERSION
    effective, warning = resolve_version(effective_version, all_versions)
    if warning:
        typer.echo(warning)

    forecasts: list[dict[str, object]] = []
    for d in load_all_forecast_jsons(versions=effective):
        if d.get("peer_score") is not None:
            forecasts.append(d)
    for d in load_all_retrodict_jsons(versions=effective):
        if d.get("peer_score") is not None:
            forecasts.append(d)

    if not forecasts:
        typer.echo("No scored forecasts found. Run 'scores scrape' first.")
        return

    typer.echo(f"\n{'ID':<8} {'Peer':>8} {'Base':>8} {'Res':<10} {'Title'}")
    typer.echo("-" * 95)

    peer_scores: list[float] = []
    baseline_scores: list[float] = []

    def by_post_id(d: dict[str, object]) -> int:
        pid = d.get("post_id")
        if isinstance(pid, int):
            return pid
        return 0

    for fc in sorted(forecasts, key=by_post_id):
        pid = fc.get("post_id", "")
        peer = fc.get("peer_score")
        resolution = fc.get("resolution", "")
        title = str(fc.get("question_title", ""))[:55]

        peer_str = f"{peer:+.1f}" if isinstance(peer, (int, float)) else "-"
        res_str = str(resolution)[:10] if resolution else "-"

        baseline = fc.get("baseline_score")
        base_str = f"{baseline:+.1f}" if isinstance(baseline, (int, float)) else "-"

        if isinstance(peer, (int, float)):
            peer_scores.append(float(peer))
        if isinstance(baseline, (int, float)):
            baseline_scores.append(float(baseline))

        typer.echo(f"{pid:<8} {peer_str:>8} {base_str:>8} {res_str:<10} {title}")

    typer.echo(f"\n{'=' * 40}")
    typer.echo(f"Total scored:      {len(forecasts)}")

    if peer_scores:
        typer.echo(f"Avg peer score:    {sum(peer_scores) / len(peer_scores):>+8.2f}")
    if baseline_scores:
        typer.echo(
            f"Avg baseline score:{sum(baseline_scores) / len(baseline_scores):>+8.2f}"
        )


def fetch_cdf(post_id: int, client: httpx.Client) -> dict[str, object]:
    """Fetch CDF and scaling data for a post from the Metaculus API."""
    import time

    resp = client.get(f"https://www.metaculus.com/api/posts/{post_id}/")
    for attempt in range(5):
        if resp.status_code != 429:
            break
        wait = 2 ** (attempt + 1)
        time.sleep(wait)
        resp = client.get(f"https://www.metaculus.com/api/posts/{post_id}/")

    resp.raise_for_status()
    data = resp.json()
    question = data.get("question") or {}

    my_forecasts = question.get("my_forecasts") or {}
    latest = my_forecasts.get("latest")
    if not latest:
        raise RuntimeError("no forecast submitted")

    cdf = latest.get("forecast_values", [])
    if not cdf:
        raise RuntimeError("empty forecast_values")

    scaling = question.get("scaling") or {}
    result: dict[str, object] = {"cdf": list(cdf)}
    if scaling.get("range_min") is not None:
        result["numeric_bounds"] = {
            "range_min": scaling["range_min"],
            "range_max": scaling["range_max"],
            "open_lower_bound": question.get("open_lower_bound"),
            "open_upper_bound": question.get("open_upper_bound"),
            "zero_point": scaling.get("zero_point"),
        }
    return result


@app.command("backfill-cdf")
def backfill_cdf_cmd(
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Don't update files"),
    limit: int = typer.Option(
        0, "--limit", "-l", help="Max questions to process (0=all)"
    ),
) -> None:
    """Backfill CDF and numeric_bounds into forecast JSONs via Metaculus API."""
    import time

    from aib.agent.history import _update_forecast_json
    from aib.config import settings
    from aib.paths import iter_forecast_files, iter_retrodict_files

    needs_backfill: dict[int, list[Path]] = {}
    skipped_retrodict = 0
    for f in list(iter_forecast_files()) + list(iter_retrodict_files()):
        data = json.loads(f.read_text())
        if data.get("question_type") not in ("numeric", "discrete"):
            continue
        if data.get("cdf") is not None:
            continue
        if data.get("submitted_at") is None:
            skipped_retrodict += 1
            continue
        pid = data.get("post_id")
        if isinstance(pid, int):
            needs_backfill.setdefault(pid, []).append(f)

    if not needs_backfill:
        typer.echo("All numeric/discrete forecasts already have CDF data.")
        return

    if skipped_retrodict:
        typer.echo(f"Skipped {skipped_retrodict} unsubmitted files (retrodictions)")
    typer.echo(f"Found {len(needs_backfill)} questions needing CDF backfill")

    post_ids = sorted(needs_backfill.keys())
    if limit > 0:
        post_ids = post_ids[:limit]

    client = httpx.Client(
        headers={"Authorization": f"Token {settings.metaculus_token}"},
        timeout=30,
    )

    from tqdm import tqdm

    updated = 0
    failed = 0
    for pid in tqdm(post_ids, desc="Backfilling CDFs", unit="q"):
        try:
            result = fetch_cdf(pid, client)
        except Exception as e:
            tqdm.write(f"  {pid}: FAILED ({e})")
            failed += 1
            time.sleep(10)
            continue

        cdf = result["cdf"]
        bounds = result.get("numeric_bounds")
        assert isinstance(cdf, list)

        if dry_run:
            tqdm.write(f"  {pid}: {len(cdf)} points (dry run)")
        else:
            for f in needs_backfill[pid]:
                updates: dict[str, object] = {"cdf": cdf}
                if bounds:
                    updates["numeric_bounds"] = bounds
                _update_forecast_json(f, **updates)
            tqdm.write(
                f"  {pid}: {len(cdf)} points -> {len(needs_backfill[pid])} files"
            )

        updated += 1
        time.sleep(10)

    client.close()
    typer.echo(f"\nUpdated: {updated}, Failed: {failed}")
    if dry_run:
        typer.echo("(dry run)")
