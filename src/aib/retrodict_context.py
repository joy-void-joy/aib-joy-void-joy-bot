"""ContextVar for retrodict mode cutoff date.

Tools read this to apply time restrictions without hook-based parameter injection.
"""

from contextvars import ContextVar
from datetime import date

retrodict_cutoff: ContextVar[date | None] = ContextVar("retrodict_cutoff", default=None)
