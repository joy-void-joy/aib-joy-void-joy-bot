"""In-process MCP tools for the forecasting agent."""

from aib.tools.cache import cached, get_cache_stats
from aib.tools.composition import composition_server
from aib.tools.forecasting import forecasting_server
from aib.tools.markets import markets_server
from aib.tools.metrics import (
    get_metrics_summary,
    log_metrics_summary,
    reset_metrics,
    tracked,
)
from aib.tools.notes import notes_server
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.retry import with_retry

__all__ = [
    # MCP Servers
    "forecasting_server",
    "composition_server",
    "markets_server",
    "notes_server",
    # Decorators
    "with_retry",
    "cached",
    "tracked",
    # Response helpers
    "mcp_success",
    "mcp_error",
    # Metrics
    "get_metrics_summary",
    "log_metrics_summary",
    "reset_metrics",
    "get_cache_stats",
]
