"""Composition tools for sub-question forecasting.

Enables the main forecasting agent to decompose questions and
forecast sub-questions recursively via spawn_subquestions.
"""

import asyncio
import logging

from pydantic import BaseModel, Field

from aib.agent.models import ForecastOutput
from aib.agent.session import get_session
from aib.tools.decorator import ToolError, mcp_tool

logger = logging.getLogger(__name__)


# --- Input Schemas ---


class NumericBounds(BaseModel):
    """Bounds for numeric/discrete sub-questions."""

    range_min: float | None = None
    range_max: float | None = None
    open_lower_bound: bool = False
    open_upper_bound: bool = False
    zero_point: float | None = None


class SubquestionSpec(BaseModel):
    """Specification for a single sub-question to forecast."""

    question: str
    context: str = ""
    weight: float = 1.0
    question_type: str = "binary"
    options: list[str] = Field(default_factory=list)
    numeric_bounds: NumericBounds = Field(default_factory=NumericBounds)


class SpawnSubquestionsInput(BaseModel):
    """Input for spawn_subquestions tool."""

    agents: list[SubquestionSpec] = Field(min_length=1)


# --- Output ---


class SubquestionOutput(BaseModel):
    """Result from a sub-question forecast."""

    question: str = ""
    weight: float = 1.0
    forecast: ForecastOutput | None = None
    error: str | None = None


class SpawnSubquestionsOutput(BaseModel):
    """Output from spawn_subquestions tool."""

    results: list[dict[str, object]]
    successful_count: int
    failed_count: int


# --- Runner ---


async def _run_subforecast(spec: SubquestionSpec) -> SubquestionOutput:
    """Run a recursive sub-forecast via run_forecast()."""
    session = get_session()
    if session.run_forecast_fn is None:
        return SubquestionOutput(
            question=spec.question,
            error="run_forecast not configured on session",
        )

    question_type = spec.question_type
    context: dict[str, object] = {
        "title": spec.question,
        "type": question_type,
        "description": spec.context,
        "resolution_criteria": "",
        "fine_print": "",
    }

    if question_type == "multiple_choice" and spec.options:
        context["options"] = spec.options
    elif question_type in ("numeric", "discrete"):
        bounds = spec.numeric_bounds
        if bounds.range_min is not None or bounds.range_max is not None:
            context["numeric_bounds"] = bounds.model_dump(exclude_none=True)

    try:
        result = await session.run_forecast_fn(
            question_context=context,
            allow_spawn=False,
        )

        return SubquestionOutput(
            question=spec.question,
            weight=spec.weight,
            forecast=result,
        )

    except Exception as e:
        logger.exception("Sub-forecast failed: %s", spec.question)
        return SubquestionOutput(
            question=spec.question,
            weight=spec.weight,
            error=str(e),
        )


# --- Tool ---


@mcp_tool(
    "spawn_subquestions",
    "Decompose a question into independent sub-forecasts. Each sub-question "
    "gets its own full forecasting agent (research, computation, calibration). "
    "Pass multiple sub-questions to forecast them concurrently. You receive "
    "all individual results — synthesize them yourself.\n\n"
    "Use when a question naturally breaks into independent parts:\n"
    "- Revenue segments: forecast each independently, then sum\n"
    "- Conditional chains: P(A and B) = P(A) * P(B|A)\n"
    "- Multi-component questions: each part needs its own research\n\n"
    "Example (conditional chain):\n"
    "  spawn_subquestions(agents=[\n"
    '    {"question": "Will Country X apply to join Org Y by mid-2026?", '
    '"context": "Requires parliamentary vote.", "question_type": "binary"},\n'
    '    {"question": "If applied, will all members approve?", '
    '"context": "Requires unanimous approval.", "question_type": "binary"}\n'
    "  ])\n"
    "  Then multiply: P(join) = P(apply) * P(approve|apply).\n\n"
    "Example (revenue segments):\n"
    "  spawn_subquestions(agents=[\n"
    '    {"question": "What will Search revenue be in Q1?", '
    '"context": "Q1 2025 was $50.7B.", "question_type": "numeric"},\n'
    '    {"question": "What will Cloud revenue be in Q1?", '
    '"context": "Q1 2025 was $12.3B.", "question_type": "numeric"}\n'
    "  ])\n"
    "  Then sum the sub-forecast medians and propagate uncertainty.\n",
)
async def spawn_subquestions(args: SpawnSubquestionsInput) -> SpawnSubquestionsOutput:
    """Spawn parallel sub-question forecasts for structural decomposition."""
    results = await asyncio.gather(*[_run_subforecast(s) for s in args.agents])

    errors = [r for r in results if r.error is not None]
    successful = [r for r in results if r.error is None]

    if not successful:
        error_msgs = [r.error for r in errors]
        raise ToolError(f"All sub-forecasts failed: {error_msgs}")

    return SpawnSubquestionsOutput(
        results=[r.model_dump(exclude_none=True) for r in results],
        successful_count=len(successful),
        failed_count=len(errors),
    )
