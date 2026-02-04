#!/usr/bin/env python3
"""Check forecast status for a question from the Metaculus API."""

import asyncio

import typer

from aib.agent.history import get_latest_forecast, is_submitted
from aib.clients.metaculus import get_client
from aib.config import settings

app = typer.Typer()


@app.command()
def local(
    post_id: int = typer.Argument(..., help="Post ID to check"),
) -> None:
    """Check local submission status for a question."""
    print(f"Checking local status for post {post_id}...")
    print(f"  is_submitted: {is_submitted(post_id)}")

    forecast = get_latest_forecast(post_id)
    if forecast:
        print(f"  timestamp: {forecast.timestamp}")
        print(f"  submitted_at: {forecast.submitted_at}")
    else:
        print("  No local forecast found")


@app.command()
def mark(
    post_id: int = typer.Argument(..., help="Post ID to mark as submitted"),
) -> None:
    """Mark a forecast as submitted (using API timestamp if available)."""
    from aib.agent.history import mark_submitted

    async def _mark() -> None:
        # Try to get timestamp from API
        client = get_client()
        try:
            q = await client.get_question_by_post_id(post_id)
            if isinstance(q, list):
                q = q[0]

            if q.timestamp_of_my_last_forecast is not None:
                timestamp = q.timestamp_of_my_last_forecast.strftime("%Y%m%d_%H%M%S")
                print(f"Found API submission time: {timestamp}")
            else:
                from datetime import datetime

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                print(f"No API timestamp, using current time: {timestamp}")

            if mark_submitted(post_id, timestamp):
                print(f"✅ Marked {post_id} as submitted")
            else:
                print(f"❌ No forecast found for {post_id}")
        except Exception as e:
            print(f"Error: {e}")

    asyncio.run(_mark())


@app.command()
def backfill(
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Show what would be updated"
    ),
) -> None:
    """Backfill submitted_at for forecasts that were submitted to Metaculus.

    Checks each local forecast against the Metaculus API and marks
    forecasts as submitted if the API confirms they were submitted.
    """

    from aib.agent.history import FORECASTS_BASE_PATH, mark_submitted

    async def _backfill() -> None:
        client = get_client()

        # Find all forecast directories
        if not FORECASTS_BASE_PATH.exists():
            print("No forecasts directory found")
            return

        post_ids = [
            int(d.name)
            for d in FORECASTS_BASE_PATH.iterdir()
            if d.is_dir() and d.name.isdigit()
        ]

        print(f"Found {len(post_ids)} questions with local forecasts")

        updated = 0
        already_marked = 0
        not_submitted = 0

        for post_id in sorted(post_ids):
            forecast = get_latest_forecast(post_id)
            if forecast is None:
                continue

            # Skip if already marked
            if forecast.submitted_at is not None:
                already_marked += 1
                continue

            # Check Metaculus API
            try:
                q = await client.get_question_by_post_id(post_id)
                if isinstance(q, list):
                    q = q[0]

                if q.timestamp_of_my_last_forecast is not None:
                    timestamp = q.timestamp_of_my_last_forecast.strftime(
                        "%Y%m%d_%H%M%S"
                    )
                    if dry_run:
                        print(f"  Would mark {post_id} as submitted at {timestamp}")
                    else:
                        mark_submitted(post_id, timestamp)
                        print(f"  Marked {post_id} as submitted at {timestamp}")
                    updated += 1
                else:
                    not_submitted += 1
            except Exception as e:
                print(f"  Error checking {post_id}: {e}")

        print(
            f"\nSummary: {updated} updated, {already_marked} already marked, {not_submitted} not submitted"
        )

    asyncio.run(_backfill())


@app.command()
def check(
    post_id: int = typer.Argument(..., help="Post ID to check"),
    tournament: str = typer.Option(
        "spring-aib-2026", "--tournament", "-t", help="Tournament ID"
    ),
) -> None:
    """Check if a question shows as already forecast in the API."""

    async def _check() -> None:
        client = get_client()
        print(f"Using token: {settings.metaculus_token[:8]}...")

        # First try to fetch the question directly
        print(f"\n1. Fetching question {post_id} directly...")
        try:
            q = await client.get_question_by_post_id(post_id)
            print(f"   Title: {q.question_text[:60]}...")
            print(
                f"   timestamp_of_my_last_forecast: {q.timestamp_of_my_last_forecast}"
            )
            print(f"   already_forecast: {q.timestamp_of_my_last_forecast is not None}")
            print(
                f"   scheduled_close_time: {getattr(q, 'scheduled_close_time', 'N/A')}"
            )
            print(f"   actual_close_time: {getattr(q, 'actual_close_time', 'N/A')}")
        except Exception as e:
            print(f"   Error: {e}")

        # Then check tournament listing
        print(f"\n2. Checking tournament {tournament}...")
        questions = await client.get_all_open_questions_from_tournament(tournament)
        print(f"   Found {len(questions)} open questions")

        for q in questions:
            print(f"\n   Question {q.id_of_post}: {q.question_text[:40]}...")
            print(
                f"   timestamp_of_my_last_forecast: {q.timestamp_of_my_last_forecast}"
            )

            # Check if my_forecasts is in the raw API JSON
            my_forecasts = q.api_json.get("question", {}).get("my_forecasts")
            print(f"   my_forecasts in API JSON: {my_forecasts is not None}")
            if my_forecasts:
                print(f"   my_forecasts content: {my_forecasts}")

    asyncio.run(_check())


if __name__ == "__main__":
    app()
