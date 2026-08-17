"""Tests for fetch domain routing.

The mechanism is lup's (`lup.tool_routes`); what this project owns is the
table. `SUGGEST_ONLY` is the declaration a reader checks, and registering it
into lup's registry is what makes it answer — so both are tested: the
declaration for its content, the registry for what actually resolves.
"""

from lup.tool_routes import routes

from aib.tools.fetch_routes import SUGGEST_ONLY


def arguments_for(url: str) -> object:
    """The arguments the first matching route would call its tool with."""
    for entry in routes.routes:
        found = entry.arguments(url)
        if found is not None:
            return found
    return None


class TestSuggestOnly:
    """Tests for SUGGEST_ONLY blocked domain list."""

    def test_kalshi_and_metaculus_promoted_to_routes(self) -> None:
        assert "kalshi.com" not in SUGGEST_ONLY
        assert "metaculus.com" not in SUGGEST_ONLY

    def test_contains_new_blocked_domains(self) -> None:
        assert "tradingeconomics.com" in SUGGEST_ONLY
        assert "bls.gov" in SUGGEST_ONLY
        assert "macrotrends.net" in SUGGEST_ONLY
        assert "barchart.com" in SUGGEST_ONLY
        assert "statista.com" in SUGGEST_ONLY
        assert "manifold.markets" in SUGGEST_ONLY
        assert "data.worldbank.org" in SUGGEST_ONLY
        assert "scholar.google.com" in SUGGEST_ONLY

    def test_hints_are_nonempty(self) -> None:
        for domain, hint in SUGGEST_ONLY.items():
            assert hint, f"Empty hint for {domain}"

    def test_advice_matches_on_the_host(self) -> None:
        """A lookalike registration ending in a routed domain must not match.

        The hand-rolled loop this replaced matched by substring, so a
        registration for `bls.gov` also answered for `bls.gov.evil.example`.
        """
        assert routes.advice("https://bls.gov/data") is not None
        assert routes.advice("https://www.bls.gov/data") is not None
        assert routes.advice("https://bls.gov.evil.example/data") is None

    def test_advice_does_not_match_a_domain_in_the_path(self) -> None:
        assert routes.advice("https://example.com/?q=statista.com") is None


class TestRouteRegistry:
    """Tests for self-registered domain routes."""

    def test_registry_has_routes(self) -> None:
        # Routes register at import time — importing tool modules populates them
        from aib.tools import financial, markets, search, arxiv_search  # noqa: F401

        assert len(routes.routes) >= 5, f"Expected >=5 routes, got {len(routes.routes)}"

    def test_yahoo_finance_route_registered(self) -> None:
        from aib.tools import financial  # noqa: F401

        assert arguments_for("https://finance.yahoo.com/quote/AAPL") == {
            "symbol": "AAPL"
        }

    def test_yahoo_finance_handles_complex_tickers(self) -> None:
        from aib.tools import financial  # noqa: F401

        assert arguments_for("https://finance.yahoo.com/quote/^GSPC") == {
            "symbol": "^GSPC"
        }

    def test_fred_route_registered(self) -> None:
        from aib.tools import financial  # noqa: F401

        assert arguments_for("https://fred.stlouisfed.org/series/UNRATE") == {
            "series_id": "UNRATE"
        }

    def test_arxiv_route_registered(self) -> None:
        from aib.tools import arxiv_search  # noqa: F401

        assert arguments_for("https://arxiv.org/abs/2401.12345") == {
            "paper_id": "2401.12345"
        }

    def test_polymarket_route_registered(self) -> None:
        from aib.tools import markets  # noqa: F401

        assert arguments_for("https://polymarket.com/event/will-trump-win") == {
            "query": "will trump win"
        }

    def test_kalshi_route_registered(self) -> None:
        from aib.tools import markets  # noqa: F401

        url = "https://kalshi.com/markets/kxwofskate/winter-olympics-figure-skating"
        assert arguments_for(url) == {"query": "winter olympics figure skating"}

    def test_metaculus_route_registered(self) -> None:
        from aib.tools import markets  # noqa: F401

        url = "https://www.metaculus.com/questions/41560/uk-retail-sales-jan-2026/"
        assert arguments_for(url) == {"post_id_list": [41560]}

    def test_no_match_for_unknown_domain(self) -> None:
        assert arguments_for("https://example.com/some-page") is None
