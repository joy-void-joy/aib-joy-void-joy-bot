#!/usr/bin/env python3
"""Inspect Python module APIs.

Examples:
    uv run python scripts/inspect_api.py forecasting_tools.SmartSearcher
    uv run python scripts/inspect_api.py forecasting_tools.MetaculusApi.get_question_by_post_id
    uv run python scripts/inspect_api.py mcp.server.fastmcp.FastMCP --help-full
"""

import importlib
import inspect
import sys
from typing import Annotated, Any

import typer

app = typer.Typer(help="Inspect Python module APIs")


def resolve_target(target: str) -> tuple[Any, None] | tuple[None, str]:
    """Resolve a dotted path to a Python object."""
    parts = target.split(".")

    for i in range(len(parts), 0, -1):
        module_path = ".".join(parts[:i])
        try:
            module = importlib.import_module(module_path)
            obj = module
            for attr in parts[i:]:
                obj = getattr(obj, attr)
            return obj, None
        except (ImportError, AttributeError):
            continue

    return None, f"Could not import or find: {target}"


def print_summary(target: str, obj: Any) -> None:
    """Print a summary of the object."""
    print(f"=== {target} ===\n")

    if hasattr(obj, "__doc__") and obj.__doc__:
        doc = obj.__doc__.strip().split("\n")[0]
        print(f"Doc: {doc}\n")

    public_attrs = [m for m in dir(obj) if not m.startswith("_")]

    if callable(obj) and not isinstance(obj, type):
        try:
            sig = inspect.signature(obj)
            print(f"Signature: {obj.__name__}{sig}\n")
        except (ValueError, TypeError):
            pass
    else:
        methods: list[str] = []
        properties: list[str] = []
        constants: list[str] = []

        for attr in public_attrs:
            try:
                val = getattr(obj, attr)
                if callable(val):
                    methods.append(attr)
                elif isinstance(val, property):
                    properties.append(attr)
                else:
                    constants.append(attr)
            except AttributeError:
                constants.append(attr)

        if methods:
            print(f"Methods ({len(methods)}):")
            for m in sorted(methods):
                print(f"  - {m}")
            print()

        if properties:
            print(f"Properties ({len(properties)}):")
            for p in sorted(properties):
                print(f"  - {p}")
            print()

        if constants and len(constants) <= 20:
            print(f"Constants ({len(constants)}):")
            for c in sorted(constants):
                print(f"  - {c}")


@app.command()
def main(
    target: Annotated[
        str,
        typer.Argument(help="Module path like 'module.Class' or 'module.Class.method'"),
    ],
    help_full: Annotated[
        bool,
        typer.Option("--help-full", help="Show full help() output"),
    ] = False,
) -> None:
    """Inspect a Python module, class, or method."""
    obj, error = resolve_target(target)

    if error:
        print(error, file=sys.stderr)
        raise typer.Exit(1)

    if help_full:
        help(obj)
    else:
        print_summary(target, obj)


if __name__ == "__main__":
    app()
