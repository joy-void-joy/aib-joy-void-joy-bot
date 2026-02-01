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

    The `is_error` flag is properly propagated when using `create_mcp_server`
    from `aib.tools.mcp_server` (our patched version that fixes SDK bugs).

    Args:
        message: Error message to return

    Returns:
        MCP-formatted error response with is_error=True
    """
    return {"content": [{"type": "text", "text": message}], "is_error": True}
