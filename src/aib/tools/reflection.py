"""Reflection tool for forecasting sessions.

Replaces write_meta with a structured, iterative checkpoint tool.
Takes the agent's current factors and tentative logit, computes the
factor-implied probability, and returns the gap. Each call appends a
timestamped entry to reflection.yaml in the session directory.
"""

import logging
import math
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import aiofiles
from pydantic import BaseModel, Field

from claude_agent_sdk import tool

from aib.agent.models import Factor
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)

NEUTRAL_THRESHOLD = 0.1


# --- Input Model ---


class ReflectionInput(BaseModel):
    """Structured input for the reflection tool."""

    factors: list[Factor] = Field(
        description=(
            "Key evidence items with logit values and confidence. "
            "Same format as your final forecast factors."
        )
    )
    tentative_logit: float = Field(
        description="Your current synthesized log-odds estimate."
    )
    arguments_for: list[str] = Field(
        description="Distinct arguments supporting YES / higher values."
    )
    arguments_against: list[str] = Field(
        description="Distinct arguments supporting NO / lower values."
    )
    calibration_notes: str | None = Field(
        default=None,
        description="Base rates, status quo assessment, hedging check.",
    )
    key_uncertainties: str | None = Field(
        default=None,
        description="What you're most uncertain about and what would change your mind.",
    )
    tool_audit: str = Field(
        description=(
            "Which tools provided useful information, which returned "
            "empty results, and which had actual failures."
        ),
    )
    update_triggers: str | None = Field(
        default=None,
        description="Events that would move your forecast significantly.",
    )
    process_reflection: str = Field(
        description=(
            "Reflection on the forecasting process itself: what felt "
            "rigid, what was lacking, what worked well, thoughts on "
            "the prompt or framework. What tools are missing that "
            "would have helped? What subagents would have been useful?"
        ),
    )


# --- Output Models ---


class FactorBreakdown(BaseModel):
    """Per-factor effective logit computation."""

    description: str
    logit: float
    confidence: float
    effective_logit: float


class ReflectionOutput(BaseModel):
    """Computed feedback from a reflection checkpoint."""

    factor_count: int
    factor_sum: float
    tentative_logit: float
    logit_gap: float
    neutral_factor_count: int
    factor_breakdown: list[FactorBreakdown]
    dominant_factor: str | None = None
    dominant_effective_logit: float | None = None

    # Binary-specific
    factor_implied_probability: float | None = None
    tentative_probability: float | None = None
    gap_pp: float | None = None

    # Non-binary
    factor_direction: str | None = None
    factor_strength: float | None = None


# --- Computation ---


def compute_reflection(
    inp: ReflectionInput,
    question_type: str,
) -> ReflectionOutput:
    """Compute factor analysis and return structured feedback."""
    breakdown: list[FactorBreakdown] = []
    for f in inp.factors:
        breakdown.append(
            FactorBreakdown(
                description=f.description,
                logit=f.logit,
                confidence=f.confidence,
                effective_logit=f.logit * f.confidence,
            )
        )

    factor_sum = sum(fb.effective_logit for fb in breakdown)
    neutral_count = sum(1 for f in inp.factors if abs(f.logit) < NEUTRAL_THRESHOLD)
    dominant = max(breakdown, key=lambda fb: abs(fb.effective_logit), default=None)

    output = ReflectionOutput(
        factor_count=len(inp.factors),
        factor_sum=factor_sum,
        tentative_logit=inp.tentative_logit,
        logit_gap=inp.tentative_logit - factor_sum,
        neutral_factor_count=neutral_count,
        factor_breakdown=breakdown,
        dominant_factor=dominant.description if dominant else None,
        dominant_effective_logit=dominant.effective_logit if dominant else None,
    )

    if question_type == "binary":
        output.factor_implied_probability = 1 / (1 + math.exp(-factor_sum))
        output.tentative_probability = 1 / (1 + math.exp(-inp.tentative_logit))
        output.gap_pp = (output.tentative_probability - output.factor_implied_probability) * 100
    else:
        output.factor_direction = (
            "positive" if factor_sum > 0 else "negative" if factor_sum < 0 else "neutral"
        )
        output.factor_strength = abs(factor_sum)

    return output


# --- File Writing ---


async def _append_reflection(
    session_dir: Path,
    inp: ReflectionInput,
    computed: ReflectionOutput,
    question_type: str,
) -> Path:
    """Append a timestamped reflection entry to reflection.yaml."""
    import yaml

    filepath = session_dir / "reflection.yaml"
    session_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    entry = (
        {"timestamp": timestamp, "question_type": question_type}
        | inp.model_dump(exclude_none=True)
        | {"computed": computed.model_dump(exclude_none=True)}
    )

    content = "---\n" + yaml.dump(
        entry, default_flow_style=False, sort_keys=False, allow_unicode=True
    )

    async with aiofiles.open(filepath, "a", encoding="utf-8") as f:
        await f.write(content)

    return filepath


# --- Tool ---

_REFLECTION_DESCRIPTION = """\
Checkpoint your reasoning by providing your current factors and tentative logit.

Returns computed analysis: factor-implied probability (for binary), gap between
your tentative estimate and what your factors imply, and per-factor breakdown.

Call this at least once before your final StructuredOutput. You can call it
multiple times as your analysis evolves.

Example:
  reflection(
    factors=[
      {"description": "Strong trend in data", "logit": 1.5, "confidence": 0.8},
      {"description": "Status quo persistence", "logit": -0.5, "confidence": 0.7}
    ],
    tentative_logit=0.8,
    arguments_for=["Data shows consistent upward trend across 3 sources"],
    arguments_against=["Historical base rate for this type of change is only 30%"]
  )
"""


def _create_reflection_tool(
    session_dir: Path | None,
    question_type: str,
):
    """Create the reflection tool with session context."""

    @tool("reflection", _REFLECTION_DESCRIPTION, ReflectionInput)
    @tracked("reflection")
    async def reflection_tool(args: dict[str, Any]) -> dict[str, Any]:
        """Compute and log a reflection checkpoint."""
        try:
            validated = ReflectionInput.model_validate(args)
        except Exception as e:
            return mcp_error(f"Invalid input: {e}")

        if session_dir is None:
            return mcp_error("reflection is not available in this context")

        computed = compute_reflection(validated, question_type)

        try:
            filepath = await _append_reflection(
                session_dir, validated, computed, question_type
            )
            logger.info("Appended reflection entry to %s", filepath)
        except Exception as e:
            logger.exception("Failed to write reflection")
            return mcp_error(f"Failed to write reflection: {e}")

        return mcp_success(computed.model_dump(exclude_none=True))

    return reflection_tool


def create_reflection_server(
    session_dir: Path | None = None,
    question_type: str = "binary",
):
    """Create the reflection MCP server with session context.

    Args:
        session_dir: Session directory for reflection storage.
            If None, reflection is disabled.
        question_type: The question type for this forecast session.

    Returns:
        MCP server configured with the reflection tool.
    """
    return create_mcp_server(
        name="notes",
        version="4.0.0",
        tools=[_create_reflection_tool(session_dir, question_type)],
    )
