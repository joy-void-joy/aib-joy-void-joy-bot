"""Metaculus forecast submission."""

import logging
from dataclasses import dataclass

import httpx
from forecasting_tools import MetaculusClient

from aib.agent.models import ForecastOutput
from aib.config import settings

logger = logging.getLogger(__name__)

METACULUS_API_BASE = "https://www.metaculus.com/api"


class SubmissionError(Exception):
    """Error during forecast submission."""


@dataclass
class TournamentQuestion:
    """Lightweight question info from tournament listing."""

    post_id: int
    title: str
    question_type: str
    url: str
    already_forecast: bool = False


def list_open_tournament_questions(tournament_id: int | str) -> list[TournamentQuestion]:
    """List all open questions from a tournament.

    Args:
        tournament_id: Tournament ID (int) or slug (str).

    Returns:
        List of TournamentQuestion objects for open questions.
        Each question includes `already_forecast` flag from Metaculus API.
    """
    client = MetaculusClient()
    questions = client.get_all_open_questions_from_tournament(tournament_id)

    results = []
    for q in questions:
        post_id = q.id_of_post
        url = q.page_url
        if post_id is None or url is None:
            logger.warning("Skipping question with missing post_id or url: %s", q.question_text)
            continue

        # Check if we've already forecast this question using Metaculus API
        already_forecast = q.timestamp_of_my_last_forecast is not None

        results.append(
            TournamentQuestion(
                post_id=post_id,
                title=q.question_text,
                question_type=q.get_question_type(),
                url=url,
                already_forecast=already_forecast,
            )
        )
    return results


def create_forecast_payload(output: ForecastOutput) -> dict:
    """Convert a ForecastOutput to the Metaculus API payload format.

    Args:
        output: The forecast output to convert.

    Returns:
        Dict with probability_yes, probability_yes_per_category, or continuous_cdf
        depending on question type.

    Raises:
        SubmissionError: If the output is missing required fields for its type.
    """
    question_type = output.question_type

    if question_type == "binary":
        if output.probability is None:
            raise SubmissionError("Binary forecast missing probability")
        return {
            "probability_yes": output.probability,
            "probability_yes_per_category": None,
            "continuous_cdf": None,
        }

    if question_type == "multiple_choice":
        if not output.probabilities:
            raise SubmissionError("Multiple choice forecast missing probabilities")
        return {
            "probability_yes": None,
            "probability_yes_per_category": output.probabilities,
            "continuous_cdf": None,
        }

    if question_type in ("numeric", "discrete"):
        if not output.cdf:
            raise SubmissionError(
                f"{question_type.capitalize()} forecast missing CDF. "
                "Ensure numeric bounds are available and percentiles/components are valid."
            )
        if len(output.cdf) != 201:
            raise SubmissionError(
                f"CDF must have exactly 201 points, got {len(output.cdf)}"
            )
        return {
            "probability_yes": None,
            "probability_yes_per_category": None,
            "continuous_cdf": output.cdf,
        }

    raise SubmissionError(f"Unsupported question type: {question_type}")


async def submit_forecast(output: ForecastOutput) -> None:
    """Submit a forecast to Metaculus.

    Args:
        output: The forecast output to submit.

    Raises:
        SubmissionError: If the submission fails.
    """
    payload = create_forecast_payload(output)

    request_body = [
        {
            "question": output.question_id,
            **payload,
        }
    ]

    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{METACULUS_API_BASE}/questions/forecast/",
            json=request_body,
            headers={"Authorization": f"Token {settings.metaculus_token}"},
            timeout=30.0,
        )

        if response.status_code == 400:
            error_detail = response.text
            if "already closed" in error_detail.lower():
                raise SubmissionError(
                    f"Question {output.question_id} is already closed"
                )
            raise SubmissionError(f"Bad request: {error_detail}")

        if response.status_code == 401:
            raise SubmissionError("Invalid Metaculus token")

        if response.status_code == 403:
            raise SubmissionError(
                f"Not authorized to forecast on question {output.question_id}"
            )

        if not response.is_success:
            raise SubmissionError(
                f"Submission failed with status {response.status_code}: {response.text}"
            )

    logger.info("Submitted forecast for question %d", output.question_id)


async def post_comment(
    post_id: int,
    comment_text: str,
    *,
    include_forecast: bool = True,
    is_private: bool = True,
) -> None:
    """Post a comment on a Metaculus question.

    Args:
        post_id: The post ID to comment on.
        comment_text: The comment text (markdown supported).
        include_forecast: Whether to include the forecast with the comment.
        is_private: Whether the comment is private (only visible to the author).

    Raises:
        SubmissionError: If posting the comment fails.
    """
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{METACULUS_API_BASE}/comments/create/",
            json={
                "text": comment_text,
                "parent": None,
                "included_forecast": include_forecast,
                "is_private": is_private,
                "on_post": post_id,
            },
            headers={"Authorization": f"Token {settings.metaculus_token}"},
            timeout=30.0,
        )

        if not response.is_success:
            raise SubmissionError(
                f"Comment failed with status {response.status_code}: {response.text}"
            )

    logger.info("Posted comment on post %d", post_id)


def format_reasoning_comment(output: ForecastOutput) -> str:
    """Format a ForecastOutput into a markdown comment for Metaculus.

    Args:
        output: The forecast output to format.

    Returns:
        Markdown-formatted comment string.
    """
    lines = [f"## Forecast Summary\n\n{output.summary}"]

    if output.probability is not None:
        lines.append(f"\n**Probability:** {output.probability * 100:.1f}%")

    if output.probabilities:
        lines.append("\n**Probabilities:**")
        for option, prob in output.probabilities.items():
            lines.append(f"- {option}: {prob * 100:.1f}%")

    if output.median is not None:
        lines.append(f"\n**Median estimate:** {output.median}")
        if output.confidence_interval:
            lo, hi = output.confidence_interval
            lines.append(f"**90% CI:** [{lo}, {hi}]")

    if output.factors:
        lines.append("\n## Key Factors\n")
        for factor in output.factors:
            sign = "+" if factor.logit >= 0 else ""
            lines.append(f"- [{sign}{factor.logit:.1f}] {factor.description}")

    if output.sources_consulted:
        lines.append(f"\n---\n*Sources consulted: {len(output.sources_consulted)}*")

    return "\n".join(lines)
