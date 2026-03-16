"""Throttled proxy for the AskNews remote MCP server.

Wraps the remote AskNews MCP server (https://mcp.asknews.app) with rate
limiting via the Throttle class. The free tier allows 1 request per 10 seconds
with 1 concurrent request.

Instead of registering the remote server directly as McpHttpServerConfig, this
module creates a local MCP server that proxies tool calls to the remote server
with throttling applied.
"""

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


async def _call_remote(api_key: str, tool_name: str, arguments: dict[str, Any]) -> str:
    """Call a tool on the remote AskNews MCP server with throttling."""
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
    return "\n".join(texts)


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
                return list(result.tools)

    @server.call_tool()
    async def call_tool(name: str, arguments: dict[str, Any]) -> CallToolResult:
        try:
            text = await _call_remote(api_key, name, arguments)
            content: list[ContentBlock] = [TextContent(type="text", text=text)]
            return CallToolResult(content=content, isError=False)
        except Exception:
            logger.exception("AskNews tool %s failed", name)
            err: list[ContentBlock] = [
                TextContent(type="text", text=f"AskNews {name} failed")
            ]
            return CallToolResult(content=err, isError=True)

    return McpSdkServerConfig(type="sdk", name="asknews", instance=server)
