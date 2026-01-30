"""Forecasting agent using Claude Agent SDK."""

import dataclasses
import json
import logging
import uuid
from datetime import datetime
from pathlib import Path

import httpx
from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    TextBlock,
    ThinkingBlock,
    ToolUseBlock,
)

from aib.agent.models import (
    Forecast,
    ForecastOutput,
    MultipleChoiceForecast,
    NumericForecast,
)
from aib.agent.numeric import percentiles_to_cdf
from aib.agent.prompts import FORECASTING_SYSTEM_PROMPT, get_type_specific_guidance
from aib.agent.subagents import SUBAGENTS
from aib.tools import composition_server, forecasting_server, markets_server
from aib.tools.composition import set_run_forecast_fn
from aib.tools.sandbox import Sandbox

logger = logging.getLogger(__name__)

METACULUS_API_BASE = "https://www.metaculus.com/api"


def get_output_schema_for_question(
    question_type: str,
) -> tuple[type[Forecast | NumericForecast | MultipleChoiceForecast], dict]:
    """Return (model_class, json_schema) for question type.

    Args:
        question_type: Type of question (binary, numeric, discrete, multiple_choice)

    Returns:
        Tuple of (model class, JSON schema dict) for the appropriate forecast type.
    """
    if question_type == "multiple_choice":
        return MultipleChoiceForecast, MultipleChoiceForecast.model_json_schema()
    elif question_type in ("numeric", "discrete"):
        return NumericForecast, NumericForecast.model_json_schema()
    else:  # binary is default
        return Forecast, Forecast.model_json_schema()


# Notes folder base path
NOTES_BASE_PATH = Path("./notes")


def setup_notes_folder(session_id: str) -> dict[str, Path]:
    """Create session-specific notes folder structure.

    Structure:
    - notes/sessions/<session_id>/       (RW for this session)
    - notes/research/                    (RO - all research)
    - notes/research/<timestamp>/        (RW - this session's research)
    - notes/forecasts/                   (RO - all forecasts)
    - notes/forecasts/<timestamp>/       (RW - this session's forecast)

    Folders are created empty - the agent decides what files to create.
    Each note file should start with a one-line summary for quick scanning.

    Returns:
        Dict with paths for add_dirs config.
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    session_path = NOTES_BASE_PATH / "sessions" / session_id
    research_base = NOTES_BASE_PATH / "research"
    research_path = research_base / timestamp
    forecasts_base = NOTES_BASE_PATH / "forecasts"
    forecasts_path = forecasts_base / timestamp

    session_path.mkdir(parents=True, exist_ok=True)
    research_path.mkdir(parents=True, exist_ok=True)
    forecasts_path.mkdir(parents=True, exist_ok=True)

    return {
        "session": session_path,
        "research_base": research_base,
        "research": research_path,
        "forecasts_base": forecasts_base,
        "forecasts": forecasts_path,
    }


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
            "zero_point": scaling.get("zero_point"),  # For log-scaled questions
        }
        # For discrete questions, CDF size is inbound_outcome_count + 1
        if question_type == "discrete":
            inbound_outcome_count = scaling.get("inbound_outcome_count")
            if inbound_outcome_count is not None:
                context["numeric_bounds"]["cdf_size"] = inbound_outcome_count + 1

    return context


def extract_sources(messages: list[AssistantMessage]) -> list[str]:
    """Extract web sources from tool use blocks."""
    sources = []
    for msg in messages:
        for block in msg.content:
            if isinstance(block, ToolUseBlock) and block.name in (
                "WebSearch",
                "WebFetch",
                "mcp__forecasting__search_exa",
                "mcp__forecasting__search_news",
            ):
                if isinstance(block.input, dict):
                    source = block.input.get("url") or block.input.get("query")
                    if source:
                        sources.append(str(source))
    return sources


async def run_forecast(
    question_id: int | None = None,
    *,
    question_context: dict | None = None,
    allow_spawn: bool = True,
    stream_thinking: bool = False,
) -> ForecastOutput:
    """Run the forecasting agent on a question.

    Args:
        question_id: Metaculus post ID (for top-level forecasts)
        question_context: Pre-built context dict (for sub-forecasts from spawn_subquestions)
        allow_spawn: Whether this forecast can spawn subquestions (False for sub-forecasts)
        stream_thinking: Whether to print thinking blocks to stdout as they arrive

    Returns:
        ForecastOutput with the forecast results.
    """
    # Generate session ID
    session_id = str(uuid.uuid4())[:8]

    # Either fetch question or use provided context
    if question_context is not None:
        context = question_context
        question_title = context.get("title", "Sub-question")
        question_type = context.get("type", "binary")
        # Use a placeholder ID for sub-forecasts
        question_id = question_id or 0
        logger.info(
            "Starting sub-forecast session %s for: %s", session_id, question_title
        )
    elif question_id is not None:
        logger.info(
            "Starting forecast session %s for question %d", session_id, question_id
        )
        post_data = await fetch_question(question_id)
        question = post_data.get("question", {})
        question_title = question.get("title", "Unknown")
        question_type = question.get("type", "binary")
        context = build_question_context(post_data)
    else:
        raise ValueError("Either question_id or question_context must be provided")

    # Setup notes folder
    notes = setup_notes_folder(session_id)
    logger.info("Notes folder: %s", notes["session"])

    # Get type-specific output schema and guidance
    model_class, output_schema = get_output_schema_for_question(question_type)
    type_guidance = get_type_specific_guidance(question_type, context)

    prompt = f"Analyze this forecasting question and provide your forecast:\n\n{json.dumps(context, indent=2)}\n\n{type_guidance}"

    collected_text: list[str] = []
    assistant_messages: list[AssistantMessage] = []
    result: ResultMessage | None = None

    with Sandbox() as sandbox:
        options = ClaudeAgentOptions(
            model="claude-opus-4-5-20251101",
            system_prompt={
                "type": "preset",
                "preset": "claude_code",
                "append": FORECASTING_SYSTEM_PROMPT,
            },
            # Unlimited thinking tokens for deep reasoning
            max_thinking_tokens=None,
            permission_mode="bypassPermissions",
            # MCP servers for research and code execution
            mcp_servers={
                # In-process: forecasting tools (pure capabilities)
                "forecasting": forecasting_server,
                # In-process: Docker-based Python sandbox
                "sandbox": sandbox.create_mcp_server(),
                # In-process: composition tools (parallel research, subquestions)
                "composition": composition_server,
                # In-process: prediction market tools
                "markets": markets_server,
            },
            # Subagents for specialized research tasks
            agents=SUBAGENTS,
            # Notes folder access
            add_dirs=[
                str(notes["session"]),  # RW - current session
                str(notes["research_base"]),  # RO - all research
                str(notes["research"]),  # RW - this session's research
                str(notes["forecasts_base"]),  # RO - all forecasts
                str(notes["forecasts"]),  # RW - this session's forecast
            ],
            # Built-in tools + MCP tools (conditionally include spawn_subquestions)
            allowed_tools=[
                # Built-in web tools
                "WebSearch",
                "WebFetch",
                # File tools for notes
                "Read",
                "Write",
                "Glob",
                # Forecasting tools (mcp__<server>__<tool>)
                "mcp__forecasting__get_metaculus_question",
                "mcp__forecasting__list_tournament_questions",
                "mcp__forecasting__search_metaculus",
                "mcp__forecasting__get_coherence_links",
                "mcp__forecasting__search_exa",
                "mcp__forecasting__search_news",
                "mcp__forecasting__search_wikipedia",
                # Sandbox tools (in-process Docker sandbox)
                "mcp__sandbox__execute_code",
                "mcp__sandbox__install_package",
                # Composition tools (parallel execution)
                "mcp__composition__parallel_research",
                "mcp__composition__parallel_market_search",
                # spawn_subquestions only available for top-level forecasts
                *(["mcp__composition__spawn_subquestions"] if allow_spawn else []),
                # Prediction market tools
                "mcp__markets__polymarket_price",
                "mcp__markets__manifold_price",
                # Subagent spawning
                "Task",
            ],
            output_format={
                "type": "json_schema",
                "schema": output_schema,
            },
        )

        async with ClaudeSDKClient(options=options) as client:
            await client.query(prompt)

            async for message in client.receive_messages():
                if isinstance(message, AssistantMessage):
                    assistant_messages.append(message)
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            collected_text.append(block.text)
                        elif isinstance(block, ThinkingBlock):
                            # Log thinking blocks for visibility into agent reasoning
                            thinking_text = block.thinking if hasattr(block, 'thinking') else str(block)
                            logger.debug("Thinking: %s", thinking_text[:200] + "..." if len(thinking_text) > 200 else thinking_text)
                            if stream_thinking:
                                print(f"\n💭 [Thinking]\n{thinking_text}\n")
                        elif isinstance(block, ToolUseBlock):
                            logger.debug("Tool: %s", dataclasses.asdict(block))
                            if stream_thinking:
                                print(f"🔧 Tool: {block.name}")

                elif isinstance(message, ResultMessage):
                    result = message
                    if message.is_error:
                        raise RuntimeError(f"Agent error: {message.result}")

    if result is None:
        raise RuntimeError("No result received from agent")

    # Extract structured forecast based on question type
    output = ForecastOutput(
        question_id=question_id,
        question_title=question_title,
        question_type=question_type,
        summary="No forecast produced",
        factors=[],
        reasoning="".join(collected_text),
        sources_consulted=extract_sources(assistant_messages),
        duration_seconds=(result.duration_ms / 1000) if result.duration_ms else None,
        cost_usd=result.total_cost_usd,
    )

    if result.structured_output:
        forecast = model_class.model_validate(result.structured_output)
        output.summary = forecast.summary
        output.factors = forecast.factors

        if isinstance(forecast, Forecast):
            output.logit = forecast.logit
            output.probability = forecast.probability
            output.probability_from_logit = forecast.probability_from_logit
        elif isinstance(forecast, NumericForecast):
            output.median = forecast.median
            output.confidence_interval = forecast.confidence_interval
            output.percentiles = forecast.get_percentile_dict()

            # Generate CDF from percentiles
            bounds = context.get("numeric_bounds", {})
            if bounds.get("range_min") is not None and bounds.get("range_max") is not None:
                try:
                    output.cdf = percentiles_to_cdf(
                        output.percentiles,
                        upper_bound=bounds["range_max"],
                        lower_bound=bounds["range_min"],
                        open_upper_bound=bounds.get("open_upper_bound", False),
                        open_lower_bound=bounds.get("open_lower_bound", False),
                        zero_point=bounds.get("zero_point"),
                        cdf_size=bounds.get("cdf_size", 201),
                    )
                    logger.info("Generated %d-point CDF", len(output.cdf))
                except Exception as e:
                    logger.exception("Failed to generate CDF: %s", e)
                    output.cdf = None
        elif isinstance(forecast, MultipleChoiceForecast):
            output.probabilities = forecast.probabilities
    else:
        logger.warning("No structured output; using default forecast")
        if question_type == "binary":
            output.logit = 0.0
            output.probability = 0.5
        elif question_type in ("numeric", "discrete"):
            output.median = 0.0
            output.confidence_interval = (0.0, 0.0)
        elif question_type == "multiple_choice":
            output.probabilities = {}

    return output


# Wire up spawn_subquestions to use run_forecast recursively
set_run_forecast_fn(run_forecast)
