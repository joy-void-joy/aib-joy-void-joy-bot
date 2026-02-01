"""Simple metrics tracking for tool calls.

Provides a decorator that tracks tool call counts, durations, and errors.
Metrics can be logged or retrieved at the end of a forecasting session.
"""

import logging
import time
from collections import defaultdict
from collections.abc import Callable, Coroutine
from dataclasses import dataclass, field
from functools import wraps
from typing import Any, ParamSpec, TypeVar, cast

logger = logging.getLogger(__name__)

P = ParamSpec("P")
T = TypeVar("T")


@dataclass
class ToolMetrics:
    """Metrics for a single tool."""

    call_count: int = 0
    error_count: int = 0
    total_duration_ms: float = 0.0
    min_duration_ms: float = float("inf")
    max_duration_ms: float = 0.0

    @property
    def avg_duration_ms(self) -> float:
        """Average duration per call in milliseconds."""
        if self.call_count == 0:
            return 0.0
        return self.total_duration_ms / self.call_count

    @property
    def error_rate(self) -> float:
        """Percentage of calls that resulted in errors."""
        if self.call_count == 0:
            return 0.0
        return self.error_count / self.call_count

    def record_call(self, duration_ms: float, is_error: bool = False) -> None:
        """Record a tool call.

        Args:
            duration_ms: Duration of the call in milliseconds.
            is_error: Whether the call resulted in an error.
        """
        self.call_count += 1
        self.total_duration_ms += duration_ms
        self.min_duration_ms = min(self.min_duration_ms, duration_ms)
        self.max_duration_ms = max(self.max_duration_ms, duration_ms)
        if is_error:
            self.error_count += 1

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for logging/serialization."""
        return {
            "call_count": self.call_count,
            "error_count": self.error_count,
            "error_rate": f"{self.error_rate:.1%}",
            "total_duration_ms": round(self.total_duration_ms, 2),
            "avg_duration_ms": round(self.avg_duration_ms, 2),
            "min_duration_ms": (
                round(self.min_duration_ms, 2)
                if self.min_duration_ms != float("inf")
                else 0
            ),
            "max_duration_ms": round(self.max_duration_ms, 2),
        }


@dataclass
class MetricsCollector:
    """Collects metrics for all tools."""

    _metrics: dict[str, ToolMetrics] = field(
        default_factory=lambda: defaultdict(ToolMetrics)
    )
    _session_start: float = field(default_factory=time.time)

    def record(
        self, tool_name: str, duration_ms: float, is_error: bool = False
    ) -> None:
        """Record a tool call.

        Args:
            tool_name: Name of the tool.
            duration_ms: Duration of the call in milliseconds.
            is_error: Whether the call resulted in an error.
        """
        self._metrics[tool_name].record_call(duration_ms, is_error)

    def get_metrics(self, tool_name: str) -> ToolMetrics:
        """Get metrics for a specific tool."""
        return self._metrics[tool_name]

    def get_all_metrics(self) -> dict[str, dict[str, Any]]:
        """Get all metrics as a dictionary."""
        return {name: metrics.to_dict() for name, metrics in self._metrics.items()}

    def get_summary(self) -> dict[str, Any]:
        """Get a summary of all metrics."""
        total_calls = sum(m.call_count for m in self._metrics.values())
        total_errors = sum(m.error_count for m in self._metrics.values())
        total_duration = sum(m.total_duration_ms for m in self._metrics.values())
        session_duration = time.time() - self._session_start

        return {
            "session_duration_seconds": round(session_duration, 2),
            "total_tool_calls": total_calls,
            "total_errors": total_errors,
            "overall_error_rate": f"{total_errors / max(1, total_calls):.1%}",
            "total_tool_time_ms": round(total_duration, 2),
            "tools_used": len(self._metrics),
            "by_tool": self.get_all_metrics(),
        }

    def log_summary(self, level: int = logging.INFO) -> None:
        """Log a summary of all metrics."""
        summary = self.get_summary()
        logger.log(
            level,
            "Tool Metrics Summary: %d calls, %d errors, %.1fs session",
            summary["total_tool_calls"],
            summary["total_errors"],
            summary["session_duration_seconds"],
        )
        for tool_name, metrics in summary["by_tool"].items():
            logger.log(
                level,
                "  %s: %d calls, %s errors, avg %.1fms",
                tool_name,
                metrics["call_count"],
                metrics["error_rate"],
                metrics["avg_duration_ms"],
            )

    def reset(self) -> None:
        """Reset all metrics."""
        self._metrics.clear()
        self._session_start = time.time()


# Global metrics collector
_collector = MetricsCollector()


def get_collector() -> MetricsCollector:
    """Get the global metrics collector."""
    return _collector


def tracked(
    tool_name: str | None = None,
) -> Callable[
    [Callable[P, Coroutine[Any, Any, T]]],
    Callable[P, Coroutine[Any, Any, T]],
]:
    """Decorator to track tool call metrics.

    Args:
        tool_name: Name to record metrics under. If None, uses function name.

    Returns:
        Decorator function.

    Example:
        @tracked("search_exa")
        async def search_exa(args: SearchExaInput) -> dict[str, Any]:
            ...
    """

    def decorator(
        func: Callable[P, Coroutine[Any, Any, T]],
    ) -> Callable[P, Coroutine[Any, Any, T]]:
        name = tool_name or func.__name__

        @wraps(func)
        async def wrapper(*args: P.args, **kwargs: P.kwargs) -> T:
            start = time.perf_counter()
            is_error = False

            try:
                result = await func(*args, **kwargs)
                # Check if result indicates an error (MCP response format)
                if isinstance(result, dict) and cast(dict[str, Any], result).get(
                    "is_error"
                ):
                    is_error = True
                return result
            except Exception:
                is_error = True
                raise
            finally:
                duration_ms = (time.perf_counter() - start) * 1000
                _collector.record(name, duration_ms, is_error)

        return wrapper

    return decorator


def log_metrics_summary() -> None:
    """Log a summary of all tool metrics."""
    _collector.log_summary()


def get_metrics_summary() -> dict[str, Any]:
    """Get a summary of all tool metrics."""
    return _collector.get_summary()


def reset_metrics() -> None:
    """Reset all tool metrics."""
    _collector.reset()
