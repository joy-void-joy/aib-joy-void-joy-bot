"""Shared MCP response utilities.

Provides consistent response formatting across all MCP tool implementations.
"""

import json
from typing import Any


def mcp_success(result: Any) -> dict[str, Any]:
    """Return successful MCP response with JSON-encoded result.

    Args:
        result: The data to return (will be JSON-serialized)

    Returns:
        MCP-formatted success response
    """
    return {"content": [{"type": "text", "text": json.dumps(result, default=str)}]}


def mcp_error(message: str) -> dict[str, Any]:
    """Return error MCP response.

    Args:
        message: Error message to return

    Returns:
        MCP-formatted error response
    """
    return {"content": [{"type": "text", "text": message}], "is_error": True}
