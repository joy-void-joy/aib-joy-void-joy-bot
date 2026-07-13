"""The `claude` command group: Claude Code runner (default) + `usage`.

`lup-devtools claude` launches Claude Code wired for this project (research
tools + local plugin + active profile). Extra args forward straight to
`claude` (e.g. `claude --resume`); `claude run` is the explicit escape hatch
for args that collide with a subcommand name, and `claude usage` shows usage.
"""

import json
import os
import tempfile
from pathlib import Path
from typing import Annotated

import click
import sh
import typer
from pydantic import BaseModel, Field
from typer.core import TyperGroup

from aib.devtools.usage import app as usage_app
from aib.paths import PROJECT_ROOT

MCP_SERVER_NAME = "research"
DEFAULT_CONFIG_DIR = Path.home() / ".claude"
CONFIG_DIR_ENV = "CLAUDE_CONFIG_DIR"
REGISTRY_PATH = Path.home() / ".lup" / "profiles.json"


class Account(BaseModel):
    """One registered account: the config dir the runner reads as its home."""

    config_dir: str


class Registry(BaseModel):
    """The registry document as stored on disk: named profiles plus the active pick."""

    profiles: dict[str, Account] = Field(default_factory=dict)
    active: str | None = None


def load_registry() -> Registry:
    """Read the profile registry; a missing file reads as empty.

    The registry lives at `~/.lup/profiles.json` — machine-wide and shared
    with lup projects, because Claude accounts are reused across projects.
    """
    if not REGISTRY_PATH.exists():
        return Registry()
    return Registry.model_validate_json(REGISTRY_PATH.read_text())


def resolve_config_dir(name: str | None = None) -> Path:
    """Resolve a Claude config dir: explicit name > active profile > default."""
    registry = load_registry()
    chosen = name or registry.active
    if chosen is None:
        return DEFAULT_CONFIG_DIR
    if chosen not in registry.profiles:
        known = ", ".join(sorted(registry.profiles)) or "none"
        typer.echo(
            f"Error: unknown profile '{chosen}' in {REGISTRY_PATH} (known: {known})",
            err=True,
        )
        raise typer.Exit(1)
    return Path(registry.profiles[chosen].config_dir).expanduser()


def write_mcp_config() -> str:
    """Write a temp MCP config running the research tools over stdio; return its path."""
    config = {
        "mcpServers": {
            MCP_SERVER_NAME: {
                "command": "uv",
                "args": ["run", "lup-devtools", "agent", "serve-tools"],
            }
        }
    }
    tmp = tempfile.NamedTemporaryFile(
        mode="w", suffix=".json", prefix="aib-mcp-", delete=False
    )
    json.dump(config, tmp)
    tmp.close()
    return tmp.name


def run_claude(
    profile: str | None,
    model: str | None,
    no_tools: bool,
    no_plugin: bool,
    with_prompt: bool,
    extra_args: list[str],
) -> None:
    """Exec into `claude` configured for this project (see module docstring)."""
    args: list[str] = []

    if model:
        args.extend(["--model", model])

    if with_prompt:
        from aib.agent.prompts import get_forecasting_system_prompt

        args.extend(["--append-system-prompt", get_forecasting_system_prompt()])

    plugin_dir = PROJECT_ROOT / ".claude" / "plugins" / "aib"
    if not no_plugin:
        if plugin_dir.is_dir():
            args.extend(["--plugin-dir", str(plugin_dir)])
        else:
            typer.echo(
                f"Note: no local plugin at {plugin_dir}; skipping --plugin-dir",
                err=True,
            )

    mcp_path: str | None = None
    if not no_tools:
        mcp_path = write_mcp_config()
        # =-form: --mcp-config is variadic and would swallow forwarded args
        args.append(f"--mcp-config={mcp_path}")

    args.extend(extra_args)

    config_dir = resolve_config_dir(profile)
    env = {**os.environ, CONFIG_DIR_ENV: str(config_dir)}
    shown = profile or load_registry().active or "default"
    typer.echo(f"Launching claude (profile: {shown}, config dir: {config_dir})")

    try:
        sh.Command("claude")(*args, _fg=True, _env=env)
    except sh.CommandNotFound as e:
        typer.echo(
            "Error: 'claude' CLI not found. Install Claude Code first.", err=True
        )
        raise typer.Exit(1) from e
    except sh.ErrorReturnCode:
        pass  # claude exited non-zero or the user quit
    finally:
        if mcp_path:
            try:
                Path(mcp_path).unlink()
            except OSError:
                pass


class ClaudeRunnerGroup(TyperGroup):
    """Forward any non-subcommand invocation through `run` to `claude`.

    A Typer group resolves the first token as a subcommand, so `claude
    --resume` or `claude mcp` would otherwise error before reaching the
    runner. Routing unknown tokens to `run` lets `claude <args>` pass
    straight through to `claude` while keeping real subcommands (`usage`)
    and the explicit `claude run` escape hatch for collisions.
    """

    def resolve_command(
        self, ctx: click.Context, args: list[str]
    ) -> tuple[str | None, click.Command | None, list[str]]:
        if args and args[0] not in self.commands:
            args = ["run", *args]
        return super().resolve_command(ctx, args)


app = typer.Typer(
    cls=ClaudeRunnerGroup,
    help="Run Claude Code wired for this project (tools, local plugin, profile)",
    invoke_without_command=True,
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
app.add_typer(usage_app, name="usage", help="API usage and rate limits")


@app.command(
    "run",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def run_cmd(
    ctx: typer.Context,
    profile: Annotated[
        str | None,
        typer.Option("--profile", "-p", help="Claude profile (CLAUDE_CONFIG_DIR)"),
    ] = None,
    model: Annotated[
        str | None,
        typer.Option("--model", "-m", help="Model override (e.g. sonnet, opus)"),
    ] = None,
    no_tools: Annotated[
        bool,
        typer.Option("--no-tools", help="Skip attaching the research MCP tools"),
    ] = False,
    no_plugin: Annotated[
        bool,
        typer.Option("--no-plugin", help="Skip loading the local aib plugin"),
    ] = False,
    with_prompt: Annotated[
        bool,
        typer.Option(
            "--prompt/--no-prompt", help="Append the forecasting system prompt"
        ),
    ] = False,
) -> None:
    """Launch Claude Code with the project's tools, local plugin, and profile.

    Extra args pass through to `claude` (e.g. `claude run --resume`); the
    `--` is only needed for args that collide with this command's own options.
    """
    run_claude(profile, model, no_tools, no_plugin, with_prompt, ctx.args)


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    """Launch Claude Code with project defaults when no subcommand is given."""
    if ctx.invoked_subcommand is not None:
        return
    run_claude(
        profile=None,
        model=None,
        no_tools=False,
        no_plugin=False,
        with_prompt=False,
        extra_args=[],
    )
