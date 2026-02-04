"""Tests for WebFetch content quality classifiers."""

import pytest

from aib.tools.classifiers import (
    JS_FRAMEWORK_MARKERS,
    WebFetchQuality,
    _suggest_alternatives_for_url,
    classify_heuristic,
    generate_fallback_message,
)


class TestClassifyHeuristic:
    """Tests for the fast heuristic classifier."""

    def test_real_html_not_js_rendered(self, sample_html_content: str) -> None:
        """Real HTML content should not be flagged as JS-rendered."""
        result = classify_heuristic(sample_html_content)
        assert result.is_js_rendered is False
        assert result.confidence >= 0.8

    def test_js_framework_markers_detected(self, js_rendered_content: str) -> None:
        """Content with JS framework markers should be flagged."""
        result = classify_heuristic(js_rendered_content)
        assert result.is_js_rendered is True
        assert "framework_marker" in result.reason

    def test_loading_patterns_detected(self, loading_content: str) -> None:
        """Loading spinner content should be flagged."""
        result = classify_heuristic(loading_content)
        assert result.is_js_rendered is True
        assert "loading_pattern" in result.reason or "noscript" in result.reason.lower()

    def test_very_short_content(self, short_content: str) -> None:
        """Very short content should be flagged with high confidence."""
        result = classify_heuristic(short_content)
        assert result.is_js_rendered is True
        assert "very_short_content" in result.reason

    def test_json_response_detected(self) -> None:
        """JSON responses should be flagged."""
        json_content = '{"error": "unauthorized", "code": 401}'
        result = classify_heuristic(json_content)
        assert result.is_js_rendered is True
        assert "json_response" in result.reason

    def test_json_array_detected(self) -> None:
        """JSON array responses should be flagged."""
        json_array = '[{"id": 1}, {"id": 2}]'
        result = classify_heuristic(json_array)
        assert result.is_js_rendered is True
        assert "json_array_response" in result.reason

    def test_high_special_char_ratio(self) -> None:
        """Minified JS-like content should be flagged."""
        minified = "{{{{{}}}}}" * 100 + "a" * 50  # High brace ratio
        result = classify_heuristic(minified)
        assert result.is_js_rendered is True
        assert "high_special_char_ratio" in result.reason

    def test_minimal_text_content(self) -> None:
        """Lots of tags but little text should be flagged."""
        tag_heavy = "<div><div><div><span></span></div></div></div>" * 50
        result = classify_heuristic(tag_heavy)
        assert result.is_js_rendered is True
        assert "minimal_text_content" in result.reason

    def test_framework_markers_case_insensitive(self) -> None:
        """Framework markers should be detected case-insensitively."""
        content = "<script>WEBPACK_MODULE</script>" + "x" * 500
        result = classify_heuristic(content)
        assert result.is_js_rendered is True
        assert "framework_marker" in result.reason

    def test_all_framework_markers(self) -> None:
        """All defined framework markers should be detected."""
        for marker in JS_FRAMEWORK_MARKERS:
            content = f"<div>{marker}</div>" + "x" * 500
            result = classify_heuristic(content)
            assert result.is_js_rendered is True, f"Marker '{marker}' not detected"

    def test_confidence_levels(self) -> None:
        """Confidence should scale with indicator severity."""
        # Very short content = high confidence
        result_short = classify_heuristic("x")
        assert result_short.confidence >= 0.7

        # Single medium indicator = lower confidence
        result_medium = classify_heuristic("Loading..." + "x" * 300)
        # Should have loading_pattern but not be as confident
        assert result_medium.confidence < result_short.confidence


class TestSuggestAlternatives:
    """Tests for URL-based alternative suggestions."""

    def test_stock_data_urls(self) -> None:
        """Stock/financial URLs should suggest stock tools."""
        for url in [
            "https://finance.yahoo.com/quote/AAPL",
            "https://tradingview.com/chart",
            "https://marketwatch.com/stocks",
            "https://bloomberg.com/markets",
        ]:
            alternatives = _suggest_alternatives_for_url(url)
            assert any("stock" in alt.lower() for alt in alternatives)

    def test_news_urls(self) -> None:
        """News URLs should suggest news search tools."""
        for url in [
            "https://reuters.com/article",
            "https://bbc.com/news",
            "https://cnn.com/politics",
            "https://nytimes.com/article",
            "https://wsj.com/articles",
        ]:
            alternatives = _suggest_alternatives_for_url(url)
            assert any("search_news" in alt for alt in alternatives)

    def test_wikipedia_urls(self) -> None:
        """Wikipedia URLs should suggest wikipedia tool."""
        url = "https://en.wikipedia.org/wiki/Test"
        alternatives = _suggest_alternatives_for_url(url)
        assert any("wikipedia" in alt.lower() for alt in alternatives)

    def test_social_media_urls(self) -> None:
        """Social media URLs should suggest news coverage and Playwright."""
        for url in [
            "https://twitter.com/user",
            "https://x.com/user",
            "https://reddit.com/r/test",
            "https://facebook.com/page",
        ]:
            alternatives = _suggest_alternatives_for_url(url)
            assert any("JavaScript rendering" in alt for alt in alternatives)
            assert any("Playwright" in alt for alt in alternatives)

    def test_polymarket_urls(self) -> None:
        """Polymarket URLs should suggest polymarket tool."""
        url = "https://polymarket.com/event/test"
        alternatives = _suggest_alternatives_for_url(url)
        assert any("polymarket_price" in alt for alt in alternatives)

    def test_manifold_urls(self) -> None:
        """Manifold URLs should suggest manifold tool."""
        url = "https://manifold.markets/question"
        alternatives = _suggest_alternatives_for_url(url)
        assert any("manifold_price" in alt for alt in alternatives)

    def test_generic_urls(self) -> None:
        """Unknown URLs should get generic suggestions."""
        url = "https://random-site.com/page"
        alternatives = _suggest_alternatives_for_url(url)
        assert any("search_exa" in alt for alt in alternatives)
        assert any("Playwright" in alt for alt in alternatives)


class TestGenerateFallbackMessage:
    """Tests for fallback message generation."""

    def test_includes_url(self) -> None:
        """Message should include the URL."""
        classification = WebFetchQuality(
            is_js_rendered=True,
            confidence=0.8,
            reason="test reason",
            suggested_alternatives=["alt1"],
        )
        message = generate_fallback_message("https://example.com", classification)
        assert "example.com" in message

    def test_truncates_long_urls(self) -> None:
        """Long URLs should be truncated."""
        long_url = "https://example.com/" + "x" * 100
        classification = WebFetchQuality(
            is_js_rendered=True,
            confidence=0.8,
            reason="test",
            suggested_alternatives=[],
        )
        message = generate_fallback_message(long_url, classification)
        assert "..." in message
        # URL is truncated to 60 chars, but the full message line includes the template
        assert len(message.split("\n")[0]) < 150  # First line should be reasonable

    def test_includes_confidence(self) -> None:
        """Message should include confidence percentage."""
        classification = WebFetchQuality(
            is_js_rendered=True,
            confidence=0.85,
            reason="test",
            suggested_alternatives=[],
        )
        message = generate_fallback_message("https://example.com", classification)
        assert "85%" in message

    def test_includes_alternatives(self) -> None:
        """Message should list all alternatives."""
        classification = WebFetchQuality(
            is_js_rendered=True,
            confidence=0.8,
            reason="test",
            suggested_alternatives=["Use tool A", "Try tool B"],
        )
        message = generate_fallback_message("https://example.com", classification)
        assert "Use tool A" in message
        assert "Try tool B" in message

    def test_empty_alternatives(self) -> None:
        """Message should have fallback text when no alternatives."""
        classification = WebFetchQuality(
            is_js_rendered=True,
            confidence=0.8,
            reason="test",
            suggested_alternatives=[],
        )
        message = generate_fallback_message("https://example.com", classification)
        assert "different approach" in message
