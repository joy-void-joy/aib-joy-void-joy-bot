"""Tests for fetch domain routing."""

from aib.tools.fetch_routes import SUGGEST_ONLY, _registry


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


class TestRouteRegistry:
    """Tests for self-registered domain routes."""

    def test_registry_has_routes(self) -> None:
        # Routes register at import time — importing tool modules populates _registry
        from aib.tools import financial, markets, search, arxiv_search  # noqa: F401

        assert len(_registry) >= 7, f"Expected >=7 routes, got {len(_registry)}"

    def test_yahoo_finance_route_registered(self) -> None:
        from aib.tools import financial  # noqa: F401

        matched = [
            r
            for r in _registry
            if r.pattern.search("https://finance.yahoo.com/quote/AAPL")
        ]
        assert matched, "No route matches Yahoo Finance URLs"
        match = matched[0].pattern.search("https://finance.yahoo.com/quote/AAPL")
        assert match is not None
        assert match.group(1) == "AAPL"

    def test_yahoo_finance_handles_complex_tickers(self) -> None:
        from aib.tools import financial  # noqa: F401

        matched = [
            r
            for r in _registry
            if r.pattern.search("https://finance.yahoo.com/quote/^GSPC")
        ]
        assert matched
        match = matched[0].pattern.search("https://finance.yahoo.com/quote/^GSPC")
        assert match is not None
        assert match.group(1) == "^GSPC"

    def test_arxiv_route_registered(self) -> None:
        from aib.tools import arxiv_search  # noqa: F401

        matched = [
            r for r in _registry if r.pattern.search("https://arxiv.org/abs/2401.12345")
        ]
        assert matched

    def test_polymarket_route_registered(self) -> None:
        from aib.tools import markets  # noqa: F401

        matched = [
            r
            for r in _registry
            if r.pattern.search("https://polymarket.com/event/will-trump-win")
        ]
        assert matched
        match = matched[0].pattern.search("https://polymarket.com/event/will-trump-win")
        assert match is not None
        params = matched[0].param_builder(match)
        assert params == {"query": "will trump win"}

    def test_kalshi_route_registered(self) -> None:
        from aib.tools import markets  # noqa: F401

        url = "https://kalshi.com/markets/kxwofskate/winter-olympics-figure-skating"
        matched = [r for r in _registry if r.pattern.search(url)]
        assert matched
        match = matched[0].pattern.search(url)
        assert match is not None
        params = matched[0].param_builder(match)
        assert params == {"query": "winter olympics figure skating"}

    def test_metaculus_route_registered(self) -> None:
        from aib.tools import markets  # noqa: F401

        url = "https://www.metaculus.com/questions/41560/uk-retail-sales-jan-2026/"
        matched = [r for r in _registry if r.pattern.search(url)]
        assert matched
        match = matched[0].pattern.search(url)
        assert match is not None
        params = matched[0].param_builder(match)
        assert params == {"post_id_list": [41560]}

    def test_no_match_for_unknown_domain(self) -> None:
        url = "https://example.com/some-page"
        for route in _registry:
            assert route.pattern.search(url) is None
