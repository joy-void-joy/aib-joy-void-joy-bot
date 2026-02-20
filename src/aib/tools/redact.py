"""Shared text redaction for retrodict mode.

Used by markets.py and forecasting.py to strip future-dated references
from fine print before exposing to the forecasting agent.
"""

import logging

logger = logging.getLogger(__name__)


async def redact_future_info(text: str, cutoff_date: str) -> str:
    """Remove references to events after the cutoff date via Sonnet."""
    if not text or len(text) < 20:
        return text

    from aib.agent.client import one_shot

    prompt = (
        f"Remove any references to events, dates, or outcomes that occur after {cutoff_date}. "
        f"Keep all other content unchanged. Return ONLY the redacted text, nothing else.\n\n"
        f"Text:\n{text}"
    )
    try:
        result = await one_shot(
            prompt,
            model="sonnet",
            system_prompt=(
                "You redact temporal information from text. Remove sentences or clauses "
                "that reference events after the given date. Preserve everything else verbatim. "
                "Return only the redacted text."
            ),
        )
        return result or text
    except Exception:
        logger.warning("Fine-print redaction failed, returning original")
        return text
