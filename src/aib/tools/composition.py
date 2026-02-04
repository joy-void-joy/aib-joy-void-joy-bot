"""Composition tools for sub-forecasting.

These tools enable the main forecasting agent to:
- Decompose questions and forecast sub-questions in parallel
"""

import asyncio
import logging
from typing import Any

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.tools.mcp_server import create_mcp_server

from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.validation import validate_input

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


class SubQuestionInput(BaseModel):
    """A sub-question for parallel forecasting."""

    question: str
    context: str = ""
    weight: float = 1.0
    type: str = "binary"
    options: list[str] = Field(default_factory=list)
    numeric_bounds: dict[str, Any] = Field(default_factory=dict)


class SpawnSubquestionsInput(BaseModel):
    """Input for spawn_subquestions tool."""

    subquestions: list[SubQuestionInput] = Field(min_length=1)


# --- Output Schemas ---


class SubForecastResult(BaseModel):
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
    {"subquestions": list},
)
@tracked("spawn_subquestions")
async def spawn_subquestions(args: dict[str, Any]) -> dict[str, Any]:
    """Spawn parallel sub-forecasters for decomposed questions.

    Recursively calls run_forecast() for each sub-question with allow_spawn=False
    to prevent infinite recursion. Returns all individual sub-forecasts without
    aggregation — the calling agent decides how to synthesize results.
    """
    if _run_forecast_fn is None:
        return mcp_error("run_forecast not configured - call set_run_forecast_fn first")

    validated = validate_input(SpawnSubquestionsInput, args)
    if isinstance(validated, dict):
        return validated

    subquestions = validated.subquestions

    async def run_subforecast(sq: SubQuestionInput) -> dict[str, Any]:
        """Execute a single sub-forecast."""
        question_type = sq.type

        # Build context for the sub-question
        context: dict[str, Any] = {
            "title": sq.question,
            "type": question_type,
            "description": sq.context,
            "resolution_criteria": "",
            "fine_print": "",
        }

        # Add type-specific context
        if question_type == "multiple_choice" and sq.options:
            context["options"] = sq.options
        elif question_type in ("numeric", "discrete") and sq.numeric_bounds:
            context["numeric_bounds"] = sq.numeric_bounds

        try:
            result = await _run_forecast_fn(
                question_context=context,
                allow_spawn=False,  # Prevent infinite recursion
            )

            # Build response based on question type
            response: dict[str, Any] = {
                "question": sq.question,
                "type": question_type,
                "summary": result.summary,
                "weight": sq.weight,
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
            logger.exception("Sub-forecast failed: %s", sq.question)
            return {
                "question": sq.question,
                "type": question_type,
                "summary": None,
                "weight": sq.weight,
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

composition_server = create_mcp_server(
    name="composition",
    version="2.0.0",
    tools=[
        spawn_subquestions,
    ],
)
