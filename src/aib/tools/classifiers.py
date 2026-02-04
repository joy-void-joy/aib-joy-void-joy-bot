"""Content classifiers for tool quality detection.

Detects when WebFetch returns JS-rendered garbage and suggests alternatives.
Uses a two-tier approach: fast heuristics first, Haiku classifier for uncertain cases.
"""

import logging
import re

from pydantic import BaseModel, Field

logger = logging.getLogger(__name__)


class WebFetchQuality(BaseModel):
    """Classification result for WebFetch content quality."""

    is_js_rendered: bool = Field(
        description="Whether the content appears to be JS-rendered garbage"
    )
    confidence: float = Field(
        ge=0.0, le=1.0, description="Confidence in the classification (0-1)"
    )
    reason: str = Field(description="Explanation for the classification")
    suggested_alternatives: list[str] = Field(
        default_factory=list,
        description="Alternative tools or approaches to try",
    )


# Markers that indicate JS-heavy frameworks
JS_FRAMEWORK_MARKERS = frozenset(
    {
        "webpack",
        "__NEXT_DATA__",
        "window.__INITIAL",
        "_next/static",
        "react-root",
        "ng-app",
        "v-app",
        "nuxt",
        "__NUXT__",
        "gatsby",
        "__gatsby",
        "svelte",
        "ember",
        "backbone",
        "angular",
    }
)

# Patterns that indicate loading/placeholder content
LOADING_PATTERNS = [
    r"loading\.\.\.",
    r"please wait",
    r"javascript.*required",
    r"enable javascript",
    r"<noscript>",
    r"spinner",
    r"skeleton",
]


def classify_heuristic(content: str, url: str = "") -> WebFetchQuality:
    """Fast heuristic classification of WebFetch content quality.

    Checks for common indicators of JS-rendered pages without making API calls.
    Returns classification with confidence level.

    Args:
        content: The fetched page content (should be HTML/text, not raw bytes)
        url: The URL that was fetched (for domain-specific hints)

    Returns:
        WebFetchQuality with classification and suggested alternatives.
    """
    indicators: list[str] = []
    alternatives: list[str] = []

    # Check content length - very short content often indicates JS rendering
    content_len = len(content)
    if content_len < 200:
        indicators.append("very_short_content")
    elif content_len < 500:
        indicators.append("short_content")

    # Check for high ratio of special characters (minified JS, JSON artifacts)
    if content_len > 0:
        special_chars = sum(1 for c in content if c in "{}[]();,:")
        special_ratio = special_chars / content_len
        if special_ratio > 0.08:
            indicators.append("high_special_char_ratio")

    # Check for JS framework markers
    content_lower = content.lower()
    for marker in JS_FRAMEWORK_MARKERS:
        if marker.lower() in content_lower:
            indicators.append(f"framework_marker:{marker}")
            break  # One marker is enough

    # Check for loading patterns
    for pattern in LOADING_PATTERNS:
        if re.search(pattern, content_lower):
            indicators.append("loading_pattern")
            break

    # Check if content looks like JSON instead of HTML
    stripped = content.strip()
    if stripped.startswith("{") and stripped.endswith("}"):
        indicators.append("json_response")
    elif stripped.startswith("[") and stripped.endswith("]"):
        indicators.append("json_array_response")

    # Check for minimal text content (lots of tags, little text)
    text_content = re.sub(r"<[^>]+>", "", content)
    text_content = re.sub(r"\s+", " ", text_content).strip()
    if len(text_content) < 100 and content_len > 500:
        indicators.append("minimal_text_content")

    # Generate alternatives based on URL
    if url:
        alternatives = _suggest_alternatives_for_url(url)

    # Calculate confidence based on indicators
    if not indicators:
        return WebFetchQuality(
            is_js_rendered=False,
            confidence=0.9,
            reason="No JS rendering indicators detected",
            suggested_alternatives=[],
        )

    # Score indicators
    high_confidence_indicators = {
        "very_short_content",
        "json_response",
        "json_array_response",
        "high_special_char_ratio",
    }
    medium_confidence_indicators = {
        "short_content",
        "minimal_text_content",
        "loading_pattern",
    }

    high_count = sum(
        1 for i in indicators if i.split(":")[0] in high_confidence_indicators
    )
    medium_count = sum(
        1 for i in indicators if i.split(":")[0] in medium_confidence_indicators
    )
    framework_detected = any("framework_marker" in i for i in indicators)

    if high_count >= 2 or (high_count >= 1 and framework_detected):
        confidence = 0.9
    elif high_count >= 1 or (medium_count >= 2 and framework_detected):
        confidence = 0.7
    elif medium_count >= 2 or framework_detected:
        confidence = 0.5
    else:
        confidence = 0.3

    return WebFetchQuality(
        is_js_rendered=True,
        confidence=confidence,
        reason=f"Indicators: {', '.join(indicators)}",
        suggested_alternatives=alternatives,
    )


def _suggest_alternatives_for_url(url: str) -> list[str]:
    """Suggest alternative tools/approaches based on the URL.

    Args:
        url: The URL that was fetched

    Returns:
        List of suggestions for the agent to try
    """
    alternatives: list[str] = []
    url_lower = url.lower()

    # Stock/financial data
    if any(
        d in url_lower
        for d in ["yahoo.com/finance", "tradingview", "marketwatch", "bloomberg"]
    ):
        alternatives.append(
            "Use mcp__markets__stock_price or stock_history for stock data"
        )
        alternatives.append("Use mcp__financial__fred_series for economic indicators")

    # News sites
    if any(d in url_lower for d in ["reuters", "bbc", "cnn", "nytimes", "wsj"]):
        alternatives.append("Use mcp__forecasting__search_news for news content")
        alternatives.append("Use mcp__forecasting__search_exa for web search")

    # Wikipedia
    if "wikipedia" in url_lower:
        alternatives.append("Use mcp__forecasting__wikipedia for Wikipedia content")

    # Social media / dynamic content
    if any(d in url_lower for d in ["twitter", "x.com", "reddit", "facebook"]):
        alternatives.append("Social media requires JavaScript rendering")
        alternatives.append(
            "Consider using mcp__forecasting__search_news for social media coverage"
        )

    # Prediction markets
    if "polymarket" in url_lower:
        alternatives.append("Use mcp__markets__polymarket_price for Polymarket data")
    if "manifold" in url_lower:
        alternatives.append("Use mcp__markets__manifold_price for Manifold data")

    # Generic suggestions
    if not alternatives:
        alternatives.append("Try mcp__forecasting__search_exa for a more robust search")
        alternatives.append(
            "Use sandbox execute_code with requests/beautifulsoup for complex scraping"
        )

    return alternatives


async def classify_haiku(content: str) -> WebFetchQuality:
    """Use Haiku model to classify uncertain WebFetch content.

    Only called when heuristic classification has low confidence.
    Very cheap (~$0.0001 per call) but adds latency.

    Args:
        content: The fetched page content (truncated to 3000 chars)

    Returns:
        WebFetchQuality with Haiku's classification
    """
    from pydantic_ai import Agent

    # Truncate content for efficiency
    truncated = content[:3000] if len(content) > 3000 else content

    agent = Agent[None, WebFetchQuality](
        "anthropic:claude-haiku-4-5-20251001",
        output_type=WebFetchQuality,
        system_prompt=(
            "Classify whether web page content appears to be JavaScript-rendered garbage "
            "(empty page, loading spinner, framework bootstrap code) vs actual content. "
            "Set is_js_rendered=True if the content is useless for information extraction. "
            "Provide suggested_alternatives if you detect specific site types."
        ),
    )

    try:
        result = await agent.run(f"Classify this web content:\n\n{truncated}")
        return result.output
    except Exception as e:
        logger.warning("Haiku classification failed: %s", e)
        # Fall back to uncertain result
        return WebFetchQuality(
            is_js_rendered=True,
            confidence=0.5,
            reason=f"Haiku classification failed: {e}",
            suggested_alternatives=[
                "Try mcp__forecasting__search_exa for a more robust search"
            ],
        )


async def classify_webfetch_content(
    content: str,
    url: str = "",
    confidence_threshold: float = 0.6,
) -> WebFetchQuality:
    """Classify WebFetch content quality with automatic escalation to Haiku.

    Uses fast heuristics first, escalates to Haiku if confidence is below threshold.

    Args:
        content: The fetched page content
        url: The URL that was fetched (for domain-specific hints)
        confidence_threshold: Minimum confidence for heuristic result before
            escalating to Haiku (default: 0.6)

    Returns:
        WebFetchQuality with final classification
    """
    # Try heuristics first
    heuristic_result = classify_heuristic(content, url)

    # If confident enough, return heuristic result
    if heuristic_result.confidence >= confidence_threshold:
        logger.debug(
            "WebFetch classified by heuristics: is_js=%s confidence=%.2f",
            heuristic_result.is_js_rendered,
            heuristic_result.confidence,
        )
        return heuristic_result

    # Escalate to Haiku for uncertain cases
    logger.info(
        "Escalating WebFetch classification to Haiku (heuristic confidence=%.2f)",
        heuristic_result.confidence,
    )
    haiku_result = await classify_haiku(content)

    # Merge alternatives from both
    all_alternatives = list(
        dict.fromkeys(
            heuristic_result.suggested_alternatives
            + haiku_result.suggested_alternatives
        )
    )
    haiku_result.suggested_alternatives = all_alternatives

    return haiku_result


def generate_fallback_message(url: str, classification: WebFetchQuality) -> str:
    """Generate a system message with fallback suggestions.

    Args:
        url: The URL that was fetched (included for context in message)
        classification: The classification result

    Returns:
        Formatted message for the agent with suggestions
    """
    url_display = url[:60] + "..." if len(url) > 60 else url
    lines = [
        f"WebFetch for '{url_display}' returned potentially incomplete content.",
        f"Confidence: {classification.confidence:.0%}",
        f"Reason: {classification.reason}",
        "",
        "Suggested alternatives:",
    ]

    for alt in classification.suggested_alternatives:
        lines.append(f"  - {alt}")

    if not classification.suggested_alternatives:
        lines.append("  - Try a different approach to get this information")

    return "\n".join(lines)
