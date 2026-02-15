"""Service health checks."""

import shutil
from collections.abc import Callable

import sh
import typer

app = typer.Typer(no_args_is_help=True)


def _check_metaculus() -> tuple[bool, str]:
    """Check Metaculus API connectivity."""
    try:
        from aib.config import settings

        if not settings.metaculus_token:
            return False, "METACULUS_TOKEN not set"
        return True, f"token valid ({settings.metaculus_token[:8]}...)"
    except (OSError, ValueError) as e:
        return False, str(e)


def _check_exa() -> tuple[bool, str]:
    """Check Exa Search API key."""
    try:
        from aib.config import settings

        if not settings.exa_api_key:
            return False, "EXA_API_KEY not set"
        return True, "key configured"
    except (OSError, ValueError) as e:
        return False, str(e)


def _check_fred() -> tuple[bool, str]:
    """Check FRED API key."""
    try:
        from aib.config import settings

        if not settings.fred_api_key:
            return False, "FRED_API_KEY not set"
        return True, "key configured"
    except (OSError, ValueError) as e:
        return False, str(e)


def _check_docker() -> tuple[bool, str]:
    """Check Docker daemon availability."""
    if not shutil.which("docker"):
        return False, "docker not found in PATH"

    try:
        docker = sh.Command("docker")
        docker("info", _timeout=5, _tty_out=False)
        return True, "daemon running"
    except sh.ErrorReturnCode:
        return False, "daemon not running"
    except sh.TimeoutException:
        return False, "daemon timed out"
    except sh.CommandNotFound:
        return False, "docker not found"


_CheckFn = Callable[[], tuple[bool, str]]

CHECKS: list[tuple[str, _CheckFn]] = [
    ("Metaculus API", _check_metaculus),
    ("Exa Search", _check_exa),
    ("FRED API", _check_fred),
    ("Docker", _check_docker),
]


@app.command("check")
def check() -> None:
    """Ping each external dependency and report status."""
    all_ok = True
    for name, checker in CHECKS:
        ok, detail = checker()
        status = "OK" if ok else "FAIL"
        typer.echo(f"  {name:20s} ... {status:4s}  ({detail})")
        if not ok:
            all_ok = False

    if not all_ok:
        raise typer.Exit(1)
