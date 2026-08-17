"""Which of this project's tools answers a URL better than fetching it.

The mechanism is lup's (:mod:`lup.tool_routes`) — matching, dispatch, and the
host comparison that decides which redirection speaks for a URL. What lives
here is only this project's own table.

URL routes register beside the tool they reach, so this module carries just
the *redirections*: domains with a better tool whose arguments are simply not
in the URL. ``SUGGEST_ONLY`` is the declaration a reader (and the test suite)
checks; registering it into lup's registry is what makes it answer.
"""

from lup.tool_routes import routes

# Domains with dedicated tools but no simple URL → args mapping
# lup: ignore[dict-str-payload] — domain → the redirection to show the agent
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

for domain, redirection in SUGGEST_ONLY.items():
    routes.redirect(domain, redirection)
