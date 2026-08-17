"""Sub-agent cost accounting, folded into lup's tool metrics.

lup's collector measures how long each tool ran and how often it failed. It
does not measure money, and several of this project's tools run a sub-agent
underneath whose spend is worth attributing to the tool that caused it. That
accounting lives here and joins lup's summary at the point of reading, so a
caller still sees one metrics dict rather than two.

Timing and error metrics come from ``lup.telemetry.metrics`` directly —
``collector`` for the session's record, ``tracked`` for async helpers that are
not MCP tools. Tools defined with ``lup_tool`` are recorded by the decorator.
"""

from typing import NotRequired, TypedDict

from pydantic import BaseModel

from lup.telemetry.metrics import collector


class ToolMetricsWithCost(TypedDict):
    """One tool's timing and error metrics, plus what its sub-agent spent."""

    call_count: int
    error_count: int
    error_rate: str
    total_duration_ms: float
    avg_duration_ms: float
    min_duration_ms: float
    max_duration_ms: float
    total_cost_usd: NotRequired[float]


class MetricsSummaryWithCost(TypedDict):
    """lup's session summary widened by this project's sub-agent spend."""

    session_duration_seconds: float
    total_tool_calls: int
    total_errors: int
    overall_error_rate: str
    total_tool_time_ms: float
    tools_used: int
    by_tool: dict[str, ToolMetricsWithCost]
    subagent_cost_usd: float


class SubagentCosts(BaseModel):
    """USD spent by tools that run a sub-agent underneath.

    Keyed by the tool that caused the spend rather than by the sub-agent that
    incurred it, because the question this answers is which tool is expensive.
    """

    # lup: ignore[dict-str-payload] — keyed by tool name, an open runtime set
    by_tool: dict[str, float] = {}

    def record(self, tool_name: str, cost_usd: float) -> None:
        """Accumulate a sub-agent's cost against the tool that ran it."""
        # lup: ignore[dict-get] — an open counter, absent until first spend
        self.by_tool[tool_name] = self.by_tool.get(tool_name, 0.0) + cost_usd

    def total(self) -> float:
        """Everything spent on sub-agents since the last reset."""
        return sum(self.by_tool.values())

    def reset(self) -> None:
        """Forget every recorded cost."""
        self.by_tool.clear()


costs = SubagentCosts()


def uncalled_tool_metrics() -> ToolMetricsWithCost:
    """A zeroed row, for a tool that recorded spend but no call of its own."""
    return ToolMetricsWithCost(
        call_count=0,
        error_count=0,
        error_rate="0.0%",
        total_duration_ms=0.0,
        avg_duration_ms=0.0,
        min_duration_ms=0.0,
        max_duration_ms=0.0,
    )


def get_metrics_summary() -> MetricsSummaryWithCost:
    """lup's tool summary with this project's sub-agent costs folded in.

    The two halves are joined here rather than at each reader, so the shape
    stays what ``ToolCallMetrics`` and the session report already describe:
    ``subagent_cost_usd`` on the summary, ``total_cost_usd`` per tool.
    """
    summary = collector.get_summary()
    by_tool: dict[str, ToolMetricsWithCost] = {
        name: ToolMetricsWithCost(**data) for name, data in summary["by_tool"].items()
    }
    for name, cost in costs.by_tool.items():
        if name not in by_tool:
            by_tool[name] = uncalled_tool_metrics()
        by_tool[name]["total_cost_usd"] = round(cost, 4)
    return MetricsSummaryWithCost(
        session_duration_seconds=summary["session_duration_seconds"],
        total_tool_calls=summary["total_tool_calls"],
        total_errors=summary["total_errors"],
        overall_error_rate=summary["overall_error_rate"],
        total_tool_time_ms=summary["total_tool_time_ms"],
        tools_used=summary["tools_used"],
        by_tool=by_tool,
        subagent_cost_usd=round(costs.total(), 4),
    )


def reset_metrics() -> None:
    """Reset both halves of the session's metrics."""
    collector.reset()
    costs.reset()


def log_metrics_summary() -> None:
    """Log the session's tool metrics."""
    collector.log_summary()
