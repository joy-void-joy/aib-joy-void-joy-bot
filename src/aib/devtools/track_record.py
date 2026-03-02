"""Scrape Metaculus track record for peer scores and resolutions.

Uses Playwright headless browser to extract score data from React
internals on the profile track record page. The Metaculus API does not
reliably expose peer/baseline scores, so we scrape the rendered page.

Usage:
    uv run aib-devtools track-record scrape
    uv run aib-devtools track-record show
"""

import asyncio
import json
from pathlib import Path

import httpx
import typer

app = typer.Typer(no_args_is_help=True)

PROFILE_URL = "https://www.metaculus.com/accounts/profile/{user_id}/track-record/"
DEFAULT_USER_ID = 290661

EXTRACT_JS = """
() => {
    const svgs = document.querySelectorAll("svg");
    let chart = null;
    for (const svg of svgs) {
        const p = svg.parentElement;
        if (p && p.className && p.className.toString().includes("VictoryContainer")
            && parseInt(svg.getAttribute("width") || "0") > 500) {
            chart = svg;
            break;
        }
    }
    if (!chart) {
        for (const svg of svgs) {
            if (svg.querySelectorAll("path").length > 100) {
                chart = svg;
                break;
            }
        }
    }
    if (!chart) return { error: "no_chart" };

    const fk = Object.keys(chart).find(k => k.startsWith("__reactFiber"));
    if (!fk) return { error: "no_fiber" };

    let fiber = chart[fk];
    let data = null;
    let username = "";
    let depth = 0;

    while (fiber && depth < 60) {
        const props = fiber.memoizedProps || fiber.pendingProps;
        if (props) {
            const src = props.scatterPlot || props.score_scatter_plot;
            if (src && Array.isArray(src)) {
                data = src;
                username = props.username || "";
                break;
            }
        }
        fiber = fiber.return;
        depth++;
    }
    if (!data || !data.length) return { error: "no_data" };

    return {
        username,
        records: data.map(q => {
            const r = {};
            for (const [k, v] of Object.entries(q)) {
                if (typeof v !== "function" && typeof v !== "object") r[k] = v;
            }
            return r;
        })
    };
}
"""


async def fetch_scores(user_id: int) -> dict:
    """Launch headless browser, navigate to track record, extract React data."""
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        raise RuntimeError(
            "playwright not installed. Run: uv add playwright && playwright install chromium"
        )

    url = PROFILE_URL.format(user_id=user_id)
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page(
            user_agent=(
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            ),
        )
        await page.goto(url, wait_until="domcontentloaded", timeout=60_000)

        try:
            await page.wait_for_selector(
                "svg[class*='VictoryContainer'], svg",
                state="attached",
                timeout=45_000,
            )
        except Exception:
            await browser.close()
            raise RuntimeError("Chart did not render within 45s")

        await page.wait_for_timeout(5_000)
        result = await page.evaluate(EXTRACT_JS)
        await browser.close()

    if isinstance(result, dict) and "error" in result:
        errors = {
            "no_chart": "No score scatter plot found on page",
            "no_fiber": "Cannot access React internals",
            "no_data": "Score data array is empty",
        }
        raise RuntimeError(errors.get(result["error"], result["error"]))

    return result


def normalize_resolution(raw: str) -> str | float:
    """Normalize a scraped resolution string to forecast JSON format."""
    s = raw.strip()
    low = s.lower()
    if low in ("yes", "no"):
        return low
    try:
        return float(s)
    except ValueError:
        return s


def resolve_scraped(
    records: list[dict[str, object]],
    version: str | None = None,
    dry_run: bool = False,
) -> tuple[int, int]:
    """Write peer_score, score_timestamp, resolution, baseline_score to forecast JSONs."""
    from aib.agent.history import _update_forecast_json
    from aib.paths import iter_forecast_files, iter_retrodict_files
    from aib.scoring import compute_baseline_score

    scores_by_post: dict[int, dict[str, object]] = {}
    for rec in records:
        pid = rec.get("post_id")
        if isinstance(pid, int):
            scores_by_post[pid] = rec

    updated = 0
    unchanged = 0

    for post_id, rec in sorted(scores_by_post.items()):
        raw_res = rec.get("question_resolution")
        peer = rec.get("score")
        score_ts = rec.get("score_timestamp")

        if raw_res is None or str(raw_res).strip() == "":
            continue

        resolution = normalize_resolution(str(raw_res))

        files = list(iter_forecast_files(post_id, version=version)) + list(
            iter_retrodict_files(post_id, version=version)
        )
        for f in files:
            forecast = json.loads(f.read_text())

            updates: dict[str, object] = {}

            if forecast.get("resolution") is None:
                updates["resolution"] = resolution
            if peer is not None and forecast.get("peer_score") is None:
                updates["peer_score"] = peer
            if score_ts is not None and forecast.get("score_timestamp") is None:
                updates["score_timestamp"] = score_ts

            if forecast.get("baseline_score") is None:
                merged = {**forecast, **updates}
                baseline = compute_baseline_score(merged)
                if baseline is not None:
                    updates["baseline_score"] = baseline

            if not updates:
                unchanged += 1
                continue

            if dry_run:
                typer.echo(f"  {post_id}: {updates}")
            else:
                if _update_forecast_json(f, **updates):
                    typer.echo(f"  {post_id}: {updates}")
            updated += 1

    return updated, unchanged


@app.command()
def scrape(
    user_id: int = typer.Option(
        DEFAULT_USER_ID, "--user-id", "-u", help="Metaculus user ID"
    ),
    version: str | None = typer.Option(
        None, "--version", "-v", help="Only update forecasts for this version"
    ),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Don't update files"),
) -> None:
    """Scrape track record and update forecast JSONs with peer scores."""
    typer.echo(f"Scraping track record for user {user_id}...")

    data = asyncio.run(fetch_scores(user_id))
    records = data.get("records", [])
    typer.echo(f"Scraped {len(records)} records")

    scores = [r["score"] for r in records if r.get("score") is not None]
    if scores:
        avg = sum(scores) / len(scores)
        typer.echo(f"Avg peer score: {avg:.4f} (n={len(scores)})")

    updated, unchanged = resolve_scraped(records, version, dry_run)
    typer.echo(f"\nUpdated: {updated}, Unchanged: {unchanged}")
    if dry_run:
        typer.echo("(dry run)")


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
        typer.echo("No scored forecasts found. Run 'track-record scrape' first.")
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
