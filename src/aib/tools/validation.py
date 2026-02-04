"""Input validation helpers for MCP tools.

Provides a standardized way to validate tool inputs using Pydantic models
while catching the specific ValidationError (not bare Exception).
"""

from typing import Any

from pydantic import BaseModel, ValidationError

from aib.tools.responses import mcp_error


def validate_input[T: BaseModel](model: type[T], args: dict[str, Any]) -> T | dict[str, Any]:
    """Validate tool input, returning MCP error response on validation failure.

    Uses Pydantic model validation and catches only ValidationError,
    not bare Exception.

    Args:
        model: The Pydantic model class to validate against.
        args: The raw arguments dictionary from the tool call.

    Returns:
        The validated Pydantic model instance if successful,
        or an MCP error dict (with is_error=True) if validation fails.

    Example:
        validated = validate_input(SearchInput, args)
        if isinstance(validated, dict):
            return validated  # Return the error response
        # Use validated.query, validated.limit, etc.
    """
    try:
        return model.model_validate(args)
    except ValidationError as e:
        return mcp_error(f"Invalid input: {e}")
