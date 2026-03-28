"""Throttled proxy for the AskNews remote MCP server.

Wraps the remote AskNews MCP server (https://mcp.asknews.app) with rate
limiting via the Throttle class and retry logic for transient rate limit
errors. The free tier allows 1 request per 10 seconds with 1 concurrent
request, but 429s still occur occasionally.

Instead of registering the remote server directly as McpHttpServerConfig, this
module creates a local MCP server that proxies tool calls to the remote server
with throttling and retry applied.

This uses the raw @server.call_tool() pattern instead of @mcp_tool because
tool schemas are discovered dynamically from the remote server at runtime.
"""

import asyncio
import logging
from typing import Any

import httpx
from claude_agent_sdk.types import McpSdkServerConfig
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client
from mcp.server import Server
from mcp.types import CallToolResult, ContentBlock, TextContent, Tool

from aib.tools.throttle import asknews_throttle

logger = logging.getLogger(__name__)

ASKNEWS_MCP_URL = "https://mcp.asknews.app"
MAX_RETRIES = 3
RETRY_BASE_WAIT = 15.0

HIDDEN_TOOLS: set[str] = {"search_google"}


class AskNewsRateLimitError(Exception):
    """Raised when AskNews returns a rate limit error, enabling retry."""


class AskNewsRemoteError(Exception):
    """Raised when the remote AskNews server returns a non-rate-limit error."""


def _to_content(text: str) -> list[ContentBlock]:
    return [TextContent(type="text", text=text)]


async def _call_remote_once(
    api_key: str, tool_name: str, arguments: dict[str, Any]
) -> str:
    """Single attempt to call a tool on the remote AskNews MCP server."""
    async with asknews_throttle:
        http_client = httpx.AsyncClient(
            timeout=60,
            headers={"x-api-key": api_key},
        )
        async with streamable_http_client(
            url=ASKNEWS_MCP_URL,
            http_client=http_client,
        ) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(tool_name, arguments)

    texts = [block.text for block in result.content if isinstance(block, TextContent)]
    text = "\n".join(texts)

    if result.isError:
        if "rate limit" in text.lower() or "429" in text:
            raise AskNewsRateLimitError(text)
        raise AskNewsRemoteError(text)

    return text


async def _call_remote(api_key: str, tool_name: str, arguments: dict[str, Any]) -> str:
    """Call a tool on the remote AskNews MCP server with throttling and retry."""
    last_err: AskNewsRateLimitError | None = None
    for attempt in range(MAX_RETRIES):
        try:
            return await _call_remote_once(api_key, tool_name, arguments)
        except AskNewsRateLimitError as exc:
            last_err = exc
            wait = RETRY_BASE_WAIT * (2**attempt)
            logger.warning(
                "AskNews rate limited (attempt %d/%d), waiting %.0fs",
                attempt + 1,
                MAX_RETRIES,
                wait,
            )
            await asyncio.sleep(wait)
    raise last_err  # type: ignore[misc]


def create_asknews_server(api_key: str) -> McpSdkServerConfig:
    """Create a throttled local proxy for the AskNews remote MCP server."""
    server = Server("asknews", version="1.0.0")

    @server.list_tools()
    async def list_tools() -> list[Tool]:
        http_client = httpx.AsyncClient(
            timeout=30,
            headers={"x-api-key": api_key},
        )
        async with streamable_http_client(
            url=ASKNEWS_MCP_URL,
            http_client=http_client,
        ) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.list_tools()
                return [t for t in result.tools if t.name not in HIDDEN_TOOLS]

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> CallToolResult:
        if name in HIDDEN_TOOLS:
            return CallToolResult(
                content=_to_content(f"AskNews tool {name} is not available."),
                isError=True,
            )
        try:
            text = await _call_remote(api_key, name, arguments)
            return CallToolResult(content=_to_content(text), isError=False)
        except AskNewsRemoteError as exc:
            return CallToolResult(content=_to_content(str(exc)), isError=True)
        except AskNewsRateLimitError:
            msg = f"AskNews {name} rate limited after {MAX_RETRIES} retries. Try again later or use alternative news sources."
            logger.warning(msg)
            return CallToolResult(content=_to_content(msg), isError=True)
        except Exception:
            logger.exception("AskNews tool %s failed", name)
            return CallToolResult(
                content=_to_content(f"AskNews {name} failed"), isError=True
            )

    return McpSdkServerConfig(type="sdk", name="asknews", instance=server)
