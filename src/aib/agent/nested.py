"""Generic wrapper for nested-agent results.

Augments the structured payload produced by a nested agent with the
agent's final free-form text block and any error collated during the
run. The agent does not write this structure directly — the runner
builds it from the validated payload, the captured text stream, and
any exception/validation failure.
"""

from pydantic import BaseModel


class NestedAgentReport[T: BaseModel](BaseModel):
    payload: T | None = None
    final_text: str = ""
    error: str | None = None
    session_id: str | None = None
    trace: str = ""
