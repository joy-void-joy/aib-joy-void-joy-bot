#!/usr/bin/env python3
"""Inspect Python module APIs.

Usage:
    uv run python scripts/inspect_api.py <module.Class>
    uv run python scripts/inspect_api.py <module.Class.method>
    uv run python scripts/inspect_api.py <module.Class> --help
    uv run python scripts/inspect_api.py <module.Class.method> --help

Examples:
    uv run python scripts/inspect_api.py forecasting_tools.SmartSearcher
    uv run python scripts/inspect_api.py forecasting_tools.MetaculusApi.get_question_by_post_id --help
    uv run python scripts/inspect_api.py mcp.server.fastmcp.FastMCP --help
"""

import argparse
import importlib
import sys


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect Python module APIs")
    parser.add_argument("target", help="Module path like 'module.Class' or 'module.Class.method'")
    parser.add_argument("--help-full", action="store_true", help="Show full help() output")
    args = parser.parse_args()

    parts = args.target.split(".")

    # Try progressively longer module paths
    obj = None
    for i in range(len(parts), 0, -1):
        module_path = ".".join(parts[:i])
        try:
            module = importlib.import_module(module_path)
            obj = module
            # Navigate to the remaining attributes
            for attr in parts[i:]:
                obj = getattr(obj, attr)
            break
        except (ImportError, AttributeError):
            continue

    if obj is None:
        print(f"Could not import or find: {args.target}", file=sys.stderr)
        sys.exit(1)

    if args.help_full:
        help(obj)
    else:
        # Show a summary
        print(f"=== {args.target} ===\n")

        if hasattr(obj, "__doc__") and obj.__doc__:
            doc = obj.__doc__.strip().split("\n")[0]
            print(f"Doc: {doc}\n")

        # List public methods/attributes
        public_attrs = [m for m in dir(obj) if not m.startswith("_")]

        if callable(obj) and not isinstance(obj, type):
            # It's a function/method - show signature
            import inspect
            try:
                sig = inspect.signature(obj)
                print(f"Signature: {obj.__name__}{sig}\n")
            except (ValueError, TypeError):
                pass
        else:
            # It's a class or module - list attributes
            methods = []
            properties = []
            constants = []

            for attr in public_attrs:
                try:
                    val = getattr(obj, attr)
                    if callable(val):
                        methods.append(attr)
                    elif isinstance(val, property):
                        properties.append(attr)
                    else:
                        constants.append(attr)
                except Exception:
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


if __name__ == "__main__":
    main()
