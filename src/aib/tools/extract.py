"""Shared content extraction via Sonnet one-shot LLM call.

Used by wikipedia, fetch_arxiv, and fetch_url tools to extract
specific information from large text content.
"""

import logging

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient, ResultMessage

logger = logging.getLogger(__name__)


async def extract_with_prompt(content: str, prompt: str, source: str = "") -> str:
    """Use a one-shot Sonnet call to extract information from content.

    Args:
        content: Raw text content (no truncation — Sonnet handles full input).
        prompt: What information to extract.
        source: Source identifier (URL, paper ID, etc.) for context.

    Returns:
        Extracted information as a string. Falls back to truncated
        content (5k chars) if extraction fails.
    """
    extraction_prompt = (
        f"The following is the text content of {source}.\n\n"
        f"---\n{content}\n---\n\n"
        f"Based on the above content, answer the following: {prompt}\n\n"
        "Be concise and factual. If the content doesn't contain "
        "relevant information, say so.\n\n"
        "After your answer, if the content contains links that could "
        "provide deeper or more current information on this topic, "
        "list them under a 'Relevant links:' section as markdown links."
    )

    options = ClaudeAgentOptions(
        model="sonnet",
        system_prompt="You extract information from text content. Be concise and factual.",
        extra_args={"no-session-persistence": None},
    )

    result_text = ""
    async with ClaudeSDKClient(options=options) as client:
        await client.query(extraction_prompt)
        async for message in client.receive_response():
            if (
                not result_text
                and isinstance(message, ResultMessage)
                and message.result
            ):
                result_text = message.result

    return result_text or content[:5000]
