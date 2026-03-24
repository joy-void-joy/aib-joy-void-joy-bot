"""Metaculus forecast submission."""

import logging
from dataclasses import dataclass

import httpx

from aib.agent.models import ForecastOutput, NumericSupport
from aib.clients.metaculus import get_client

logger = logging.getLogger(__name__)


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
        return {"probability_yes": max(0.001, min(0.999, output.probability))}

    if question_type == "multiple_choice":
        if not output.probabilities:
            raise SubmissionError("Multiple choice forecast missing probabilities")
        clamped = {k: max(0.001, min(0.999, v)) for k, v in output.probabilities.items()}
        total = sum(clamped.values())
        normalized = {k: v / total for k, v in clamped.items()}
        return {"probability_yes_per_category": normalized}

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
        return {"continuous_cdf": output.cdf}

    raise SubmissionError(f"Unsupported question type: {question_type}")


async def submit_forecast(output: ForecastOutput) -> None:
    """Submit a forecast to Metaculus.

    Args:
        output: The forecast output to submit.

    Raises:
        SubmissionError: If the submission fails.
    """
    payload = create_forecast_payload(output)
    client = get_client()

    try:
        await client.post_question_prediction(output.question_id, payload)
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        detail = e.response.text
        if status == 400:
            if "already closed" in detail.lower():
                raise SubmissionError(
                    f"Question {output.question_id} is already closed"
                ) from e
            raise SubmissionError(f"Bad request: {detail}") from e
        if status == 401:
            raise SubmissionError("Invalid Metaculus token") from e
        if status == 403:
            raise SubmissionError(
                f"Not authorized to forecast on question {output.question_id}"
            ) from e
        raise SubmissionError(
            f"Submission failed with status {status}: {detail}"
        ) from e

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
    client = get_client()
    try:
        await client.post_question_comment(
            post_id,
            comment_text,
            is_private=is_private,
            included_forecast=include_forecast,
        )
    except httpx.HTTPStatusError as e:
        raise SubmissionError(
            f"Comment failed with status {e.response.status_code}: {e.response.text}"
        ) from e


def format_reasoning_comment(output: ForecastOutput) -> str:
    """Format a ForecastOutput into a markdown comment for Metaculus.

    Tournament rules require bots to leave comments showing reasoning.
    This function produces a structured comment with:
    - Summary and forecast values
    - Key factors with directional weights
    - Sources consulted (deduplicated URLs)

    Args:
        output: The forecast output to format.

    Returns:
        Markdown-formatted comment string.
    """
    lines: list[str] = []

    if output.reasoning:
        lines.append(output.reasoning)

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

    if output.condensed_reasoning:
        lines.append(f"\n## Reasoning\n\n{output.condensed_reasoning}")

    if output.factors:
        lines.append("\n## Key Factors\n")
        for factor in output.factors:
            conf_note = (
                f" (conf: {factor.confidence:.0%})" if factor.confidence < 1 else ""
            )
            if isinstance(factor.supports, NumericSupport):
                lines.append(
                    f"- [{factor.supports.center} ({factor.supports.low}–{factor.supports.high}), "
                    f"{factor.logit:+.1f}] {factor.description}{conf_note}"
                )
            elif factor.supports is not None:
                lines.append(
                    f"- [{factor.supports}, {factor.logit:+.1f}] {factor.description}{conf_note}"
                )
            else:
                lines.append(f"- [{factor.logit:+.1f}] {factor.description}{conf_note}")

    if output.sources_consulted:
        lines.append("\n## Sources\n")
        for source in output.sources_consulted:
            lines.append(f"- {source}")

    # Meta info
    from aib.version import AGENT_VERSION

    meta_parts = [f"Agent: v{AGENT_VERSION}"]
    if output.meta:
        if output.meta.subagents_used:
            meta_parts.append(f"Sub-questions: {', '.join(output.meta.subagents_used)}")
        if output.meta.tools_used_count:
            meta_parts.append(f"Tool calls: {output.meta.tools_used_count}")
    lines.append(f"\n---\n*{' | '.join(meta_parts)}*")

    return "\n".join(lines)
