"""Unified MCP tool decorator.

Combines @tool + @tracked + input validation + output serialization +
exception handling into a single decorator. Tools receive a validated
Pydantic model, return plain data, and raise ToolError for recoverable
errors — the decorator handles all MCP response formatting and logging.
"""

import logging
import re
from collections.abc import Awaitable, Callable
from typing import Any

from claude_agent_sdk import SdkMcpTool
from pydantic import BaseModel

from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)

ParamBuilder = Callable[[re.Match[str]], dict[str, Any]]
UrlRoute = tuple[str, ParamBuilder]


class ToolError(Exception):
    """Raised by tool functions to signal a recoverable error.

    The decorator converts this into an MCP error response (is_error=True)
    without logging a traceback (the error is intentional, not a bug).
    """


def _serialize_result(result: Any) -> Any:
    """Serialize a tool result for JSON encoding."""
    if isinstance(result, BaseModel):
        return result.model_dump(mode="json")
    return result


def mcp_tool(
    name: str,
    description: str,
    url_route: UrlRoute | None = None,
) -> Callable[
    [Callable[..., Awaitable[Any]]],
    SdkMcpTool[Any],
]:
    """Decorator that creates an MCP tool with automatic validation and serialization.

    The decorated function:
    - Receives a validated Pydantic model (from first parameter's type annotation)
    - Returns plain data or a BaseModel (auto-serialized via mcp_success)
    - Raises ToolError for intentional errors (converted to mcp_error, no traceback)
    - Any other exception is caught, logged, and converted to mcp_error
    """

    def decorator(
        fn: Callable[..., Awaitable[Any]],
    ) -> SdkMcpTool[Any]:
        annotations = fn.__annotations__
        params = [k for k in annotations if k != "return"]
        if not params:
            raise TypeError(f"mcp_tool '{name}': function must have a typed parameter")

        input_type = annotations[params[0]]
        if not (isinstance(input_type, type) and issubclass(input_type, BaseModel)):
            raise TypeError(
                f"mcp_tool '{name}': first parameter must be a BaseModel subclass, "
                f"got {input_type}"
            )

        schema = input_type.model_json_schema()

        @tracked(name)
        async def handler(args: dict[str, Any]) -> dict[str, Any]:
            try:
                validated = input_type.model_validate(args)
            except Exception as e:
                return mcp_error(f"Invalid input: {e}")
            try:
                result = await fn(validated)
            except ToolError as e:
                return mcp_error(str(e))
            except Exception as e:
                logger.exception("Tool '%s' failed", name)
                return mcp_error(f"{type(e).__name__}: {e}")
            return mcp_success(_serialize_result(result))

        tool = SdkMcpTool(
            name=name,
            description=description,
            input_schema=schema,
            handler=handler,
        )

        if url_route is not None:
            from aib.tools.fetch_routes import register_route

            pattern, param_builder = url_route
            register_route(pattern, handler, param_builder)

        return tool

    return decorator
