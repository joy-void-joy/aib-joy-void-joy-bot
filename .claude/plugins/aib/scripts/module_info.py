#!/usr/bin/env python3
"""Inspect Python module information.

Get paths and source code for installed modules.
"""

import sys
from typing import Annotated

import typer

app = typer.Typer(help="Inspect Python modules")


@app.command()
def path(
    module: Annotated[
        str,
        typer.Argument(
            help="Module name (e.g., 'forecasting_tools.helpers.asknews_searcher')"
        ),
    ],
) -> None:
    """Print the file path of a Python module."""
    import importlib

    mod = importlib.import_module(module)
    if hasattr(mod, "__file__") and mod.__file__:
        print(mod.__file__)
    else:
        print(
            f"Module {module} has no __file__ attribute (built-in or namespace package)"
        )
        sys.exit(1)


@app.command()
def source(
    module: Annotated[str, typer.Argument(help="Module name")],
    lines: Annotated[
        int, typer.Option("--lines", "-n", help="Number of lines to show (0 = all)")
    ] = 100,
) -> None:
    """Print the source code of a Python module."""
    import importlib
    import inspect

    mod = importlib.import_module(module)
    try:
        src = inspect.getsource(mod)
        if lines > 0:
            source_lines = src.split("\n")
            src = "\n".join(source_lines[:lines])
            if len(source_lines) > lines:
                src += f"\n... ({len(source_lines) - lines} more lines)"
        print(src)
    except (TypeError, OSError) as e:
        print(f"Cannot get source for {module}: {e}")
        sys.exit(1)


if __name__ == "__main__":
    app()
