"""Tests for aib.tools.metrics."""

import pytest

from aib.tools.metrics import MetricsCollector, ToolMetrics, get_collector, tracked


class TestToolMetrics:
    """Tests for the ToolMetrics dataclass."""

    def test_initial_values(self) -> None:
        """Metrics start at zero/infinity."""
        metrics = ToolMetrics()
        assert metrics.call_count == 0
        assert metrics.error_count == 0
        assert metrics.total_duration_ms == 0.0
        assert metrics.min_duration_ms == float("inf")
        assert metrics.max_duration_ms == 0.0

    def test_avg_duration_zero_calls(self) -> None:
        """Average duration is 0 when no calls recorded."""
        metrics = ToolMetrics()
        assert metrics.avg_duration_ms == 0.0

    def test_error_rate_zero_calls(self) -> None:
        """Error rate is 0 when no calls recorded."""
        metrics = ToolMetrics()
        assert metrics.error_rate == 0.0

    def test_record_single_call(self) -> None:
        """Single call updates metrics correctly."""
        metrics = ToolMetrics()
        metrics.record_call(100.0, is_error=False)

        assert metrics.call_count == 1
        assert metrics.error_count == 0
        assert metrics.total_duration_ms == 100.0
        assert metrics.min_duration_ms == 100.0
        assert metrics.max_duration_ms == 100.0
        assert metrics.avg_duration_ms == 100.0
        assert metrics.error_rate == 0.0

    def test_record_multiple_calls(self) -> None:
        """Multiple calls accumulate correctly."""
        metrics = ToolMetrics()
        metrics.record_call(50.0, is_error=False)
        metrics.record_call(150.0, is_error=False)
        metrics.record_call(100.0, is_error=False)

        assert metrics.call_count == 3
        assert metrics.total_duration_ms == 300.0
        assert metrics.min_duration_ms == 50.0
        assert metrics.max_duration_ms == 150.0
        assert metrics.avg_duration_ms == 100.0

    def test_record_error_call(self) -> None:
        """Error calls increment error count."""
        metrics = ToolMetrics()
        metrics.record_call(100.0, is_error=True)

        assert metrics.call_count == 1
        assert metrics.error_count == 1
        assert metrics.error_rate == 1.0

    def test_error_rate_calculation(self) -> None:
        """Error rate is correctly calculated."""
        metrics = ToolMetrics()
        metrics.record_call(100.0, is_error=False)
        metrics.record_call(100.0, is_error=True)
        metrics.record_call(100.0, is_error=False)
        metrics.record_call(100.0, is_error=True)

        assert metrics.error_rate == 0.5

    def test_to_dict_format(self) -> None:
        """to_dict returns expected format."""
        metrics = ToolMetrics()
        metrics.record_call(100.0, is_error=False)
        metrics.record_call(200.0, is_error=True)

        result = metrics.to_dict()

        assert result["call_count"] == 2
        assert result["error_count"] == 1
        assert result["error_rate"] == "50.0%"
        assert result["total_duration_ms"] == 300.0
        assert result["avg_duration_ms"] == 150.0
        assert result["min_duration_ms"] == 100.0
        assert result["max_duration_ms"] == 200.0

    def test_to_dict_no_calls(self) -> None:
        """to_dict handles no calls gracefully."""
        metrics = ToolMetrics()
        result = metrics.to_dict()

        assert result["call_count"] == 0
        assert result["min_duration_ms"] == 0  # Converts inf to 0


class TestMetricsCollector:
    """Tests for the MetricsCollector."""

    def test_record_creates_tool_metrics(self) -> None:
        """Recording creates metrics for new tools."""
        collector = MetricsCollector()
        collector.record("search_tool", 100.0, is_error=False)

        metrics = collector.get_metrics("search_tool")
        assert metrics.call_count == 1

    def test_record_accumulates(self) -> None:
        """Recording accumulates across calls."""
        collector = MetricsCollector()
        collector.record("tool_a", 100.0)
        collector.record("tool_a", 200.0)

        metrics = collector.get_metrics("tool_a")
        assert metrics.call_count == 2
        assert metrics.total_duration_ms == 300.0

    def test_separate_tools_tracked_independently(self) -> None:
        """Different tools are tracked independently."""
        collector = MetricsCollector()
        collector.record("tool_a", 100.0)
        collector.record("tool_b", 200.0)
        collector.record("tool_a", 150.0)

        assert collector.get_metrics("tool_a").call_count == 2
        assert collector.get_metrics("tool_b").call_count == 1

    def test_get_all_metrics(self) -> None:
        """get_all_metrics returns all tool metrics."""
        collector = MetricsCollector()
        collector.record("tool_a", 100.0)
        collector.record("tool_b", 200.0)

        all_metrics = collector.get_all_metrics()

        assert "tool_a" in all_metrics
        assert "tool_b" in all_metrics
        assert all_metrics["tool_a"]["call_count"] == 1
        assert all_metrics["tool_b"]["call_count"] == 1

    def test_get_summary(self) -> None:
        """get_summary returns correct totals."""
        collector = MetricsCollector()
        collector.record("tool_a", 100.0, is_error=False)
        collector.record("tool_a", 100.0, is_error=True)
        collector.record("tool_b", 200.0, is_error=False)

        summary = collector.get_summary()

        assert summary["total_tool_calls"] == 3
        assert summary["total_errors"] == 1
        assert summary["overall_error_rate"] == "33.3%"
        assert summary["total_tool_time_ms"] == 400.0
        assert summary["tools_used"] == 2
        assert "by_tool" in summary

    def test_reset_clears_metrics(self) -> None:
        """reset clears all recorded metrics."""
        collector = MetricsCollector()
        collector.record("tool_a", 100.0)
        collector.record("tool_b", 200.0)

        collector.reset()

        assert collector.get_all_metrics() == {}

    def test_reset_resets_session_start(self) -> None:
        """reset also resets session start time."""
        collector = MetricsCollector()
        original_start = collector._session_start

        # Small delay to ensure time difference
        import time

        time.sleep(0.01)

        collector.reset()

        assert collector._session_start > original_start


class TestTrackedDecorator:
    """Tests for the @tracked decorator."""

    @pytest.fixture(autouse=True)
    def reset_collector(self) -> None:
        """Reset global collector before each test."""
        get_collector().reset()

    @pytest.mark.asyncio
    async def test_tracks_successful_call(self) -> None:
        """Decorator tracks successful async calls."""

        @tracked("test_func")
        async def test_func() -> str:
            return "success"

        result = await test_func()

        assert result == "success"
        metrics = get_collector().get_metrics("test_func")
        assert metrics.call_count == 1
        assert metrics.error_count == 0

    @pytest.mark.asyncio
    async def test_tracks_duration(self) -> None:
        """Decorator tracks call duration."""
        import asyncio

        @tracked("slow_func")
        async def slow_func() -> None:
            await asyncio.sleep(0.01)

        await slow_func()

        metrics = get_collector().get_metrics("slow_func")
        assert metrics.total_duration_ms >= 10  # At least 10ms

    @pytest.mark.asyncio
    async def test_tracks_exception_as_error(self) -> None:
        """Decorator tracks exceptions as errors."""

        @tracked("failing_func")
        async def failing_func() -> None:
            raise ValueError("Test error")

        with pytest.raises(ValueError):
            await failing_func()

        metrics = get_collector().get_metrics("failing_func")
        assert metrics.call_count == 1
        assert metrics.error_count == 1

    @pytest.mark.asyncio
    async def test_tracks_mcp_error_response(self) -> None:
        """Decorator tracks MCP error responses as errors."""

        @tracked("mcp_func")
        async def mcp_func() -> dict[str, object]:
            return {"content": [], "is_error": True}

        result = await mcp_func()

        assert result["is_error"] is True
        metrics = get_collector().get_metrics("mcp_func")
        assert metrics.call_count == 1
        assert metrics.error_count == 1

    @pytest.mark.asyncio
    async def test_uses_function_name_if_not_specified(self) -> None:
        """Decorator uses function name if tool_name not provided."""

        @tracked()
        async def auto_named() -> None:
            pass

        await auto_named()

        metrics = get_collector().get_metrics("auto_named")
        assert metrics.call_count == 1

    @pytest.mark.asyncio
    async def test_preserves_function_metadata(self) -> None:
        """Decorator preserves original function metadata."""

        @tracked("documented")
        async def documented() -> None:
            """This is the docstring."""
            pass

        assert documented.__doc__ == "This is the docstring."
        assert documented.__name__ == "documented"
