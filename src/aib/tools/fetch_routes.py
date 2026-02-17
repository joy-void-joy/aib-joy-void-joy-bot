"""Domain routing for the fetch tool.

Maps URL patterns to specialized tool functions (stock_price, wikipedia, etc.).
When a URL matches, extracts parameters from the match and calls the tool directly.
"""

import logging
import re
from collections.abc import Awaitable, Callable
from dataclasses import dataclass
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class DomainRoute:
    """Maps a URL regex to a tool function via a param builder."""

    domain: str
    pattern: re.Pattern[str]
    handler: Callable[[dict[str, Any]], Awaitable[dict[str, Any]]]
    param_builder: Callable[[re.Match[str]], dict[str, Any]]


# Domains with dedicated tools but no simple URL → args mapping
SUGGEST_ONLY: dict[str, str] = {
    "kalshi.com": "Use kalshi_price, kalshi_event, or kalshi_history.",
    "metaculus.com": "Use the Metaculus API tools (get_prediction_history, etc.).",
    "tradingeconomics.com": "Use fred_series/fred_search for US data, or world_bank_indicator for international data.",
    "bls.gov": "Use fred_series (FRED mirrors BLS data). Try UNRATE, CPIAUCSL, PAYEMS.",
    "macrotrends.net": "Use company_financials for earnings data, or fred_series for macro indicators.",
    "barchart.com": "Use stock_price or stock_history for market data.",
    "statista.com": "Use search_exa or search_news for statistics and reports.",
}

_routes: list[DomainRoute] | None = None


def _build_routes() -> list[DomainRoute]:
    """Build domain routes. Lazy to avoid circular imports."""
    from aib.tools.arxiv_search import fetch_arxiv
    from aib.tools.financial import fred_series
    from aib.tools.forecasting import wikipedia
    from aib.tools.markets import polymarket_price, stock_price

    return [
        DomainRoute(
            domain="finance.yahoo.com",
            pattern=re.compile(r"finance\.yahoo\.com/quote/([A-Za-z0-9^._-]+)"),
            handler=stock_price.handler,
            param_builder=lambda m: {"symbol": m.group(1).upper()},
        ),
        DomainRoute(
            domain="arxiv.org",
            pattern=re.compile(r"arxiv\.org/(?:abs|pdf)/(\d+\.\d+)"),
            handler=fetch_arxiv.handler,
            param_builder=lambda m: {"paper_id": m.group(1)},
        ),
        DomainRoute(
            domain="wikipedia.org",
            pattern=re.compile(r"wikipedia\.org/wiki/([^#?]+)"),
            handler=wikipedia.handler,
            param_builder=lambda m: {
                "topic": m.group(1).replace("_", " "),
                "mode": "full",
            },
        ),
        DomainRoute(
            domain="fred.stlouisfed.org",
            pattern=re.compile(r"fred\.stlouisfed\.org/series/([A-Za-z0-9]+)"),
            handler=fred_series.handler,
            param_builder=lambda m: {"series_id": m.group(1).upper()},
        ),
        DomainRoute(
            domain="polymarket.com",
            pattern=re.compile(r"polymarket\.com/event/([^/?#]+)"),
            handler=polymarket_price.handler,
            param_builder=lambda m: {"query": m.group(1).replace("-", " ")},
        ),
    ]


def get_routes() -> list[DomainRoute]:
    global _routes
    if _routes is None:
        _routes = _build_routes()
    return _routes


async def domain_dispatch(url: str) -> dict[str, Any] | None:
    """Route URL to a specialized tool if possible. Returns None to fall through."""
    for route in get_routes():
        match = route.pattern.search(url)
        if match:
            params = route.param_builder(match)
            logger.info(
                "Domain dispatch: %s → %s(%s)",
                route.domain,
                route.handler.__name__,
                params,
            )
            return await route.handler(params)
    return None
