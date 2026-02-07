"""Tests for historical Wikipedia fetching in retrodict mode."""

import pytest


# These are integration tests that make real HTTP calls to Wikipedia
pytestmark = pytest.mark.integration


class TestWikipediaHistorical:
    """Tests for _fetch_wikipedia_historical_content."""

    @pytest.mark.asyncio
    async def test_fetch_historical_article(self) -> None:
        """Test fetching a Wikipedia article at a past date."""
        from aib.tools.wikipedia import fetch_wikipedia_historical

        result = await fetch_wikipedia_historical(
            "Python (programming language)", "2024-01-15"
        )

        assert result["title"] == "Python (programming language)"
        assert result["revision_id"] > 0
        assert result["revision_timestamp"].startswith("2024-01")
        assert result["cutoff_date"] == "2024-01-15"
        assert len(result["extract"]) > 1000
        # Should mention Python is a programming language
        assert "programming" in result["extract"].lower()

    @pytest.mark.asyncio
    async def test_fetch_article_not_found(self) -> None:
        """Test that nonexistent articles raise ValueError."""
        from aib.tools.wikipedia import fetch_wikipedia_historical

        with pytest.raises(ValueError, match="Article not found"):
            await fetch_wikipedia_historical(
                "Xyzzy Nonexistent Article 12345", "2024-01-15"
            )

    @pytest.mark.asyncio
    async def test_fetch_article_before_creation(self) -> None:
        """Test that articles before their creation raise ValueError."""
        from aib.tools.wikipedia import fetch_wikipedia_historical

        # Wikipedia didn't exist before 2001
        with pytest.raises(ValueError, match="No revision found before"):
            await fetch_wikipedia_historical(
                "Python (programming language)", "1990-01-01"
            )


class TestExtractIntro:
    """Tests for _extract_intro helper."""

    def test_extract_intro_short_text(self) -> None:
        """Short text should be returned as-is."""
        from aib.tools.wikipedia import extract_intro

        text = "This is a short paragraph."
        assert extract_intro(text) == text

    def test_extract_intro_with_sections(self) -> None:
        """Intro should stop at reasonable length."""
        from aib.tools.wikipedia import extract_intro

        text = "First paragraph with enough content to meet the threshold.\n\n" * 20
        intro = extract_intro(text)
        # Should have some content but not all 20 paragraphs
        assert len(intro) < len(text)
        assert len(intro) > 100
