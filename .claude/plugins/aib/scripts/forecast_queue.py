#!/usr/bin/env python3
"""Forecasting queue management.

Shows questions that need forecasting, sorted by urgency.
Helps prevent missing questions before they close.
"""

import asyncio
import csv
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx
import typer

app = typer.Typer(help="Manage forecasting queue and priorities")

FORECASTS_PATH = Path("./notes/forecasts")
RETRODICT_PATH = Path("./notes/retrodict")
SCORES_CSV_PATH = Path("./notes/scores.csv")
TOURNAMENTS = {
    "aib": 32916,  # AIB Spring 2026
    "minibench": 32715,  # MiniBench
    "cup": 32585,  # Metaculus Cup
}


def get_forecasted_post_ids() -> set[int]:
    """Get post IDs that have already been forecast."""
    forecasted = set()
    if not FORECASTS_PATH.exists():
        return forecasted

    for post_dir in FORECASTS_PATH.iterdir():
        if post_dir.is_dir():
            try:
                forecasted.add(int(post_dir.name))
            except ValueError:
                continue
    return forecasted


def get_retrodicted_post_ids() -> set[int]:
    """Get post IDs that have already been retrodicted."""
    retrodicted = set()
    if not RETRODICT_PATH.exists():
        return retrodicted

    for post_dir in RETRODICT_PATH.iterdir():
        if post_dir.is_dir():
            name = post_dir.name.split("_")[0]
            try:
                retrodicted.add(int(name))
            except ValueError:
                continue
    return retrodicted


def _extract_resolution_and_cp(q: dict) -> tuple[str | None, bool, str]:
    """Extract resolution value, CP availability, and question type from API response."""
    question_data = q.get("question", {})
    resolution = question_data.get("resolution")
    question_type = question_data.get("type", "unknown")

    has_cp = False
    try:
        aggregations = question_data.get("aggregations", {})
        for agg_type in ("recency_weighted", "unweighted"):
            if agg_type in aggregations:
                latest = aggregations[agg_type].get("latest")
                if latest and latest.get("centers"):
                    has_cp = True
                    break
    except (KeyError, TypeError):
        pass

    return resolution, has_cp, question_type


def _load_scores_for_posts(post_ids: set[int]) -> dict[int, dict[str, str]]:
    """Load the latest score row for each post_id from scores.csv."""
    scores: dict[int, dict[str, str]] = {}
    if not SCORES_CSV_PATH.exists():
        return scores
    with SCORES_CSV_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                pid = int(row["post_id"])
            except (ValueError, KeyError):
                continue
            if pid in post_ids:
                scores[pid] = row
    return scores


async def fetch_tournament_questions(tournament_id: int) -> list[dict]:
    """Fetch open questions from a tournament."""
    questions = []
    offset = 0

    async with httpx.AsyncClient(timeout=30.0) as client:
        while True:
            response = await client.get(
                "https://www.metaculus.com/api/posts/",
                params={
                    "order_by": "close_time",
                    "status": "open",
                    "tournaments": tournament_id,
                    "offset": offset,
                    "limit": 100,
                },
            )
            response.raise_for_status()
            data = response.json()

            results = data.get("results", [])
            if not results:
                break

            questions.extend(results)
            offset += len(results)

            if len(results) < 100:
                break

    return questions


async def fetch_individual_posts(post_ids: list[int]) -> dict[int, dict]:
    """Fetch individual posts to get full resolution and CP data.

    The listing endpoint strips aggregation data; individual fetches include it.
    Uses a semaphore to avoid overwhelming the API.
    """
    results: dict[int, dict] = {}
    sem = asyncio.Semaphore(5)

    async def _fetch_one(client: httpx.AsyncClient, pid: int) -> None:
        async with sem:
            try:
                resp = await client.get(f"https://www.metaculus.com/api/posts/{pid}/")
                if resp.status_code == 200:
                    results[pid] = resp.json()
            except httpx.HTTPError:
                pass

    async with httpx.AsyncClient(timeout=30.0) as client:
        await asyncio.gather(*[_fetch_one(client, pid) for pid in post_ids])

    return results


async def _fetch_resolved(tournament_ids: list[int], limit: int = 50) -> list[dict]:
    """Fetch resolved questions from one or more tournaments."""
    all_questions: list[dict] = []

    async with httpx.AsyncClient(timeout=30.0) as client:
        for tid in tournament_ids:
            response = await client.get(
                "https://www.metaculus.com/api/posts/",
                params={
                    "order_by": "-resolve_time",
                    "status": "resolved",
                    "tournaments": tid,
                    "limit": limit,
                },
            )
            response.raise_for_status()
            results = response.json().get("results", [])
            all_questions.extend(results)

    # Deduplicate by post ID (a question may appear in multiple tournaments)
    seen: set[int] = set()
    deduped: list[dict] = []
    for q in all_questions:
        pid = q.get("id")
        if pid and pid not in seen:
            seen.add(pid)
            deduped.append(q)

    return deduped


def parse_question(q: dict) -> dict | None:
    """Parse a question from the API response."""
    question_data = q.get("question")
    if not question_data:
        return None

    close_time_str = q.get("scheduled_close_time") or question_data.get(
        "scheduled_close_time"
    )
    if not close_time_str:
        return None

    try:
        close_time = datetime.fromisoformat(close_time_str.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None

    now = datetime.now(timezone.utc)
    time_left = close_time - now

    return {
        "post_id": q.get("id"),
        "title": q.get("title", "")[:70],
        "question_type": question_data.get("type", "unknown"),
        "close_time": close_time,
        "time_left": time_left,
        "url": f"https://www.metaculus.com/questions/{q.get('id')}/",
    }


@app.command("upcoming")
def upcoming(
    tournament: str = typer.Argument("aib", help="Tournament: aib, minibench, or cup"),
    days: int = typer.Option(7, help="Show questions closing in next N days"),
    show_all: bool = typer.Option(
        False, "--all", help="Include already-forecasted questions"
    ),
) -> None:
    """Show questions closing soon that need forecasting."""
    if tournament not in TOURNAMENTS:
        typer.echo(f"Unknown tournament: {tournament}")
        typer.echo(f"Available: {', '.join(TOURNAMENTS.keys())}")
        raise typer.Exit(1)

    tournament_id = TOURNAMENTS[tournament]
    forecasted = get_forecasted_post_ids()

    typer.echo(f"\nFetching open questions from {tournament}...")
    questions = asyncio.run(fetch_tournament_questions(tournament_id))

    parsed = []
    for q in questions:
        p = parse_question(q)
        if p:
            parsed.append(p)

    # Filter to questions closing soon
    cutoff = timedelta(days=days)
    closing_soon = [
        q
        for q in parsed
        if q["time_left"] <= cutoff and q["time_left"].total_seconds() > 0
    ]

    # Sort by time left
    closing_soon.sort(key=lambda x: x["time_left"])

    # Optionally filter out already forecasted
    if not show_all:
        closing_soon = [q for q in closing_soon if q["post_id"] not in forecasted]

    if not closing_soon:
        typer.echo(f"\nNo questions closing in next {days} days need forecasting.")
        return

    typer.echo(f"\n=== Questions Closing in Next {days} Days ===")
    typer.echo(f"{'ID':<8} {'Type':<10} {'Time Left':<15} {'Title'}")
    typer.echo("-" * 100)

    for q in closing_soon:
        time_left_str = format_timedelta(q["time_left"])
        forecasted_marker = " ✓" if q["post_id"] in forecasted else ""
        typer.echo(
            f"{q['post_id']:<8} {q['question_type']:<10} {time_left_str:<15} {q['title']}{forecasted_marker}"
        )

    unforecasted = sum(1 for q in closing_soon if q["post_id"] not in forecasted)
    typer.echo(
        f"\nTotal: {len(closing_soon)} questions, {unforecasted} not yet forecasted"
    )


@app.command("status")
def status(
    tournament: str = typer.Argument("aib", help="Tournament: aib, minibench, or cup"),
) -> None:
    """Show forecasting status for a tournament."""
    if tournament not in TOURNAMENTS:
        typer.echo(f"Unknown tournament: {tournament}")
        raise typer.Exit(1)

    tournament_id = TOURNAMENTS[tournament]
    forecasted = get_forecasted_post_ids()

    typer.echo(f"\nFetching questions from {tournament}...")
    questions = asyncio.run(fetch_tournament_questions(tournament_id))

    parsed = [parse_question(q) for q in questions]
    parsed = [p for p in parsed if p is not None]

    # Stats
    total = len(parsed)
    done = sum(1 for q in parsed if q["post_id"] in forecasted)

    # By type
    by_type: dict[str, dict[str, int]] = {}
    for q in parsed:
        qtype = q["question_type"]
        if qtype not in by_type:
            by_type[qtype] = {"total": 0, "done": 0}
        by_type[qtype]["total"] += 1
        if q["post_id"] in forecasted:
            by_type[qtype]["done"] += 1

    typer.echo(f"\n=== {tournament.upper()} Tournament Status ===\n")
    typer.echo(f"Total open questions: {total}")
    typer.echo(
        f"Already forecasted:   {done} ({100 * done / total:.0f}%)"
        if total > 0
        else "Already forecasted: 0"
    )
    typer.echo(f"Need forecasting:     {total - done}")

    typer.echo("\nBy question type:")
    for qtype, stats in sorted(by_type.items()):
        pct = 100 * stats["done"] / stats["total"] if stats["total"] > 0 else 0
        typer.echo(f"  {qtype:<15} {stats['done']:>3}/{stats['total']:<3} ({pct:.0f}%)")


@app.command("missed")
def missed(
    tournament: str = typer.Argument(
        "aib", help="Tournament: aib, minibench, cup, or all"
    ),
    days: int = typer.Option(14, help="Look back N days for resolved questions"),
    show_all: bool = typer.Option(
        False, "--all", help="Include questions without confirmed resolution"
    ),
) -> None:
    """Show recently resolved questions suitable for retrodiction.

    Validates each question has a confirmed resolution via individual API fetches.
    Shows resolution value, CP availability, question type, and retrodiction scores.
    Use --tournament all to search across all tournaments.
    """
    if tournament == "all":
        tournament_ids = list(TOURNAMENTS.values())
        label = "all tournaments"
    elif tournament in TOURNAMENTS:
        tournament_ids = [TOURNAMENTS[tournament]]
        label = tournament
    else:
        typer.echo(f"Unknown tournament: {tournament}")
        typer.echo(f"Available: {', '.join(TOURNAMENTS.keys())}, all")
        raise typer.Exit(1)

    forecasted = get_forecasted_post_ids()
    retrodicted = get_retrodicted_post_ids()

    typer.echo(f"\nFetching recently resolved questions from {label}...")
    questions = asyncio.run(_fetch_resolved(tournament_ids))

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    # First pass: filter by time and collect candidates
    candidates: list[dict] = []
    for q in questions:
        post_id = q.get("id")
        resolve_time_str = q.get("actual_close_time") or q.get("scheduled_close_time")
        if not resolve_time_str:
            continue

        try:
            resolve_time = datetime.fromisoformat(
                resolve_time_str.replace("Z", "+00:00")
            )
        except (ValueError, AttributeError):
            continue

        if resolve_time < cutoff:
            continue

        if post_id in forecasted:
            continue

        resolution, has_cp, question_type = _extract_resolution_and_cp(q)
        candidates.append(
            {
                "post_id": post_id,
                "title": q.get("title", "")[:55],
                "resolve_time": resolve_time,
                "resolution": resolution,
                "has_cp": has_cp,
                "question_type": question_type,
                "retrodicted": post_id in retrodicted,
            }
        )

    # Individual fetches for questions missing resolution or CP
    needs_fetch = [
        c["post_id"] for c in candidates if not c["resolution"] or not c["has_cp"]
    ]
    if needs_fetch:
        typer.echo(
            f"Fetching details for {len(needs_fetch)} questions (missing resolution/CP)..."
        )
        individual = asyncio.run(fetch_individual_posts(needs_fetch))
        for c in candidates:
            if c["post_id"] in individual:
                resolution, has_cp, _ = _extract_resolution_and_cp(
                    individual[c["post_id"]]
                )
                if resolution:
                    c["resolution"] = resolution
                if has_cp:
                    c["has_cp"] = has_cp

    # Filter out null-resolution unless --all
    missed_questions: list[dict] = []
    skipped_no_resolution = 0
    for c in candidates:
        if not c["resolution"] and not show_all:
            skipped_no_resolution += 1
            continue
        missed_questions.append(c)

    if not missed_questions:
        msg = f"\nNo retrodict-ready questions resolved in last {days} days."
        if skipped_no_resolution:
            msg += f" ({skipped_no_resolution} skipped: no confirmed resolution)"
        typer.echo(msg)
        return

    # Load scores for retrodicted questions
    retrodicted_ids = {q["post_id"] for q in missed_questions if q["retrodicted"]}
    scores = _load_scores_for_posts(retrodicted_ids)

    typer.echo(f"\n=== Retrodiction Candidates ({label}, Last {days} Days) ===")
    typer.echo("Legend: [R]esolution [C]P available  (*=already retrodicted)\n")
    typer.echo(
        f"{'ID':<8} {'R':>1} {'C':>1} {'Type':<8} {'Score':<10} "
        f"{'Resolved':<12} {'Title'}"
    )
    typer.echo("-" * 105)

    retrodict_ready: list[dict] = []
    for q in missed_questions:
        resolve_str = q["resolve_time"].strftime("%Y-%m-%d")
        r_icon = "Y" if q["resolution"] else "-"
        c_icon = "Y" if q["has_cp"] else "-"
        retro_marker = "*" if q["retrodicted"] else " "

        score_str = "-"
        if q["post_id"] in scores:
            s = scores[q["post_id"]]
            brier = s.get("brier", "")
            log_s = s.get("log_score", "")
            if brier:
                score_str = f"B={float(brier):.3f}"
            elif log_s:
                score_str = f"L={float(log_s):.3f}"

        typer.echo(
            f"{q['post_id']:<8} {r_icon:>1} {c_icon:>1} {q['question_type']:<8} "
            f"{score_str:<10} {resolve_str:<12} {retro_marker}{q['title']}"
        )
        if q["resolution"] and not q["retrodicted"]:
            retrodict_ready.append(q)

    typer.echo(f"\nTotal: {len(missed_questions)} questions")
    if skipped_no_resolution:
        typer.echo(
            f"  Skipped: {skipped_no_resolution} (no confirmed resolution, use --all)"
        )
    already = sum(1 for q in missed_questions if q["retrodicted"])
    if already:
        typer.echo(f"  Already retrodicted: {already}")

    if retrodict_ready:
        ids = " ".join(str(q["post_id"]) for q in retrodict_ready)
        typer.echo(f"\nRetrodict command:\n  uv run forecast retrodict {ids}")


@app.command("search")
def search(
    query: str = typer.Argument(help="Search query (e.g. 'AI safety', 'nuclear')"),
    question_type: str = typer.Option(
        "binary", "--type", "-t", help="Question type: binary, numeric, multiple_choice"
    ),
    limit: int = typer.Option(20, "--limit", "-l", help="Max results"),
    resolved_only: bool = typer.Option(
        True, "--resolved/--open", help="Only resolved questions (default) or open"
    ),
) -> None:
    """Search Metaculus for questions suitable for retrodiction.

    Searches across all of Metaculus (not limited to any tournament).
    By default shows resolved questions with confirmed resolution values.
    """
    retrodicted = get_retrodicted_post_ids()

    status = "resolved" if resolved_only else "open"
    typer.echo(f"\nSearching Metaculus for '{query}' ({status}, {question_type})...")

    async def _search() -> list[dict]:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(
                "https://www.metaculus.com/api/posts/",
                params={
                    "search": query,
                    "status": status,
                    "order_by": "-resolve_time" if resolved_only else "-publish_time",
                    "limit": limit,
                },
            )
            response.raise_for_status()
            return response.json().get("results", [])

    questions = asyncio.run(_search())

    # Filter by question type
    filtered: list[dict] = []
    for q in questions:
        qdata = q.get("question", {})
        if qdata.get("type") == question_type:
            filtered.append(q)

    if not filtered:
        typer.echo(f"\nNo {question_type} questions found matching '{query}'.")
        return

    # Individual fetches to get resolution + CP data
    post_ids: list[int] = [q["id"] for q in filtered if q.get("id")]
    typer.echo(f"Fetching details for {len(post_ids)} questions...")
    individual = asyncio.run(fetch_individual_posts(post_ids))

    typer.echo(f"\n=== Search Results: '{query}' ({len(filtered)} {question_type}) ===")
    typer.echo("Legend: [R]esolution [C]P available  (*=already retrodicted)\n")
    typer.echo(f"{'ID':<8} {'R':>1} {'C':>1} {'Type':<8} {'Title'}")
    typer.echo("-" * 90)

    retrodict_ready: list[int] = []
    for q in filtered:
        pid: int = q.get("id", 0)
        title = q.get("title", "")[:60]

        data = individual.get(pid, q)
        resolution, has_cp, _ = _extract_resolution_and_cp(data)

        r_icon = "Y" if resolution else "-"
        c_icon = "Y" if has_cp else "-"
        retro_marker = "*" if pid in retrodicted else " "

        typer.echo(
            f"{pid:<8} {r_icon:>1} {c_icon:>1} {question_type:<8} {retro_marker}{title}"
        )
        if resolution and pid not in retrodicted:
            retrodict_ready.append(pid)

    if retrodict_ready:
        ids = " ".join(str(pid) for pid in retrodict_ready)
        typer.echo(f"\nRetrodict command:\n  uv run forecast retrodict {ids}")


def format_timedelta(td: timedelta) -> str:
    """Format a timedelta for display."""
    total_seconds = int(td.total_seconds())

    if total_seconds < 0:
        return "CLOSED"

    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, _ = divmod(remainder, 60)

    if days > 0:
        return f"{days}d {hours}h"
    elif hours > 0:
        return f"{hours}h {minutes}m"
    else:
        return f"{minutes}m"


if __name__ == "__main__":
    app()
