"""Metaculus Forecasting Bot - CLI Entry Point."""

import asyncio
import logging
from typing import Annotated

import httpx
import typer

from . import ForecastOutput, run_forecast

app = typer.Typer(help="Metaculus AI Benchmarking Forecasting Bot")
logger = logging.getLogger(__name__)


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
    print()


@app.command()
def test(
    question_id: Annotated[int, typer.Argument(help="Metaculus question/post ID")],
    verbose: Annotated[bool, typer.Option("--verbose", "-v")] = False,
) -> None:
    """Test forecasting on a single question without submitting."""
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )

    try:
        output = asyncio.run(run_forecast(question_id))
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
