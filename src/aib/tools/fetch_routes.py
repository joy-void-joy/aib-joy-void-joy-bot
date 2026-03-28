"""Domain routing for the fetch tool.

Routes self-register at import time when tools use @mcp_tool(url_route=...)
via mcp_tool(url_route=...) at tool definition time — no centralized
import list needed.
"""

import logging
import re
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

logger = logging.getLogger(__name__)

Handler = Callable[[dict[str, Any]], Awaitable[dict[str, Any]]]
ParamBuilder = Callable[[re.Match[str]], dict[str, Any]]


@dataclass
class DomainRoute:
    """Maps a URL regex to a tool function via a param builder."""

    pattern: re.Pattern[str]
    handler: Handler
    param_builder: ParamBuilder


# Domains with dedicated tools but no simple URL → args mapping
SUGGEST_ONLY: dict[str, str] = {
    "tradingeconomics.com": "Use fred_series/fred_search for US data, or world_bank_indicator for international data.",
    "bls.gov": "Use fred_series (FRED mirrors BLS data). Try UNRATE, CPIAUCSL, PAYEMS.",
    "macrotrends.net": "Use company_financials for earnings data, or fred_series for macro indicators.",
    "barchart.com": "Use stock_price or stock_history for market data.",
    "statista.com": "Use search_exa or search_news for statistics and reports.",
    "manifold.markets": "Use manifold_price for market data, or manifold_history for historical prices.",
    "data.worldbank.org": "Use world_bank_indicator for data, or world_bank_search to find indicator codes.",
    "scholar.google.com": "Use search_arxiv for academic paper search.",
    "congress.gov": "Use search_exa for cached content, or web_search for legislative information.",
    "echr.coe.int": "Use search_exa for cached content, or web_search for ECHR case information.",
    "missingmigrants.iom.int": "Use search_exa for cached content, or web_search for migration data.",
}

_registry: list[DomainRoute] = []


def register_route(pattern: str, handler: Handler, param_builder: ParamBuilder) -> None:
    """Register a domain route. Called by @mcp_tool when url_route is provided."""
    _registry.append(
        DomainRoute(
            pattern=re.compile(pattern),
            handler=handler,
            param_builder=param_builder,
        )
    )


async def domain_dispatch(url: str) -> dict[str, Any] | None:
    """Route URL to a specialized tool if possible. Returns None to fall through."""
    for route in _registry:
        match = route.pattern.search(url)
        if match:
            params = route.param_builder(match)
            logger.info(
                "Domain dispatch: %s → %s(%s)",
                url[:60],
                route.handler.__name__,
                params,
            )
            return await route.handler(params)
    return None
