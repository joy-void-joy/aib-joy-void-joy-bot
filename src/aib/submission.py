"""Metaculus forecast submission."""

import logging
from dataclasses import dataclass

import httpx

from aib.agent.models import ForecastOutput
from aib.clients.metaculus import get_client
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


async def list_open_tournament_questions(
    tournament_id: int | str,
) -> list[TournamentQuestion]:
    """List all open questions from a tournament.

    Args:
        tournament_id: Tournament ID (int) or slug (str).

    Returns:
        List of TournamentQuestion objects for open questions.
        Each question includes `already_forecast` flag from Metaculus API.
    """
    client = get_client()
    questions = await client.get_all_open_questions_from_tournament(tournament_id)

    results = []
    for q in questions:
        post_id = q.id_of_post
        url = q.page_url
        if post_id is None or url is None:
            logger.warning(
                "Skipping question with missing post_id or url: %s", q.question_text
            )
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
        # Validate CDF size: 201 for numeric, variable for discrete
        expected_size = output.cdf_size or 201
        if len(output.cdf) != expected_size:
            raise SubmissionError(
                f"CDF must have exactly {expected_size} points, got {len(output.cdf)}"
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


def format_reasoning_comment(output: ForecastOutput, *, max_length: int = 15000) -> str:
    """Format a ForecastOutput into a markdown comment for Metaculus.

    Tournament rules require bots to leave comments showing reasoning.
    This function produces a structured comment with:
    - Summary and forecast values
    - Key factors with directional weights
    - Full reasoning trace (if available)
    - Sources consulted

    Args:
        output: The forecast output to format.
        max_length: Maximum comment length. Reasoning is truncated if needed.

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
            conf_note = (
                f" (conf: {factor.confidence:.0%})" if factor.confidence < 1 else ""
            )
            lines.append(
                f"- [{sign}{factor.logit:.1f}] {factor.description}{conf_note}"
            )

    # Include reasoning trace if available
    if output.reasoning:
        lines.append("\n## Reasoning Trace\n")
        # Reserve space for other sections
        current_length = len("\n".join(lines))
        sources_estimate = 500 if output.sources_consulted else 50
        available = max_length - current_length - sources_estimate

        if len(output.reasoning) <= available:
            lines.append(output.reasoning)
        else:
            truncated = output.reasoning[: available - 50]
            # Try to cut at a paragraph or sentence boundary
            for sep in ["\n\n", "\n", ". "]:
                idx = truncated.rfind(sep)
                if idx > available * 0.7:
                    truncated = truncated[: idx + len(sep)]
                    break
            lines.append(truncated.strip())
            lines.append("\n*[Reasoning truncated for length]*")

    # Include actual sources (top 10)
    if output.sources_consulted:
        lines.append("\n## Sources Consulted\n")
        sources_to_show = output.sources_consulted[:10]
        for source in sources_to_show:
            # Format as bullet, handling URLs and queries
            if source.startswith("http"):
                lines.append(f"- {source}")
            else:
                lines.append(f"- {source}")
        if len(output.sources_consulted) > 10:
            lines.append(
                f"\n*...and {len(output.sources_consulted) - 10} more sources*"
            )
    else:
        lines.append("\n---\n*No sources recorded*")

    # Meta info
    if output.meta:
        meta_parts = []
        if output.meta.subagents_used:
            meta_parts.append(f"Subagents: {', '.join(output.meta.subagents_used)}")
        if output.meta.tools_used_count:
            meta_parts.append(f"Tool calls: {output.meta.tools_used_count}")
        if meta_parts:
            lines.append(f"\n---\n*{' | '.join(meta_parts)}*")

    return "\n".join(lines)
