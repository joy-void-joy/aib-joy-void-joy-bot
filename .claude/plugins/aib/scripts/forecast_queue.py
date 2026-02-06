#!/usr/bin/env python3
"""Forecasting queue management.

Shows questions that need forecasting, sorted by urgency.
Helps prevent missing questions before they close.
"""

import asyncio
from datetime import datetime, timedelta, timezone
from pathlib import Path

import httpx
import typer

app = typer.Typer(help="Manage forecasting queue and priorities")

FORECASTS_PATH = Path("./notes/forecasts")
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
    tournament: str = typer.Argument("aib", help="Tournament: aib, minibench, or cup"),
    days: int = typer.Option(7, help="Look back N days for resolved questions"),
) -> None:
    """Show recently resolved questions that we didn't forecast."""
    if tournament not in TOURNAMENTS:
        typer.echo(f"Unknown tournament: {tournament}")
        raise typer.Exit(1)

    tournament_id = TOURNAMENTS[tournament]
    forecasted = get_forecasted_post_ids()

    async def fetch_resolved():
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(
                "https://www.metaculus.com/api/posts/",
                params={
                    "order_by": "-resolve_time",
                    "status": "resolved",
                    "tournaments": tournament_id,
                    "limit": 50,
                },
            )
            response.raise_for_status()
            return response.json().get("results", [])

    typer.echo(f"\nFetching recently resolved questions from {tournament}...")
    questions = asyncio.run(fetch_resolved())

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)

    missed_questions = []
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

        if post_id not in forecasted:
            missed_questions.append(
                {
                    "post_id": post_id,
                    "title": q.get("title", "")[:60],
                    "resolve_time": resolve_time,
                }
            )

    if not missed_questions:
        typer.echo(f"\nNo questions resolved in last {days} days were missed!")
        return

    typer.echo(f"\n=== Missed Questions (Last {days} Days) ===\n")
    typer.echo(f"{'ID':<8} {'Resolved':<12} {'Title'}")
    typer.echo("-" * 90)

    for q in missed_questions:
        resolve_str = q["resolve_time"].strftime("%Y-%m-%d")
        typer.echo(f"{q['post_id']:<8} {resolve_str:<12} {q['title']}")

    typer.echo(f"\nTotal missed: {len(missed_questions)}")


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
