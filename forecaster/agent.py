"""Forecasting agent using Claude Agent SDK."""

import dataclasses
import json
import logging

import httpx
from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
)

from forecaster.models import Forecast, ForecastOutput
from forecaster.prompts import FORECASTING_SYSTEM_PROMPT

logger = logging.getLogger(__name__)

METACULUS_API_BASE = "https://www.metaculus.com/api"


async def fetch_question(question_id: int, token: str | None = None) -> dict:
    """Fetch question details from Metaculus API."""
    headers = {"Authorization": f"Token {token}"} if token else {}

    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{METACULUS_API_BASE}/posts/{question_id}/",
            headers=headers,
        )
        response.raise_for_status()
        return response.json()


def build_question_context(post_data: dict) -> dict:
    """Extract relevant question data for the agent prompt."""
    question = post_data.get("question", {})
    question_type = question.get("type", "binary")

    context = {
        "title": question.get("title", "Unknown"),
        "type": question_type,
        "description": post_data.get("description") or question.get("description", ""),
        "resolution_criteria": question.get("resolution_criteria", ""),
        "fine_print": question.get("fine_print", ""),
        "scheduled_close_time": question.get("scheduled_close_time"),
    }

    if question_type == "multiple_choice":
        context["options"] = question.get("options", [])

    if question_type in ("numeric", "discrete"):
        scaling = question.get("scaling", {})
        context["numeric_bounds"] = {
            "range_min": scaling.get("range_min"),
            "range_max": scaling.get("range_max"),
            "open_lower_bound": question.get("open_lower_bound", False),
            "open_upper_bound": question.get("open_upper_bound", False),
        }

    return context


def extract_sources(messages: list[AssistantMessage]) -> list[str]:
    """Extract web sources from tool use blocks."""
    sources = []
    for msg in messages:
        for block in msg.content:
            if isinstance(block, ToolUseBlock) and block.name in (
                "WebSearch",
                "WebFetch",
            ):
                if isinstance(block.input, dict):
                    source = block.input.get("url") or block.input.get("query")
                    if source:
                        sources.append(str(source))
    return sources


async def run_forecast(question_id: int) -> ForecastOutput:
    """Run the forecasting agent on a question."""
    logger.info("Fetching question %d", question_id)
    post_data = await fetch_question(question_id)

    question = post_data.get("question", {})
    question_title = question.get("title", "Unknown")
    question_type = question.get("type", "binary")

    context = build_question_context(post_data)
    prompt = f"Analyze this forecasting question and provide your forecast:\n\n{json.dumps(context, indent=2)}"

    options = ClaudeAgentOptions(
        model="claude-opus-4-5-20251101",
        system_prompt={
            "type": "preset",
            "preset": "claude_code",
            "append": FORECASTING_SYSTEM_PROMPT,
        },
        permission_mode="bypassPermissions",
        allowed_tools=["WebSearch", "WebFetch", "Bash", "Read", "Write"],
        output_format={"type": "json_schema", "schema": Forecast.model_json_schema()},
    )

    collected_text: list[str] = []
    assistant_messages: list[AssistantMessage] = []
    result: ResultMessage | None = None

    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)

        async for message in client.receive_messages():
            if isinstance(message, AssistantMessage):
                assistant_messages.append(message)
                for block in message.content:
                    if isinstance(block, TextBlock):
                        collected_text.append(block.text)
                    elif isinstance(block, ToolUseBlock):
                        logger.debug("Tool: %s", dataclasses.asdict(block))

            elif isinstance(message, ResultMessage):
                result = message
                if message.is_error:
                    raise RuntimeError(f"Agent error: {message.result}")

    if result is None:
        raise RuntimeError("No result received from agent")

    # Extract structured forecast
    if result.structured_output:
        forecast = Forecast.model_validate(result.structured_output)
    else:
        logger.warning("No structured output; using default forecast")
        forecast = Forecast(
            summary="No forecast produced", factors=[], logit=0.0, probability=0.5
        )

    return ForecastOutput(
        question_id=question_id,
        question_title=question_title,
        question_type=question_type,
        summary=forecast.summary,
        factors=forecast.factors,
        logit=forecast.logit,
        probability=forecast.probability,
        probability_from_logit=forecast.probability_from_logit,
        reasoning="".join(collected_text),
        sources_consulted=extract_sources(assistant_messages),
        duration_seconds=(result.duration_ms / 1000) if result.duration_ms else None,
        cost_usd=result.total_cost_usd,
    )
