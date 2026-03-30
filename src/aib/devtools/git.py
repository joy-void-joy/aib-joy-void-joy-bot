"""Git operations for forecast files."""

import asyncio
import json
import re

import sh
import typer

from aib.agent.history import get_latest_forecast, is_submitted
from aib.paths import (
    find_latest_forecast_file,
    iter_forecast_dirs,
    iter_session_dirs,
    iter_trace_log_files,
)

app = typer.Typer(no_args_is_help=True)

_TRACE_POST_RE = re.compile(r"notes/traces/[^/]+/(?:forecasts|sessions)/(\d+)/")
_TRACE_LOG_RE = re.compile(r"notes/traces/[^/]+/logs/(\d+)_")


def _get_uncommitted_post_ids() -> set[int]:
    """Find post IDs with uncommitted forecast-related files."""
    git = sh.Command("git")
    post_ids: set[int] = set()

    status = str(git.status("--porcelain", "--", "notes/", _ok_code=[0])).strip()
    if not status:
        return post_ids

    for line in status.splitlines():
        file_path = line[3:].split(" -> ")[0].strip()

        m = _TRACE_POST_RE.search(file_path) or _TRACE_LOG_RE.search(file_path)
        if m:
            post_ids.add(int(m.group(1)))

    return post_ids


def _get_question_title(post_id: int) -> str:
    """Read question title from the latest forecast JSON."""
    latest = find_latest_forecast_file(post_id)
    if latest is None:
        return f"question {post_id}"
    try:
        data = json.loads(latest.read_text(encoding="utf-8"))
        return data.get("question_title", f"question {post_id}")
    except (json.JSONDecodeError, OSError):
        return f"question {post_id}"


def _commit_post(post_id: int, *, dry_run: bool = False) -> bool:
    """Stage and commit files for a single post ID."""
    git = sh.Command("git")
    paths: list[str] = []

    for d in iter_forecast_dirs(post_id):
        paths.append(str(d))

    for d in iter_session_dirs(post_id):
        paths.append(str(d))

    for f in iter_trace_log_files(post_id):
        paths.append(str(f))

    if not paths:
        return False

    if dry_run:
        from tqdm import tqdm

        title = _get_question_title(post_id)
        tqdm.write(f"  Would commit {post_id}: {title[:50]}")
        for p in paths:
            tqdm.write(f"    {p}")
        return True

    for path in paths:
        try:
            git.add(path)
        except sh.ErrorReturnCode:
            pass

    diff = str(git.diff("--cached", "--stat", _ok_code=[0, 1])).strip()
    if not diff:
        return False

    title = _get_question_title(post_id)
    slug = title[:50].strip().rstrip(".")
    from tqdm import tqdm

    git.commit("-m", f"data(forecasts): {slug}")
    tqdm.write(f"  Committed {post_id}: {slug}")
    return True


@app.command("commit-forecasts")
def commit_forecasts(
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Show what would be committed"
    ),
) -> None:
    """Commit all uncommitted forecast files, one commit per question."""
    post_ids = _get_uncommitted_post_ids()

    if not post_ids:
        typer.echo("Nothing to commit.")
        return

    typer.echo(f"Found {len(post_ids)} post(s) with uncommitted files")

    from tqdm import tqdm

    committed = 0
    for post_id in tqdm(sorted(post_ids), desc="Committing", unit="post"):
        try:
            if _commit_post(post_id, dry_run=dry_run):
                committed += 1
        except sh.ErrorReturnCode as e:
            tqdm.write(f"  Failed {post_id}: {e}")

    if dry_run:
        typer.echo(f"\nWould commit {committed} question(s)")
    else:
        typer.echo(f"\nCommitted {committed} question(s)")


# ---------------------------------------------------------------------------
# Forecast status checking
# ---------------------------------------------------------------------------


@app.command("local")
def local_status(
    post_id: int = typer.Argument(..., help="Post ID to check"),
) -> None:
    """Check local submission status for a question."""
    typer.echo(f"Checking local status for post {post_id}...")
    typer.echo(f"  is_submitted: {is_submitted(post_id)}")

    forecast = get_latest_forecast(post_id)
    if forecast:
        typer.echo(f"  timestamp: {forecast.timestamp}")
        typer.echo(f"  submitted_at: {forecast.submitted_at}")
    else:
        typer.echo("  No local forecast found")


@app.command("mark")
def mark_submitted_cmd(
    post_id: int = typer.Argument(..., help="Post ID to mark as submitted"),
) -> None:
    """Mark a forecast as submitted (using API timestamp if available)."""
    from aib.agent.history import mark_submitted
    from aib.clients.metaculus import get_client

    async def _mark() -> None:
        client = get_client()
        try:
            q = await client.get_question_by_post_id(post_id)
            if isinstance(q, list):
                q = q[0]

            if q.timestamp_of_my_last_forecast is not None:
                timestamp = q.timestamp_of_my_last_forecast.strftime("%Y%m%d_%H%M%S")
                typer.echo(f"Found API submission time: {timestamp}")
            else:
                from datetime import datetime

                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                typer.echo(f"No API timestamp, using current time: {timestamp}")

            if mark_submitted(post_id, timestamp):
                typer.echo(f"Marked {post_id} as submitted")
            else:
                typer.echo(f"No forecast found for {post_id}")
        except (OSError, ValueError, AttributeError) as e:
            typer.echo(f"Error: {e}")

    asyncio.run(_mark())


@app.command("backfill")
def backfill(
    dry_run: bool = typer.Option(
        False, "--dry-run", "-n", help="Show what would be updated"
    ),
) -> None:
    """Backfill submitted_at for forecasts confirmed by the Metaculus API."""
    from aib.agent.history import mark_submitted
    from aib.clients.metaculus import get_client

    async def _backfill() -> None:
        client = get_client()

        from aib.paths import get_all_forecasted_post_ids

        post_ids = sorted(get_all_forecasted_post_ids())
        if not post_ids:
            typer.echo("No forecasts found")
            return

        from tqdm import tqdm

        updated = 0
        already_marked = 0
        not_submitted = 0

        for post_id in tqdm(sorted(post_ids), desc="Backfilling", unit="post"):
            forecast = get_latest_forecast(post_id)
            if forecast is None:
                continue

            if forecast.submitted_at is not None:
                already_marked += 1
                continue

            try:
                q = await client.get_question_by_post_id(post_id)
                if isinstance(q, list):
                    q = q[0]

                if q.timestamp_of_my_last_forecast is not None:
                    timestamp = q.timestamp_of_my_last_forecast.strftime(
                        "%Y%m%d_%H%M%S"
                    )
                    if dry_run:
                        tqdm.write(
                            f"  Would mark {post_id} as submitted at {timestamp}"
                        )
                    else:
                        mark_submitted(post_id, timestamp)
                        tqdm.write(f"  Marked {post_id} as submitted at {timestamp}")
                    updated += 1
                else:
                    not_submitted += 1
            except (OSError, ValueError, AttributeError) as e:
                tqdm.write(f"  Error checking {post_id}: {e}")

        typer.echo(
            f"\nSummary: {updated} updated, {already_marked} already marked, "
            f"{not_submitted} not submitted"
        )

    asyncio.run(_backfill())


@app.command("check")
def check_api(
    post_id: int = typer.Argument(..., help="Post ID to check"),
    tournament: str = typer.Option(
        "spring-aib-2026", "--tournament", "-t", help="Tournament ID"
    ),
) -> None:
    """Check if a question shows as already forecast in the API."""
    from aib.clients.metaculus import get_client
    from aib.config import settings

    async def _check() -> None:
        client = get_client()
        typer.echo(f"Using token: {settings.metaculus_token[:8]}...")

        typer.echo(f"\n1. Fetching question {post_id} directly...")
        try:
            q_result = await client.get_question_by_post_id(post_id)
            q = q_result[0] if isinstance(q_result, list) else q_result
            typer.echo(f"   Title: {q.question_text[:60]}...")
            typer.echo(
                f"   timestamp_of_my_last_forecast: {q.timestamp_of_my_last_forecast}"
            )
            typer.echo(
                f"   already_forecast: {q.timestamp_of_my_last_forecast is not None}"
            )
            typer.echo(
                f"   scheduled_close_time: {getattr(q, 'scheduled_close_time', 'N/A')}"
            )
            typer.echo(
                f"   actual_close_time: {getattr(q, 'actual_close_time', 'N/A')}"
            )
        except (OSError, ValueError) as e:
            typer.echo(f"   Error: {e}")

        typer.echo(f"\n2. Checking tournament {tournament}...")
        questions = await client.get_all_open_questions_from_tournament(tournament)
        typer.echo(f"   Found {len(questions)} open questions")

        for q in questions:
            typer.echo(f"\n   Question {q.id_of_post}: {q.question_text[:40]}...")
            typer.echo(
                f"   timestamp_of_my_last_forecast: {q.timestamp_of_my_last_forecast}"
            )

            my_forecasts = q.api_json.get("question", {}).get("my_forecasts")
            typer.echo(f"   my_forecasts in API JSON: {my_forecasts is not None}")
            if my_forecasts:
                typer.echo(f"   my_forecasts content: {my_forecasts}")

    asyncio.run(_check())
