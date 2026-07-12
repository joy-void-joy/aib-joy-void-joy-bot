"""Fetch resolutions and update saved forecasts.

Scans both live forecasts and retrodictions under notes/traces/<version>/.
Uses Playwright-based profile scraping for resolutions and scores.
"""

from __future__ import annotations

import asyncio
import json
import logging
from collections.abc import Callable
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import TYPE_CHECKING

import typer

if TYPE_CHECKING:
    from playwright.async_api import Page

from aib.devtools.scores import DEFAULT_USER_ID, fetch_scores, resolve_scraped
from aib.tools.retry import with_retry
from aib.agent.history import update_forecast_file
from aib.paths import (
    iter_forecast_dirs,
    iter_forecast_files,
    iter_retrodict_dirs,
    iter_retrodict_files,
)

logger = logging.getLogger(__name__)

app = typer.Typer(no_args_is_help=True)


SCRAPED_TO_FORECAST_FIELDS: dict[str, str] = {
    "title": "question_title",
    "type": "question_type",
    "description": "background_info",
    "resolution_criteria": "resolution_criteria",
    "fine_print": "fine_print",
    "scheduled_resolve_time": "question_scheduled_resolve_time",
    "scheduled_close_time": "question_close_time",
}


def map_scraped_fields(data: dict[str, str | None]) -> dict[str, str | None]:
    """Map scraped field names to SavedForecast field names."""
    return {
        SCRAPED_TO_FORECAST_FIELDS[k]: v
        for k, v in data.items()
        if k in SCRAPED_TO_FORECAST_FIELDS and v is not None
    }


def find_unresolved(
    base_path: Path,
    include_tentative: bool = False,
) -> list[dict]:
    """Find forecast files needing resolution in a directory tree.

    Args:
        base_path: Root path containing post_id subdirectories.
        include_tentative: If True, also include forecasts with
            resolution_source="tentative" (from AI-powered early resolution).
    """
    unresolved: list[dict] = []
    if not base_path.exists():
        return unresolved
    for post_dir in base_path.iterdir():
        if not post_dir.is_dir():
            continue
        for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
            try:
                data = json.loads(forecast_file.read_text())
                has_resolution = data.get("resolution") is not None
                is_tentative = data.get("resolution_source") == "tentative"
                if has_resolution and not (include_tentative and is_tentative):
                    continue
                unresolved.append(
                    {
                        "post_id": data.get("post_id") or int(post_dir.name),
                        "file": forecast_file,
                        "dir": post_dir,
                        "title": data.get("question_title", "Unknown")[:50],
                        "question_type": data.get("question_type", "binary"),
                        "resolution_criteria": data.get("resolution_criteria"),
                        "fine_print": data.get("fine_print"),
                        "scheduled_resolve_time": data.get(
                            "question_scheduled_resolve_time"
                        ),
                        "scheduled_close_time": data.get("question_close_time"),
                        "background_info": data.get("background_info"),
                        "resolution_source": data.get("resolution_source"),
                    }
                )
            except (json.JSONDecodeError, OSError, ValueError):
                continue
    return unresolved


QUESTION_PAGE_URL = "https://www.metaculus.com/questions/{post_id}/"


class NoCriteriaError(Exception):
    """Page loaded but no resolution criteria found (likely a 429)."""


SCRAPE_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

CAPTURE_RSC_INIT = """
    window.__rsc_captured = [];
    if (!window.__next_f) window.__next_f = [];
    const _origPush = window.__next_f.push.bind(window.__next_f);
    window.__next_f.push = function(...items) {
        for (const item of items) window.__rsc_captured.push(item);
        return _origPush(...items);
    };
"""

EXTRACT_QUESTION_JS = """() => {
    function find(obj, depth, parentDesc) {
        if (!obj || typeof obj !== 'object' || depth > 12) return null;
        if (typeof obj.description === 'string' && obj.description.length > 10) {
            parentDesc = obj.description;
        }
        if (typeof obj.resolution_criteria === 'string'
            && obj.resolution_criteria.length > 10) {
            return {
                title: obj.title || null,
                type: obj.type || null,
                description: obj.description || parentDesc || null,
                resolution_criteria: obj.resolution_criteria,
                fine_print: obj.fine_print || null,
                scheduled_resolve_time: obj.scheduled_resolve_time || null,
                scheduled_close_time: obj.scheduled_close_time || null,
            };
        }
        for (const v of (Array.isArray(obj) ? obj : Object.values(obj))) {
            if (v && typeof v === 'object') {
                const r = find(v, depth + 1, parentDesc);
                if (r) return r;
            }
        }
        return null;
    }

    function searchRscItems(items) {
        for (const item of items) {
            if (!Array.isArray(item) || item.length < 2
                || typeof item[1] !== 'string'
                || !item[1].includes('resolution_criteria')) continue;
            const colonIdx = item[1].indexOf(':');
            if (colonIdx < 1 || colonIdx > 5) continue;
            try {
                const data = JSON.parse(item[1].substring(colonIdx + 1));
                const q = find(data, 0, null);
                if (q) return q;
            } catch {}
        }
        return null;
    }

    // Strategy 1: Captured RSC data (intercepted via init script)
    if (window.__rsc_captured && window.__rsc_captured.length) {
        const q = searchRscItems(window.__rsc_captured);
        if (q) return JSON.stringify(q);
    }

    // Strategy 2: __next_f (if data hasn't been consumed)
    if (window.__next_f && Array.isArray(window.__next_f)) {
        const q = searchRscItems(window.__next_f);
        if (q) return JSON.stringify(q);
    }

    // Strategy 3: __NEXT_DATA__ (Pages Router)
    if (window.__NEXT_DATA__) {
        const q = find(window.__NEXT_DATA__, 0, null);
        if (q) return JSON.stringify(q);
    }

    return null;
}"""


def find_question_data(
    obj: object,
    depth: int = 0,
    parent_description: str | None = None,
) -> dict[str, str | None] | None:
    """Recursively search nested data for an object with resolution_criteria.

    Metaculus puts description on the post object, not the question object,
    so we track the nearest ancestor's description and use it as fallback.
    """
    if depth > 12 or not isinstance(obj, (dict, list)):
        return None
    if isinstance(obj, dict):
        desc = obj.get("description")
        if isinstance(desc, str) and len(desc) > 10:
            parent_description = desc
        criteria = obj.get("resolution_criteria")
        if isinstance(criteria, str) and len(criteria) > 10:
            return {
                "title": obj.get("title"),
                "type": obj.get("type"),
                "description": obj.get("description") or parent_description,
                "resolution_criteria": criteria,
                "fine_print": obj.get("fine_print"),
                "scheduled_resolve_time": obj.get("scheduled_resolve_time"),
                "scheduled_close_time": obj.get("scheduled_close_time"),
            }
        for v in obj.values():
            result = find_question_data(v, depth + 1, parent_description)
            if result:
                return result
    elif isinstance(obj, list):
        for item in obj:
            result = find_question_data(item, depth + 1, parent_description)
            if result:
                return result
    return None


async def scrape_question_page(
    post_id: int,
    page: Page,
) -> dict[str, str | None] | None:
    """Scrape question data from a Metaculus question page.

    Strategies:
    1. Intercept API responses during page load
    2. Extract from __NEXT_DATA__ or inline script tags via JS evaluation
    """
    from playwright.async_api import Response

    url = QUESTION_PAGE_URL.format(post_id=post_id)
    api_responses: list[Response] = []

    def capture(response: Response) -> None:
        if response.status != 200:
            return
        resp_url = response.url
        if (
            f"/api/posts/{post_id}" in resp_url
            or f"/api2/questions/{post_id}" in resp_url
        ):
            api_responses.append(response)

    page.on("response", capture)
    try:
        await page.goto(url, wait_until="networkidle", timeout=60_000)

        for resp in api_responses:
            try:
                data = await resp.json()
                result = find_question_data(data)
                if result:
                    return result
            except Exception:
                continue

        raw = await page.evaluate(EXTRACT_QUESTION_JS)
        if raw:
            try:
                return json.loads(raw)
            except (json.JSONDecodeError, TypeError):
                pass

        return None
    finally:
        page.remove_listener("response", capture)


async def scrape_questions_batch(
    post_ids: list[int],
    on_scraped: Callable[[int, str], None] | None = None,
    on_data: Callable[[int, dict[str, str | None]], None] | None = None,
) -> dict[int, dict[str, str | None]]:
    """Scrape question data for multiple posts using a shared browser.

    The on_scraped callback receives (post_id, status) where status is one of:
    - "scraped": resolution criteria found
    - "no criteria on page": page loaded but no resolution criteria in data
    - "error: <message>": page failed to load or Playwright error
    """
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        raise RuntimeError(
            "playwright not installed. Run: uv add playwright && playwright install chromium"
        )

    results: dict[int, dict[str, str | None]] = {}

    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)

        @with_retry(
            max_attempts=8, min_wait=8, max_wait=64, extra_exceptions=(NoCriteriaError,)
        )
        async def scrape_with_retry(pid: int) -> dict[str, str | None]:
            page = await browser.new_page(user_agent=SCRAPE_USER_AGENT)
            await page.add_init_script(CAPTURE_RSC_INIT)
            try:
                data = await scrape_question_page(pid, page)
                if data and data.get("resolution_criteria"):
                    return data
                raise NoCriteriaError(f"Post {pid}: no criteria on page (429?)")
            finally:
                await page.close()

        from tqdm import tqdm

        for pid in tqdm(post_ids, desc="Scraping questions", unit="q"):
            try:
                results[pid] = await scrape_with_retry(pid)
                status = "scraped"
            except NoCriteriaError:
                status = "no criteria on page"
            except Exception as exc:
                logger.warning("Failed to scrape post %d: %s", pid, exc)
                status = f"error: {exc}"

            if on_data and pid in results:
                on_data(pid, results[pid])
            if on_scraped:
                on_scraped(pid, status)

            await asyncio.sleep(5.0)

        await browser.close()

    return results


def backfill_metadata(
    version: str | None = None,
    dry_run: bool = False,
) -> None:
    """Scrape question pages for forecasts missing text fields.

    Finds forecasts missing resolution_criteria, fine_print, etc. and
    scrapes the Metaculus question page to fill them in. Handles both
    forecast and retrodict files.
    """
    from aib.agent.history import _update_forecast_json

    BACKFILLABLE = {
        "resolution_criteria",
        "fine_print",
        "background_info",
        "question_scheduled_resolve_time",
        "question_close_time",
    }

    targets: list[int] = []
    seen: set[int] = set()
    for base in {d.parent for d in iter_forecast_dirs()}:
        for item in find_unresolved(base):
            pid = item["post_id"]
            if not isinstance(pid, int) or pid in seen:
                continue
            seen.add(pid)
            if any(not item.get(f) for f in BACKFILLABLE):
                targets.append(pid)
    for base in {d.parent for d in iter_retrodict_dirs()}:
        for item in find_unresolved(base):
            pid = item["post_id"]
            if not isinstance(pid, int) or pid in seen:
                continue
            seen.add(pid)
            if any(not item.get(f) for f in BACKFILLABLE):
                targets.append(pid)

    if not targets:
        typer.echo("All forecasts have complete metadata fields")
        return

    typer.echo(f"Found {len(targets)} forecasts with missing metadata")

    updated_files = 0

    def write_scraped(pid: int, data: dict[str, str | None]) -> None:
        nonlocal updated_files
        fields = map_scraped_fields(data)
        for f in iter_forecast_files(pid, version=version):
            if dry_run or _update_forecast_json(f, **fields):
                updated_files += 1
        for f in iter_retrodict_files(pid, version=version):
            if dry_run or _update_forecast_json(f, **fields):
                updated_files += 1

    asyncio.run(scrape_questions_batch(targets, on_data=write_scraped))

    typer.echo(f"Backfilled {updated_files} files")
    if dry_run:
        typer.echo("  (dry run — no files changed)")


def _count_tentative_resolutions() -> dict[int, str]:
    """Find all forecasts with resolution_source='tentative'."""
    tentative: dict[int, str] = {}
    for base in {d.parent for d in iter_forecast_dirs()}:
        if not base.exists():
            continue
        for post_dir in base.iterdir():
            if not post_dir.is_dir():
                continue
            for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
                try:
                    data = json.loads(forecast_file.read_text())
                    if data.get("resolution_source") == "tentative":
                        pid = data.get("post_id") or int(post_dir.name)
                        res = str(data.get("resolution", "?"))
                        tentative[pid] = res
                except (json.JSONDecodeError, OSError, ValueError):
                    continue
    return tentative


@app.command("sync")
def sync(
    user_id: int = typer.Option(DEFAULT_USER_ID, "--user-id", help="Metaculus user ID"),
    version: str | None = typer.Option(
        None, "--version", "-v", help="Scope to agent version"
    ),
    backfill: bool = typer.Option(
        False, "--backfill", help="Also scrape question pages for missing metadata"
    ),
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Don't update files"),
) -> None:
    """Check for and apply resolution updates via profile page scrape."""
    tentative = _count_tentative_resolutions()
    if tentative:
        typer.echo(f"Tentative resolutions (from AI resolve): {len(tentative)}")
        for pid, res in sorted(tentative.items()):
            typer.echo(f"  {pid}: {res}")
        typer.echo()

    typer.echo(f"Fetching scores from profile page (user {user_id})...")
    raw = asyncio.run(fetch_scores(user_id))
    records = raw.get("records")
    record_list = records if isinstance(records, list) else []
    typer.echo(f"Got {len(record_list)} records from profile")

    updated, unchanged = resolve_scraped(record_list, version=version, dry_run=dry_run)
    typer.echo(f"\nUpdated: {updated}, Unchanged: {unchanged}")
    if dry_run:
        typer.echo("(dry run — no files changed)")

    # Worldview subforecast resolution sweep
    from aib.tools.worldview_manager import (
        find_resolvable_forecasts,
        resolve_ready_forecasts,
    )

    resolvable = find_resolvable_forecasts()
    if resolvable:
        typer.echo(
            f"\n--- Worldview subforecast resolution ({len(resolvable)} resolvable) ---"
        )
        wv_results = asyncio.run(resolve_ready_forecasts(dry_run=dry_run))
        resolved = sum(1 for r in wv_results if r.get("resolved") and "resolution" in r)
        typer.echo(f"Checked: {len(wv_results)}, Resolved: {resolved}")
        for r in wv_results:
            if r.get("resolved") and "resolution" in r:
                typer.echo(
                    f"  ✓ {r.get('slug')}: {r['resolution']} (score={r.get('score')})"
                )
        if not dry_run and resolved > 0:
            from aib.worldview.lookup import commit_worldview

            commit_worldview("worldview: AI resolution sweep")

    if backfill:
        typer.echo("\n--- Backfilling missing metadata ---")
        backfill_metadata(version=version, dry_run=dry_run)


@app.command("status")
def status() -> None:
    """Show resolution status of all forecasts (live + retrodict)."""
    resolved_yes = 0
    resolved_no = 0
    resolved_other = 0
    tentative_count = 0
    unresolved = 0

    from tqdm import tqdm

    seen_posts: set[str] = set()
    bases = [
        *(d.parent for d in iter_forecast_dirs()),
        *(d.parent for d in iter_retrodict_dirs()),
    ]
    all_post_dirs = [
        (base, post_dir)
        for base in bases
        if base.exists()
        for post_dir in base.iterdir()
        if post_dir.is_dir()
    ]
    for base, post_dir in tqdm(all_post_dirs, desc="Scanning", unit="dir"):
        key = f"{base}:{post_dir.name}"
        if key in seen_posts:
            continue
        seen_posts.add(key)
        for forecast_file in sorted(post_dir.glob("*.json"), reverse=True)[:1]:
            try:
                data = json.loads(forecast_file.read_text())
                resolution = data.get("resolution")
                source = data.get("resolution_source")
                if resolution is None:
                    unresolved += 1
                elif source == "tentative":
                    tentative_count += 1
                elif str(resolution).lower() == "yes":
                    resolved_yes += 1
                elif str(resolution).lower() == "no":
                    resolved_no += 1
                else:
                    resolved_other += 1
            except (json.JSONDecodeError, OSError):
                continue

    total = resolved_yes + resolved_no + resolved_other + tentative_count + unresolved

    typer.echo(f"\n=== Resolution Status ({total} forecasts) ===\n")
    typer.echo(f"Resolved YES:   {resolved_yes}")
    typer.echo(f"Resolved NO:    {resolved_no}")
    typer.echo(f"Resolved other: {resolved_other}")
    typer.echo(f"Tentative:      {tentative_count}")
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
    for f in iter_forecast_files(post_id):
        if update_forecast_file(f, resolution, source="manual"):
            updated += 1
    for f in iter_retrodict_files(post_id):
        if update_forecast_file(f, resolution, source="manual"):
            updated += 1

    if updated == 0:
        typer.echo(f"No forecasts found for post {post_id}")
        raise typer.Exit(1)

    typer.echo(f"Updated {updated} forecast files for post {post_id}")


def is_due_within(
    item: dict[str, object],
    days: float,
) -> bool:
    """Check if a forecast's scheduled_resolve_time is past or within N days."""
    raw = item.get("scheduled_resolve_time")
    if not isinstance(raw, str):
        return False
    try:
        resolve_time = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    except ValueError:
        return False
    cutoff = datetime.now(timezone.utc) + timedelta(days=days)
    return resolve_time <= cutoff


def _score_resolved_forecasts(applied_pids: list[int]) -> None:
    """Fetch community predictions and compute peer+baseline scores for resolved posts."""
    from aib.agent.history import _update_forecast_json
    from aib.devtools.scores import scrape_community_batch

    typer.echo(f"\nScoring {len(applied_pids)} resolved forecasts...")

    community_data = asyncio.run(scrape_community_batch(applied_pids))

    scored = 0
    for pid in applied_pids:
        cd = community_data.get(pid)
        if cd is None:
            continue
        cp_updates = cd.to_forecast_updates()
        if not cp_updates:
            continue

        for f in iter_forecast_files(pid):
            _update_forecast_json(f, **cp_updates)

        scored += 1

    typer.echo(f"  Scored: {scored}/{len(applied_pids)}")


@app.command("tentative")
def tentative(
    post_ids: list[int] = typer.Argument(
        None, help="Post IDs to resolve (all unresolved if omitted)"
    ),
    days: float = typer.Option(
        2.5,
        "--days",
        "-d",
        help="Only check questions resolving within N days (0=past due only, use --all to skip)",
    ),
    all_questions: bool = typer.Option(
        False, "--all", help="Check all unresolved questions regardless of resolve time"
    ),
    min_confidence: float = typer.Option(
        0.7, "--min-confidence", help="Minimum confidence to apply resolution"
    ),
    override: bool = typer.Option(
        False,
        "--override",
        help="Re-check questions that already have tentative resolutions",
    ),
    sync_first: bool = typer.Option(
        True,
        "--sync/--no-sync",
        help="Scrape official resolutions from the profile page before AI resolution",
    ),
) -> None:
    """Attempt early resolution using AI agents to check criteria.

    Scrapes official resolutions from the profile page first so questions
    that already resolved on Metaculus get their real answer instead of an
    AI verdict (skip with --no-sync).
    """
    from aib.agent.resolver import (
        QuestionForResolution,
        ResolutionVerdict,
        resolve_batch,
        resolve_question,
    )

    if sync_first:
        typer.echo("Syncing official resolutions from profile page...")
        raw = asyncio.run(fetch_scores(DEFAULT_USER_ID))
        records = raw.get("records")
        record_list = records if isinstance(records, list) else []
        updated, unchanged = resolve_scraped(record_list)
        typer.echo(f"  Official updates: {updated} applied, {unchanged} unchanged\n")

    unresolved: list[dict[str, object]] = []
    for base in {d.parent for d in iter_forecast_dirs()}:
        unresolved.extend(find_unresolved(base, include_tentative=override))

    if post_ids:
        pid_set = set(post_ids)
        unresolved = [u for u in unresolved if u["post_id"] in pid_set]
    elif not all_questions:
        total = len(unresolved)
        due = [u for u in unresolved if is_due_within(u, days)]
        no_time = [u for u in unresolved if not u.get("scheduled_resolve_time")]
        skipped = total - len(due)
        if skipped:
            typer.echo(
                f"Filtered to {len(due)}/{total} questions due within {days} days "
                f"({skipped} skipped, {len(no_time)} missing resolve time)"
            )
            if no_time:
                typer.echo(
                    "  Tip: run 'aib-devtools resolution sync --backfill' to backfill resolve times"
                )
        unresolved = due

    if not unresolved:
        typer.echo("No unresolved forecasts found")
        return

    # Build questions from local forecast data
    questions: list[QuestionForResolution] = []
    no_criteria_items: list[dict[str, object]] = []
    for item in unresolved:
        pid = item["post_id"]
        if not isinstance(pid, int):
            continue
        criteria = str(item.get("resolution_criteria") or "")
        if not criteria:
            no_criteria_items.append(item)
            continue
        questions.append(
            QuestionForResolution(
                post_id=pid,
                question_title=str(item.get("title", "")),
                question_type=str(item.get("question_type", "binary")),
                resolution_criteria=criteria,
                fine_print=str(item.get("fine_print") or ""),
                description=str(item.get("background_info") or ""),
                scheduled_resolve_time=str(v)
                if (v := item.get("scheduled_resolve_time"))
                else None,
                scheduled_close_time=str(v2)
                if (v2 := item.get("scheduled_close_time"))
                else None,
            )
        )

    # Scrape question pages for forecasts missing resolution_criteria
    if no_criteria_items:
        pids_to_scrape = [
            item["post_id"]
            for item in no_criteria_items
            if isinstance(item["post_id"], int)
        ]
        typer.echo(f"  Scraping {len(pids_to_scrape)} questions missing criteria...")

        scraped = asyncio.run(scrape_questions_batch(pids_to_scrape))

        items_by_pid = {
            item["post_id"]: item
            for item in no_criteria_items
            if isinstance(item["post_id"], int)
        }
        for pid, data in scraped.items():
            local = items_by_pid.get(pid, {})
            questions.append(
                QuestionForResolution(
                    post_id=pid,
                    question_title=str(data.get("title") or local.get("title") or ""),
                    question_type=str(
                        data.get("type") or local.get("question_type") or "binary"
                    ),
                    resolution_criteria=str(data["resolution_criteria"]),
                    fine_print=str(data.get("fine_print") or ""),
                    description=str(data.get("description") or ""),
                    scheduled_resolve_time=str(v)
                    if (
                        v := data.get("scheduled_resolve_time")
                        or local.get("scheduled_resolve_time")
                    )
                    else None,
                    scheduled_close_time=str(v2)
                    if (
                        v2 := data.get("scheduled_close_time")
                        or local.get("scheduled_close_time")
                    )
                    else None,
                )
            )

        still_missing = len(pids_to_scrape) - len(scraped)
        if still_missing:
            typer.echo(f"  {still_missing} questions still missing after scrape")

    if not questions:
        typer.echo("No questions with resolution criteria to check")
        return

    from tqdm import tqdm

    pbar = tqdm(total=len(questions), desc="Resolving", unit="q")

    applied = 0
    skipped = 0
    applied_pids: list[int] = []

    def on_complete(pid: int, verdict: ResolutionVerdict) -> None:
        nonlocal applied, skipped
        icon = "Y" if verdict.resolved else "N"
        tqdm.write(
            f"  [{icon}] {pid} ({verdict.confidence:.0%}): {verdict.reason[:80]}"
        )

        if not verdict.resolved or verdict.resolution is None:
            skipped += 1
        elif verdict.confidence < min_confidence:
            tqdm.write(
                f"  -> Skipped {pid} (confidence {verdict.confidence:.0%} < {min_confidence:.0%})"
            )
            skipped += 1
        else:
            for f in iter_forecast_files(pid):
                update_forecast_file(
                    f,
                    verdict.resolution,
                    source="tentative",
                    reason=verdict.reason,
                )
            applied += 1
            applied_pids.append(pid)

        pbar.update(1)

    async def run() -> list[tuple[int, ResolutionVerdict]]:
        if len(questions) == 1:
            report = await resolve_question(questions[0])
            v = report.payload or ResolutionVerdict(
                resolved=False,
                resolution=None,
                confidence=0.0,
                reason="Agent produced no structured output",
                sources=[],
            )
            on_complete(questions[0].post_id, v)
            return [(questions[0].post_id, v)]
        return await resolve_batch(questions, on_complete=on_complete)

    asyncio.run(run())
    pbar.close()

    typer.echo(f"\nResults: {applied} applied, {skipped} skipped")

    if applied_pids:
        _score_resolved_forecasts(applied_pids)


TRACE_FIELD_MAP: dict[str, str] = {
    "resolution_criteria": "resolution_criteria",
    "fine_print": "fine_print",
    "background_info": "background_info",
    "description": "background_info",
    "scheduled_resolve_time": "question_scheduled_resolve_time",
    "scheduled_close_time": "question_close_time",
}


def extract_fields_from_trace(trace_path: Path) -> dict[str, str | None]:
    """Extract question fields from a trace.md JSON block."""
    for line in trace_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped.startswith("{") or '"resolution_criteria"' not in stripped:
            continue
        try:
            data = json.loads(stripped)
        except json.JSONDecodeError:
            continue
        if not data.get("resolution_criteria"):
            continue
        result: dict[str, str | None] = {}
        for src_key, dst_key in TRACE_FIELD_MAP.items():
            val = data.get(src_key)
            if val and dst_key not in result:
                result[dst_key] = str(val)
        return result
    return {}


@app.command("backfill-criteria")
def backfill_criteria(
    dry_run: bool = typer.Option(False, "--dry-run", "-n", help="Don't update files"),
) -> None:
    """Backfill missing fields from session traces into forecast JSONs.

    Extracts resolution_criteria, fine_print, description (background_info),
    scheduled_resolve_time, and scheduled_close_time from trace files.
    """
    from aib.agent.history import _update_forecast_json
    from aib.paths import TRACES_PATH

    from tqdm import tqdm

    fields_by_post: dict[int, dict[str, str | None]] = {}
    for version_dir in tqdm(
        sorted(TRACES_PATH.iterdir()), desc="Scanning traces", unit="ver"
    ):
        sessions = version_dir / "sessions"
        if not sessions.is_dir():
            continue
        for post_dir in sessions.iterdir():
            if not post_dir.is_dir():
                continue
            try:
                pid = int(post_dir.name)
            except ValueError:
                continue
            if pid in fields_by_post:
                continue
            for trace_file in post_dir.glob("*/trace.md"):
                result = extract_fields_from_trace(trace_file)
                if result:
                    fields_by_post[pid] = result
                    break

    typer.echo(f"Found trace data for {len(fields_by_post)} posts")

    updated = 0
    already_complete = 0
    no_trace = 0
    all_forecast_post_dirs = [
        post_dir
        for base in {d.parent for d in iter_forecast_dirs()}
        if base.exists()
        for post_dir in base.iterdir()
        if post_dir.is_dir()
    ]
    for post_dir in tqdm(all_forecast_post_dirs, desc="Updating forecasts", unit="dir"):
        try:
            pid = int(post_dir.name)
        except ValueError:
            continue
        if pid not in fields_by_post:
            no_trace += 1
            continue
        trace_fields = fields_by_post[pid]
        for forecast_file in post_dir.glob("*.json"):
            data = json.loads(forecast_file.read_text(encoding="utf-8"))
            new_fields = {
                k: v for k, v in trace_fields.items() if v and not data.get(k)
            }
            if not new_fields:
                already_complete += 1
                continue
            if dry_run:
                updated += 1
                continue
            if _update_forecast_json(forecast_file, **new_fields):
                updated += 1

    typer.echo(
        f"Updated: {updated}, Already complete: {already_complete}, No trace data: {no_trace}"
    )
    if dry_run:
        typer.echo("  (dry run - no files changed)")
