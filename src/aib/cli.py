"""Metaculus Forecasting Bot - CLI Entry Point."""

import asyncio
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Annotated

import httpx
import typer

from aib.agent import ForecastOutput, run_forecast

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


def setup_logging(question_id: int, verbose: bool) -> Path:
    """Configure logging to console and file.

    Returns the path to the log file.
    """
    level = logging.DEBUG if verbose else logging.INFO
    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    datefmt = "%H:%M:%S"

    # Create log directory for this question
    log_dir = LOGS_BASE_PATH / str(question_id)
    log_dir.mkdir(parents=True, exist_ok=True)

    # Timestamped log file
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    log_file = log_dir / f"{timestamp}.log"

    # Configure root logger with both console and file handlers
    root_logger = logging.getLogger()
    root_logger.setLevel(level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(logging.Formatter(fmt, datefmt))
    root_logger.addHandler(console_handler)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)  # Always capture DEBUG to file
    file_handler.setFormatter(
        logging.Formatter("%(asctime)s %(levelname)s %(name)s: %(message)s")
    )
    root_logger.addHandler(file_handler)

    return log_file


@app.command()
def test(
    question_id: Annotated[int, typer.Argument(help="Metaculus question/post ID")],
    verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False,
    stream: Annotated[
        bool,
        typer.Option("--stream", "-s", help="Stream thinking blocks as they arrive"),
    ] = False,
) -> None:
    """Test forecasting on a single question without submitting."""
    log_file = setup_logging(question_id, verbose)
    logger.info("Logging to %s", log_file)

    try:
        output = asyncio.run(run_forecast(question_id, stream_thinking=stream))
        display_forecast(output)

        if verbose:
            print("Full reasoning:")
            print(output.reasoning)

    except httpx.HTTPStatusError as e:
        logger.error("Failed to fetch question: %s", e)
        raise typer.Exit(1)
    except RuntimeError as e:
        logger.error("Agent failed: %s", e)
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
