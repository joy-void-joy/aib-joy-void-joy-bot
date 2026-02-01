"""Composition tools for sub-forecasting.

These tools enable the main forecasting agent to:
- Decompose questions and forecast sub-questions in parallel
"""

import asyncio
import logging
from typing import Any, Required, TypedDict

from claude_agent_sdk import create_sdk_mcp_server, tool

from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


# --- Run Forecast Reference (set by core.py) ---

# Reference to run_forecast function - set by core.py to avoid circular import
_run_forecast_fn: Any = None


def set_run_forecast_fn(fn: Any) -> None:
    """Set the run_forecast function reference.

    Called by core.py after run_forecast is defined to enable
    spawn_subquestions to recursively call the forecasting agent.
    """
    global _run_forecast_fn
    _run_forecast_fn = fn


# --- Input Schemas ---


class SubQuestion(TypedDict, total=False):
    """A sub-question for parallel forecasting.

    Attributes:
        question: The sub-question text.
        context: How this relates to the parent question.
        weight: Optional weight for agent's own synthesis (default: 1.0).
        type: Question type: "binary" (default), "numeric", or "multiple_choice".
        options: For multiple_choice questions, list of option labels.
        numeric_bounds: For numeric questions, dict with range_min, range_max, etc.
    """

    question: Required[str]
    context: str
    weight: float  # Optional, default 1.0; for agent's synthesis reference
    type: str  # "binary", "numeric", or "multiple_choice" (default: binary)
    options: list[str]  # For multiple_choice
    numeric_bounds: dict[str, Any]  # For numeric questions


class SpawnSubquestionsInput(TypedDict):
    """Input for spawn_subquestions tool."""

    subquestions: list[SubQuestion]


# --- Output Schemas ---


class SubForecastResult(TypedDict):
    """Result from a single sub-forecast."""

    question: str
    type: str
    summary: str | None
    weight: float
    error: str | None


# --- Tools ---


@tool(
    "spawn_subquestions",
    (
        "Decompose a forecasting question into sub-questions and forecast each in "
        "parallel. Each sub-question gets its own forecasting agent with full research "
        "capabilities. Returns all individual sub-forecasts for you to synthesize. "
        "No automatic aggregation — you decide how to combine results."
    ),
    SpawnSubquestionsInput,
)
@tracked("spawn_subquestions")
async def spawn_subquestions(args: SpawnSubquestionsInput) -> dict[str, Any]:
    """Spawn parallel sub-forecasters for decomposed questions.

    Recursively calls run_forecast() for each sub-question with allow_spawn=False
    to prevent infinite recursion. Returns all individual sub-forecasts without
    aggregation — the calling agent decides how to synthesize results.
    """
    if _run_forecast_fn is None:
        return mcp_error("run_forecast not configured - call set_run_forecast_fn first")

    subquestions = args["subquestions"]

    if not subquestions:
        return mcp_error("No subquestions provided")

    async def run_subforecast(sq: SubQuestion) -> dict[str, Any]:
        """Execute a single sub-forecast."""
        question_type = sq.get("type", "binary")

        # Build context for the sub-question
        context: dict[str, Any] = {
            "title": sq["question"],
            "type": question_type,
            "description": sq.get("context", ""),
            "resolution_criteria": "",
            "fine_print": "",
        }

        # Add type-specific context
        if question_type == "multiple_choice" and "options" in sq:
            context["options"] = sq["options"]
        elif question_type in ("numeric", "discrete") and "numeric_bounds" in sq:
            context["numeric_bounds"] = sq["numeric_bounds"]

        try:
            result = await _run_forecast_fn(
                question_context=context,
                allow_spawn=False,  # Prevent infinite recursion
            )

            # Build response based on question type
            response: dict[str, Any] = {
                "question": sq["question"],
                "type": question_type,
                "summary": result.summary,
                "weight": sq.get("weight", 1.0),  # Default weight 1.0
                "error": None,
            }

            if question_type == "binary":
                response["probability"] = result.probability
            elif question_type in ("numeric", "discrete"):
                response["median"] = result.median
                response["confidence_interval"] = result.confidence_interval
                response["percentiles"] = result.percentiles
            elif question_type == "multiple_choice":
                response["probabilities"] = result.probabilities

            return response

        except Exception as e:
            logger.exception("Sub-forecast failed: %s", sq["question"])
            return {
                "question": sq["question"],
                "type": question_type,
                "summary": None,
                "weight": sq.get("weight", 1.0),
                "error": str(e),
            }

    # Run all sub-forecasts in parallel
    results = await asyncio.gather(*[run_subforecast(sq) for sq in subquestions])

    # Separate results by success status
    errors = [r for r in results if r.get("error") is not None]
    successful = [r for r in results if r.get("error") is None]

    if not successful:
        error_msgs = [e["error"] for e in errors]
        return mcp_error(f"All sub-forecasts failed: {error_msgs}")

    # Return all results without aggregation — agent synthesizes
    output: dict[str, Any] = {
        "subforecasts": list(results),
        "successful_count": len(successful),
        "failed_count": len(errors),
    }

    return mcp_success(output)


# --- MCP Server ---

composition_server = create_sdk_mcp_server(
    name="composition",
    version="2.0.0",
    tools=[
        spawn_subquestions,
    ],
)
