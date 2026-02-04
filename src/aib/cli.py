"""Metaculus Forecasting Bot - CLI Entry Point."""

import asyncio
import logging
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated

import httpx
import typer

from aib.agent import ForecastOutput, run_forecast
from aib.agent.history import is_submitted, load_latest_for_submission, mark_submitted
from aib.agent.retrodict import RetrodictConfig
from aib.agent.models import CreditExhaustedError
from aib.submission import (
    SubmissionError,
    format_reasoning_comment,
    list_open_tournament_questions,
    post_comment,
    submit_forecast,
)

app = typer.Typer(help="Metaculus AI Benchmarking Forecasting Bot")
logger = logging.getLogger(__name__)

LOGS_BASE_PATH = Path("./logs")


def wait_for_credit_reset(error: CreditExhaustedError) -> None:
    """Wait until credit reset time, with progress updates."""
    if error.reset_time is None:
        # No reset time available, use a default wait of 1 hour
        default_wait = 60 * 60
        print("💤 Credit exhausted, waiting 1 hour (no reset time available)...")
        time.sleep(default_wait)
        return

    now = datetime.now(error.reset_time.tzinfo)
    wait_seconds = (error.reset_time - now).total_seconds()

    if wait_seconds <= 0:
        print("⚡ Reset time has passed, continuing...")
        return

    reset_str = error.reset_time.strftime("%H:%M %Z")
    print(
        f"💤 Credit exhausted. Waiting until {reset_str} ({wait_seconds / 60:.0f} minutes)..."
    )

    # Sleep in chunks to show progress
    chunk_size = 300  # 5 minutes
    remaining = wait_seconds
    while remaining > 0:
        sleep_time = min(chunk_size, remaining)
        time.sleep(sleep_time)
        remaining -= sleep_time
        if remaining > 0:
            print(f"   ⏳ {remaining / 60:.0f} minutes remaining...")

    print("⚡ Credit reset time reached, resuming...")


def display_forecast(output: ForecastOutput) -> None:
    """Display forecast results to console."""
    print(f"\n{'=' * 60}")
    print(f"Question: {output.question_title}")
    print(f"Type: {output.question_type}")
    print("=" * 60)

    print(f"\nSummary: {output.summary}")

    if output.probability is not None:
        line = f"\nForecast: {output.probability * 100:.1f}%"
        if output.logit is not None:
            line += f" (logit: {output.logit:+.2f})"
            if output.probability_from_logit is not None:
                diff = abs(output.probability - output.probability_from_logit)
                if diff > 0.005:  # Show if >0.5% difference
                    line += f" [sigmoid: {output.probability_from_logit * 100:.1f}%]"
        print(line)

    if output.probabilities:
        print("\nProbabilities:")
        for option, prob in output.probabilities.items():
            print(f"  {option}: {prob * 100:.1f}%")

    if output.median is not None:
        print(f"\nEstimate: {output.median}")
        if output.confidence_interval:
            lo, hi = output.confidence_interval
            print(f"90% CI: [{lo}, {hi}]")

    if output.factors:
        print("\nFactors:")
        for factor in output.factors:
            sign = "+" if factor.logit >= 0 else ""
            print(f"  [{sign}{factor.logit:.1f}] {factor.description}")

    if output.sources_consulted:
        print(f"\nSources: {len(output.sources_consulted)} consulted")

    print("\n" + "=" * 60)
    if output.duration_seconds:
        print(f"Duration: {output.duration_seconds:.1f}s")
    if output.cost_usd:
        print(f"Cost: ${output.cost_usd:.4f}")
    if output.tool_metrics:
        metrics = output.tool_metrics
        print(
            f"Tools: {metrics.get('total_tool_calls', 0)} calls, "
            f"{metrics.get('total_errors', 0)} errors"
        )
    print()


def setup_logging(question_id: int) -> Path:
    """Configure logging to file only.

    Returns the path to the log file.
    """
    log_dir = LOGS_BASE_PATH / str(question_id)
    log_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    log_file = log_dir / f"{timestamp}.log"

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    )
    root_logger.addHandler(file_handler)

    return log_file


@app.command()
def test(
    question_id: Annotated[int, typer.Argument(help="Metaculus question/post ID")],
) -> None:
    """Test forecasting on a single question without submitting."""
    log_file = setup_logging(question_id)
    print(f"Logging to {log_file}")

    try:
        output = asyncio.run(run_forecast(question_id))
        display_forecast(output)
    except CreditExhaustedError as e:
        reset_msg = ""
        if e.reset_time:
            reset_msg = f" Resets at {e.reset_time.strftime('%H:%M %Z')}."
        print(f"❌ Credit exhausted.{reset_msg}")
        raise typer.Exit(1)
    except httpx.HTTPStatusError as e:
        print(f"Failed to fetch question: {e}")
        raise typer.Exit(1)
    except RuntimeError as e:
        print(f"Agent failed: {e}")
        raise typer.Exit(1)


@app.command()
def retrodict(
    question_ids: Annotated[
        list[int], typer.Argument(help="Metaculus post IDs of resolved questions")
    ],
    forecast_date: Annotated[
        str | None,
        typer.Option(
            "--forecast-date",
            "-d",
            help="Restrict data access to this date (YYYY-MM-DD). Enables blind mode.",
        ),
    ] = None,
    blind: Annotated[
        bool,
        typer.Option(
            "--blind/--no-blind",
            help="Enable blind mode (restrict to question published_at if no --forecast-date)",
        ),
    ] = True,
) -> None:
    """Run forecasts on resolved questions for calibration.

    Forecasts resolved questions to build calibration data. Does not submit.
    Shows the actual resolution and computes Brier score for binary questions.

    By default, runs in "blind mode" which restricts all tools to data
    available before the question's published_at date. This prevents
    "future leak" where the agent finds out the answer by searching.

    Use --forecast-date to specify a custom cutoff date, or --no-blind
    to disable time restrictions entirely (useful for testing).

    Examples:
        uv run forecast retrodict 41835 41521
        uv run forecast retrodict 41835 --forecast-date 2026-01-15
        uv run forecast retrodict 41835 --no-blind  # No time restriction
    """
    import sys

    sys.path.insert(0, "src")
    from metaculus import AsyncMetaculusClient, BinaryQuestion

    # Parse forecast_date if provided
    parsed_forecast_date: datetime | None = None
    if forecast_date:
        try:
            parsed_forecast_date = datetime.strptime(forecast_date, "%Y-%m-%d")
        except ValueError:
            print(f"❌ Invalid date format: {forecast_date}. Use YYYY-MM-DD.")
            raise typer.Exit(1)

    async def get_resolution_and_published(
        post_id: int,
    ) -> tuple[str | None, float | None, datetime | None]:
        """Fetch resolution, final CP, and published_at for a question."""
        client = AsyncMetaculusClient()
        try:
            result = await client.get_question_by_post_id(post_id)
            # Handle single question or group (list). For groups, we use the
            # first question - if the user wants a specific sub-question, they
            # should provide that sub-question's post_id directly.
            if isinstance(result, list):
                if len(result) > 1:
                    logger.warning(
                        "Post %d contains %d questions. Using first: %s",
                        post_id,
                        len(result),
                        result[0].question_text[:50],
                    )
                q = result[0]
            else:
                q = result
            resolution = q.resolution_string
            cp = None
            if isinstance(q, BinaryQuestion):
                cp = q.community_prediction_at_access_time
            # Get published_at from the question data
            published_at = getattr(q, "published_at", None)
            if published_at and isinstance(published_at, str):
                # Parse ISO format
                published_at = datetime.fromisoformat(
                    published_at.replace("Z", "+00:00")
                )
            return resolution, cp, published_at
        except Exception as e:
            logger.warning(f"Failed to fetch resolution for {post_id}: {e}")
            return None, None, None

    results: list[dict] = []

    for i, qid in enumerate(question_ids, 1):
        print(f"\n{'=' * 60}")
        print(f"[{i}/{len(question_ids)}] Retrodicting question {qid}")
        print("=" * 60)

        # Fetch resolution and published_at
        resolution, final_cp, published_at = asyncio.run(
            get_resolution_and_published(qid)
        )
        if resolution:
            print(f"Resolution: {resolution}")
            if final_cp is not None:
                print(f"Final CP: {final_cp:.1%}")
        else:
            print("⚠️  Could not fetch resolution (question may not be resolved)")

        # Determine the retrodict config
        retrodict_config: RetrodictConfig | None = None
        if blind:
            if parsed_forecast_date:
                retrodict_config = RetrodictConfig(forecast_date=parsed_forecast_date)
                print(
                    f"🔒 Blind mode: data restricted to before {parsed_forecast_date.date()}"
                )
            elif published_at:
                retrodict_config = RetrodictConfig(forecast_date=published_at)
                print(f"🔒 Blind mode: data restricted to before {published_at.date()}")
            else:
                print("⚠️  No published_at found, running without blind mode")

        # Setup logging
        log_file = setup_logging(qid)
        print(f"Logging to {log_file}")

        # Run forecast
        try:
            output = asyncio.run(run_forecast(qid, retrodict_config=retrodict_config))
            display_forecast(output)

            # Compute Brier score for binary questions
            brier = None
            if output.probability is not None and resolution in ("yes", "no"):
                outcome = 1.0 if resolution == "yes" else 0.0
                brier = (output.probability - outcome) ** 2
                print("\n📊 Calibration:")
                print(f"   Our forecast: {output.probability:.1%}")
                print(f"   Resolution: {resolution}")
                print(f"   Brier score: {brier:.4f}")
                if final_cp is not None:
                    cp_brier = (final_cp - outcome) ** 2
                    print(f"   CP Brier: {cp_brier:.4f}")
                    diff = brier - cp_brier
                    better_worse = "better" if diff < 0 else "worse"
                    print(f"   We were {abs(diff):.4f} {better_worse} than CP")

            results.append(
                {
                    "post_id": qid,
                    "resolution": resolution,
                    "our_forecast": output.probability,
                    "final_cp": final_cp,
                    "brier": brier,
                    "question_type": output.question_type,
                }
            )

        except CreditExhaustedError as e:
            reset_msg = ""
            if e.reset_time:
                reset_msg = f" Resets at {e.reset_time.strftime('%H:%M %Z')}."
            print(f"❌ Credit exhausted.{reset_msg}")
            results.append({"post_id": qid, "error": "credit_exhausted"})
        except httpx.HTTPStatusError as e:
            print(f"❌ Failed to fetch question: {e}")
            results.append({"post_id": qid, "error": str(e)})
        except RuntimeError as e:
            print(f"❌ Agent failed: {e}")
            results.append({"post_id": qid, "error": str(e)})

    # Summary
    print(f"\n{'=' * 60}")
    print("RETRODICT SUMMARY")
    print("=" * 60)

    binary_results = [r for r in results if r.get("brier") is not None]
    if binary_results:
        avg_brier = sum(r["brier"] for r in binary_results) / len(binary_results)
        print(f"\nBinary questions: {len(binary_results)}")
        print(f"Average Brier score: {avg_brier:.4f}")

        # Compare to CP
        cp_briers = [
            (r.get("final_cp", 0.5) - (1.0 if r["resolution"] == "yes" else 0.0)) ** 2
            for r in binary_results
            if r.get("final_cp") is not None
        ]
        if cp_briers:
            avg_cp_brier = sum(cp_briers) / len(cp_briers)
            print(f"Average CP Brier: {avg_cp_brier:.4f}")
            diff = avg_brier - avg_cp_brier
            print(
                f"Difference: {diff:+.4f} ({'worse' if diff > 0 else 'better'} than CP)"
            )

    errors = [r for r in results if "error" in r]
    if errors:
        print(f"\nErrors: {len(errors)}")
        for r in errors:
            print(f"  {r['post_id']}: {r['error']}")


@app.command()
def submit(
    question_id: Annotated[int, typer.Argument(help="Metaculus post ID")],
    comment: Annotated[
        bool,
        typer.Option(
            "--comment/--no-comment",
            "-c",
            help="Post reasoning as a private comment (required by tournament rules)",
        ),
    ] = True,
    use_cache: Annotated[
        bool,
        typer.Option(
            "--use-cache/--no-cache",
            help="Use cached forecast if available instead of re-running agent",
        ),
    ] = True,
) -> None:
    """Forecast a question and submit the prediction to Metaculus."""
    output: ForecastOutput | None = None

    # Try to load from cache if requested
    # Use allow_resubmit=True since user explicitly requested submission
    if use_cache:
        output = load_latest_for_submission(question_id, allow_resubmit=True)
        if output is not None:
            print(f"📂 Loaded cached forecast from notes/forecasts/{question_id}/")
            display_forecast(output)
        else:
            print("⚠️  No cached forecast found, running agent...")

    # Run forecast if not loaded from cache
    if output is None:
        log_file = setup_logging(question_id)
        print(f"Logging to {log_file}")

        try:
            output = asyncio.run(run_forecast(question_id))
            display_forecast(output)
        except CreditExhaustedError as e:
            reset_msg = ""
            if e.reset_time:
                reset_msg = f" Resets at {e.reset_time.strftime('%H:%M %Z')}."
            print(f"❌ Credit exhausted.{reset_msg}")
            raise typer.Exit(1)
        except httpx.HTTPStatusError as e:
            print(f"Failed to fetch question: {e}")
            raise typer.Exit(1)
        except RuntimeError as e:
            print(f"Agent failed: {e}")
            raise typer.Exit(1)

    print("Submitting forecast to Metaculus...")
    try:
        asyncio.run(submit_forecast(output))
        mark_submitted(output.post_id)
        print(
            f"✅ Forecast submitted (post {output.post_id} → question {output.question_id})"
        )
    except SubmissionError as e:
        print(f"❌ Submission failed: {e}")
        raise typer.Exit(1)

    if comment:
        print("Posting reasoning comment...")
        try:
            comment_text = format_reasoning_comment(output)
            # Comments use post_id, not question_id
            asyncio.run(post_comment(output.post_id, comment_text))
            print(f"✅ Comment posted on post {output.post_id}")
        except SubmissionError as e:
            print(f"⚠️  Comment failed (forecast was submitted): {e}")


# Known tournament IDs
TOURNAMENT_IDS = {
    "aib": "spring-aib-2026",
    "minibench": "minibench",
    "cup": 32921,
}


@app.command()
def tournament(
    tournament_id: Annotated[
        str,
        typer.Argument(
            help="Tournament ID or alias (aib, minibench, cup) or numeric ID"
        ),
    ] = "aib",
    skip_existing: Annotated[
        bool,
        typer.Option(
            "--skip-existing/--no-skip-existing",
            help="Skip questions that already have a local forecast",
        ),
    ] = True,
    comment: Annotated[
        bool,
        typer.Option(
            "--comment/--no-comment",
            "-c",
            help="Post reasoning as a private comment (required by tournament rules)",
        ),
    ] = True,
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", "-n", help="List questions without forecasting"),
    ] = False,
) -> None:
    """Forecast all open questions in a tournament and submit to Metaculus."""
    # Resolve tournament ID alias
    resolved_id: int | str
    if tournament_id in TOURNAMENT_IDS:
        resolved_id = TOURNAMENT_IDS[tournament_id]
    elif tournament_id.isdigit():
        resolved_id = int(tournament_id)
    else:
        resolved_id = tournament_id

    print(f"Fetching open questions from tournament: {resolved_id}")
    try:
        questions = asyncio.run(list_open_tournament_questions(resolved_id))
    except Exception as e:
        print(f"Failed to fetch tournament questions: {e}")
        raise typer.Exit(1)

    print(f"Found {len(questions)} open questions")

    if dry_run:
        for q in questions:
            status = "📝 Already forecast" if q.already_forecast else "⏳ Pending"
            print(f"  [{status}] {q.post_id}: {q.title[:60]}...")
        return

    # Track results
    success_count = 0
    skip_count = 0
    error_count = 0

    for i, q in enumerate(questions, 1):
        print(f"\n[{i}/{len(questions)}] Question {q.post_id}: {q.title[:50]}...")

        # Check for existing forecast (uses Metaculus API data)
        if skip_existing and q.already_forecast:
            print("  ⏭️  Skipping (already forecast on Metaculus)")
            skip_count += 1
            continue

        # Setup logging for this question
        log_file = setup_logging(q.post_id)
        print(f"  📝 Logging to {log_file}")

        # Run forecast with credit exhaustion retry
        output: ForecastOutput | None = None
        while True:
            try:
                output = asyncio.run(run_forecast(q.post_id))
                display_forecast(output)
                break
            except CreditExhaustedError as e:
                print(f"  ⚠️  {e}")
                wait_for_credit_reset(e)
                print(f"  🔄 Retrying {q.post_id}...")
            except httpx.HTTPStatusError as e:
                print(f"  ❌ Failed to fetch question: {e}")
                error_count += 1
                break
            except RuntimeError as e:
                print(f"  ❌ Agent failed: {e}")
                error_count += 1
                break

        if output is None:
            continue

        # Submit forecast
        print("  📤 Submitting forecast...")
        try:
            asyncio.run(submit_forecast(output))
            mark_submitted(output.post_id)
            print("  ✅ Forecast submitted")
            success_count += 1
        except SubmissionError as e:
            print(f"  ❌ Submission failed: {e}")
            error_count += 1
            continue

        # Post comment if requested
        if comment:
            try:
                comment_text = format_reasoning_comment(output)
                asyncio.run(post_comment(q.post_id, comment_text))
                print("  💬 Comment posted")
            except SubmissionError as e:
                print(f"  ⚠️  Comment failed: {e}")

    # Summary
    print(f"\n{'=' * 60}")
    print(
        f"Tournament complete: {success_count} submitted, {skip_count} skipped, {error_count} errors"
    )


@app.command()
def loop(
    tournaments: Annotated[
        list[str] | None,
        typer.Argument(
            help="Tournament IDs or aliases to loop over (default: aib minibench)"
        ),
    ] = None,
    interval: Annotated[
        int,
        typer.Option("--interval", "-i", help="Minutes between runs"),
    ] = 20,
    comment: Annotated[
        bool,
        typer.Option(
            "--comment/--no-comment",
            "-c",
            help="Post reasoning as a private comment (required by tournament rules)",
        ),
    ] = True,
    use_cache: Annotated[
        bool,
        typer.Option(
            "--use-cache/--no-cache",
            help="Use cached forecast if available instead of re-running agent",
        ),
    ] = True,
) -> None:
    """Continuously forecast tournaments in a loop.

    Runs forever, checking each tournament for new questions every INTERVAL minutes.
    Use Ctrl+C to stop.
    """
    if tournaments is None:
        tournaments = ["aib", "minibench"]

    print(f"Starting forecast loop for tournaments: {', '.join(tournaments)}")
    print(f"Interval: {interval} minutes")
    print("Press Ctrl+C to stop\n")

    while True:
        cycle_start = time.time()
        print(f"\n{'=' * 60}")
        print(f"Cycle started at {datetime.now(timezone.utc).isoformat()}")
        print("=" * 60)

        for tid in tournaments:
            # Resolve tournament ID alias
            resolved_id: int | str
            if tid in TOURNAMENT_IDS:
                resolved_id = TOURNAMENT_IDS[tid]
            elif tid.isdigit():
                resolved_id = int(tid)
            else:
                resolved_id = tid

            print(f"\n📊 Tournament: {tid} ({resolved_id})")

            try:
                questions = asyncio.run(list_open_tournament_questions(resolved_id))
            except Exception as e:
                print(f"  ❌ Failed to fetch questions: {e}")
                continue

            # Filter to only unforecast questions
            pending = [q for q in questions if not q.already_forecast]
            print(
                f"  Found {len(pending)} pending questions (of {len(questions)} open)"
            )

            for i, q in enumerate(pending, 1):
                print(f"\n  [{i}/{len(pending)}] {q.post_id}: {q.title[:50]}...")

                # Check if already submitted locally (API doesn't track this in listings)
                if use_cache and is_submitted(q.post_id):
                    print("    ⏭️  Already submitted (from local cache)")
                    continue

                output: ForecastOutput | None = None

                # Try cache first
                if use_cache:
                    output = load_latest_for_submission(q.post_id)
                    if output is not None:
                        print("    📂 Loaded from cache")
                        display_forecast(output)

                # Run agent if no cached forecast
                if output is None:
                    log_file = setup_logging(q.post_id)
                    print(f"    📝 Logging to {log_file}")

                    # Retry loop for credit exhaustion
                    while True:
                        try:
                            output = asyncio.run(run_forecast(q.post_id))
                            display_forecast(output)
                            break
                        except CreditExhaustedError as e:
                            print(f"    ⚠️  {e}")
                            wait_for_credit_reset(e)
                            print(f"    🔄 Retrying {q.post_id}...")
                        except httpx.HTTPStatusError as e:
                            print(f"    ❌ Failed to fetch: {e}")
                            output = None
                            break
                        except RuntimeError as e:
                            print(f"    ❌ Agent failed: {e}")
                            output = None
                            break

                if output is None:
                    continue

                print("    📤 Submitting...")
                try:
                    asyncio.run(submit_forecast(output))
                    mark_submitted(output.post_id)
                    print("    ✅ Submitted")
                except SubmissionError as e:
                    print(f"    ❌ Submission failed: {e}")
                    continue

                if comment:
                    try:
                        comment_text = format_reasoning_comment(output)
                        asyncio.run(post_comment(q.post_id, comment_text))
                        print("    💬 Comment posted")
                    except SubmissionError as e:
                        print(f"    ⚠️  Comment failed: {e}")

        cycle_duration = time.time() - cycle_start
        print(f"\n✅ Cycle complete in {cycle_duration:.0f}s")

        sleep_seconds = interval * 60
        next_run = datetime.now(timezone.utc).timestamp() + sleep_seconds
        next_run_str = datetime.fromtimestamp(next_run, timezone.utc).strftime(
            "%H:%M:%S UTC"
        )
        print(f"💤 Sleeping {interval} minutes (next run at {next_run_str})...")

        try:
            time.sleep(sleep_seconds)
        except KeyboardInterrupt:
            print("\n\n👋 Loop stopped by user")
            raise typer.Exit(0)


@app.command()
def backfill_comments(
    dry_run: Annotated[
        bool,
        typer.Option("--dry-run", "-n", help="List forecasts without posting comments"),
    ] = False,
    force: Annotated[
        bool,
        typer.Option(
            "--force", "-f", help="Post comments even if already marked as posted"
        ),
    ] = False,
) -> None:
    """Post private comments on all saved forecasts.

    Skips forecasts that already have comment_posted_at set (unless --force).
    Safe to run multiple times.
    """
    asyncio.run(_backfill_comments_async(dry_run, force))


async def _backfill_comments_async(dry_run: bool, force: bool) -> None:
    """Async implementation of backfill_comments."""
    import httpx

    from aib.agent.history import (
        FORECASTS_BASE_PATH,
        get_latest_forecast,
        has_comment,
        mark_comment_posted,
    )
    from aib.agent.models import Factor, ForecastOutput
    from aib.config import settings

    if not FORECASTS_BASE_PATH.exists():
        print("No forecasts directory found")
        raise typer.Exit(1)

    # Find all forecast directories
    forecast_dirs = sorted(
        [d for d in FORECASTS_BASE_PATH.iterdir() if d.is_dir() and d.name.isdigit()],
        key=lambda d: int(d.name),
    )

    print(f"Found {len(forecast_dirs)} forecast directories")

    success_count = 0
    skip_count = 0
    error_count = 0

    async with httpx.AsyncClient(timeout=30.0) as client:
        for d in forecast_dirs:
            post_id = int(d.name)

            # Check if already has comment (unless force)
            if not force and has_comment(post_id):
                print(f"  ⏭️  {post_id}: Already has comment")
                skip_count += 1
                continue

            saved = get_latest_forecast(post_id)

            if saved is None:
                print(f"  ⚠️  {post_id}: No forecast files found")
                skip_count += 1
                continue

            print(f"  📝 {post_id}: {saved.question_title[:50]}...")

            if dry_run:
                success_count += 1
                continue

            # Convert SavedForecast to ForecastOutput for format_reasoning_comment
            output = ForecastOutput(
                question_id=saved.question_id,
                post_id=saved.post_id or saved.question_id,
                question_title=saved.question_title,
                question_type=saved.question_type,
                summary=saved.summary,
                factors=[Factor.model_validate(f) for f in saved.factors],
                probability=saved.probability,
                logit=saved.logit,
                probabilities=saved.probabilities,
                median=saved.median,
                confidence_interval=saved.confidence_interval,
                percentiles=saved.percentiles,
            )

            comment_text = format_reasoning_comment(output)

            try:
                response = await client.post(
                    "https://www.metaculus.com/api/comments/create/",
                    json={
                        "text": comment_text,
                        "parent": None,
                        "included_forecast": True,
                        "is_private": True,
                        "on_post": post_id,
                    },
                    headers={"Authorization": f"Token {settings.metaculus_token}"},
                )

                if response.is_success:
                    mark_comment_posted(post_id)
                    print("    ✅ Comment posted")
                    success_count += 1
                else:
                    print(f"    ❌ Failed: {response.status_code}")
                    error_count += 1
                    if response.status_code in (429, 403):
                        print("    ⏳ Rate limited, waiting 30s...")
                        await asyncio.sleep(30)

            except httpx.HTTPError as e:
                print(f"    ❌ HTTP error: {e}")
                error_count += 1

            # Small delay between requests
            await asyncio.sleep(1)

    print(
        f"\nDone: {success_count} comments posted, {skip_count} skipped, {error_count} errors"
    )


if __name__ == "__main__":
    app()
