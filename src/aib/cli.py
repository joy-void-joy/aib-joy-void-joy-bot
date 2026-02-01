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
    except httpx.HTTPStatusError as e:
        print(f"Failed to fetch question: {e}")
        raise typer.Exit(1)
    except RuntimeError as e:
        print(f"Agent failed: {e}")
        raise typer.Exit(1)


@app.command()
def submit(
    question_id: Annotated[int, typer.Argument(help="Metaculus question/post ID")],
    comment: Annotated[
        bool,
        typer.Option("--comment", "-c", help="Post reasoning as a private comment"),
    ] = False,
) -> None:
    """Forecast a question and submit the prediction to Metaculus."""
    log_file = setup_logging(question_id)
    print(f"Logging to {log_file}")

    try:
        output = asyncio.run(run_forecast(question_id))
        display_forecast(output)
    except httpx.HTTPStatusError as e:
        print(f"Failed to fetch question: {e}")
        raise typer.Exit(1)
    except RuntimeError as e:
        print(f"Agent failed: {e}")
        raise typer.Exit(1)

    print("Submitting forecast to Metaculus...")
    try:
        asyncio.run(submit_forecast(output))
        print(f"✅ Forecast submitted for question {question_id}")
    except SubmissionError as e:
        print(f"❌ Submission failed: {e}")
        raise typer.Exit(1)

    if comment:
        print("Posting reasoning comment...")
        try:
            comment_text = format_reasoning_comment(output)
            asyncio.run(post_comment(question_id, comment_text))
            print(f"✅ Comment posted on question {question_id}")
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
        typer.Option("--comment", "-c", help="Post reasoning as a private comment"),
    ] = False,
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

        # Run forecast
        try:
            output = asyncio.run(run_forecast(q.post_id))
            display_forecast(output)
        except httpx.HTTPStatusError as e:
            print(f"  ❌ Failed to fetch question: {e}")
            error_count += 1
            continue
        except RuntimeError as e:
            print(f"  ❌ Agent failed: {e}")
            error_count += 1
            continue

        # Submit forecast
        print("  📤 Submitting forecast...")
        try:
            asyncio.run(submit_forecast(output))
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
        typer.Option("--comment", "-c", help="Post reasoning as a private comment"),
    ] = False,
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
            print(f"  Found {len(pending)} pending questions (of {len(questions)} open)")

            for i, q in enumerate(pending, 1):
                print(f"\n  [{i}/{len(pending)}] {q.post_id}: {q.title[:50]}...")

                log_file = setup_logging(q.post_id)
                print(f"    📝 Logging to {log_file}")

                try:
                    output = asyncio.run(run_forecast(q.post_id))
                    display_forecast(output)
                except httpx.HTTPStatusError as e:
                    print(f"    ❌ Failed to fetch: {e}")
                    continue
                except RuntimeError as e:
                    print(f"    ❌ Agent failed: {e}")
                    continue

                print("    📤 Submitting...")
                try:
                    asyncio.run(submit_forecast(output))
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


if __name__ == "__main__":
    app()
