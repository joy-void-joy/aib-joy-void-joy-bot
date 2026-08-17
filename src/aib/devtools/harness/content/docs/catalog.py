# lup: ignore[constant-declaration]
# Which documents this repository publishes is its own composition, decided
# here because nothing sits above it to be asked.
"""Every document this repository generates under `docs/`.

The roster is the whole of what `docs/` contains: a document not declared
here is not published, and a file found there that generation did not produce
is deleted as unowned.
"""

from pathlib import Path

import lup.harness.models as models

import aib.devtools.harness.content.docs.devtools as devtools

DOCUMENTS = [
    models.Document(
        path=Path("docs/devtools.md"),
        semantic_id="docs.devtools",
        source=devtools.__name__,
        document=devtools.DOCUMENT,
    ),
]
"""What the always-loaded guidance points at instead of carrying.

One document so far. The guidance has a hard byte budget — past it a runtime
truncates the file silently rather than reporting it — so a section that is
looked up rather than read moves here and leaves a pointer behind."""
