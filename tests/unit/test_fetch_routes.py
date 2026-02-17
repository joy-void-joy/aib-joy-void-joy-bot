"""Tests for fetch domain routing."""

import re

from aib.tools.fetch_routes import SUGGEST_ONLY, _build_routes


class TestSuggestOnly:
    """Tests for SUGGEST_ONLY blocked domain list."""

    def test_contains_original_entries(self) -> None:
        assert "kalshi.com" in SUGGEST_ONLY
        assert "metaculus.com" in SUGGEST_ONLY

    def test_contains_new_blocked_domains(self) -> None:
        assert "tradingeconomics.com" in SUGGEST_ONLY
        assert "bls.gov" in SUGGEST_ONLY
        assert "macrotrends.net" in SUGGEST_ONLY
        assert "barchart.com" in SUGGEST_ONLY
        assert "statista.com" in SUGGEST_ONLY

    def test_hints_are_nonempty(self) -> None:
        for domain, hint in SUGGEST_ONLY.items():
            assert hint, f"Empty hint for {domain}"


class TestRouteRegexes:
    """Tests for each route's regex and parameter extraction."""

    def _get_route(self, domain: str) -> re.Pattern[str]:
        routes = _build_routes()
        for route in routes:
            if route.domain == domain:
                return route.pattern
        raise AssertionError(f"No route for {domain}")

    def _get_param_builder(self, domain: str):  # noqa: ANN201
        routes = _build_routes()
        for route in routes:
            if route.domain == domain:
                return route.param_builder
        raise AssertionError(f"No route for {domain}")

    def test_yahoo_finance_captures_symbol(self) -> None:
        pattern = self._get_route("finance.yahoo.com")
        match = pattern.search("https://finance.yahoo.com/quote/AAPL")
        assert match is not None
        assert match.group(1) == "AAPL"

    def test_yahoo_finance_handles_complex_tickers(self) -> None:
        pattern = self._get_route("finance.yahoo.com")
        match = pattern.search("https://finance.yahoo.com/quote/^GSPC")
        assert match is not None
        assert match.group(1) == "^GSPC"

    def test_arxiv_captures_paper_id(self) -> None:
        pattern = self._get_route("arxiv.org")
        for url in [
            "https://arxiv.org/abs/2401.12345",
            "https://arxiv.org/pdf/2401.12345",
        ]:
            match = pattern.search(url)
            assert match is not None, f"No match for {url}"
            assert match.group(1) == "2401.12345"

    def test_wikipedia_captures_topic(self) -> None:
        pattern = self._get_route("wikipedia.org")
        match = pattern.search("https://en.wikipedia.org/wiki/Machine_learning")
        assert match is not None
        assert match.group(1) == "Machine_learning"

    def test_fred_captures_series_id(self) -> None:
        pattern = self._get_route("fred.stlouisfed.org")
        match = pattern.search("https://fred.stlouisfed.org/series/DGS10")
        assert match is not None
        assert match.group(1) == "DGS10"

    def test_polymarket_captures_slug(self) -> None:
        pattern = self._get_route("polymarket.com")
        match = pattern.search(
            "https://polymarket.com/event/will-trump-win-2024"
        )
        assert match is not None
        assert match.group(1) == "will-trump-win-2024"

    def test_polymarket_param_builder_converts_hyphens(self) -> None:
        pattern = self._get_route("polymarket.com")
        builder = self._get_param_builder("polymarket.com")
        match = pattern.search(
            "https://polymarket.com/event/will-trump-win-2024"
        )
        assert match is not None
        params = builder(match)
        assert params == {"query": "will trump win 2024"}

    def test_polymarket_stops_at_query_params(self) -> None:
        pattern = self._get_route("polymarket.com")
        match = pattern.search(
            "https://polymarket.com/event/my-event?tid=123"
        )
        assert match is not None
        assert match.group(1) == "my-event"

    def test_no_match_for_unknown_domain(self) -> None:
        routes = _build_routes()
        url = "https://example.com/some-page"
        for route in routes:
            assert route.pattern.search(url) is None
