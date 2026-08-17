"""Per-API rate limits for this project's outbound calls.

The mechanism is :class:`lup.resilience.throttle.Throttle`. What belongs here
is the part that is this project's own: which APIs it talks to, and how hard
each one may be pushed. Every limit is read from settings, and each instance is
a module-level singleton shared by all concurrent forecast sessions in the
process.
"""

from lup.resilience.throttle import Throttle

from aib.config import settings

exa_throttle = Throttle(max_concurrent=settings.exa_max_concurrent)
wayback_throttle = Throttle(max_concurrent=settings.wayback_max_concurrent)
wikipedia_throttle = Throttle(max_concurrent=settings.wikipedia_max_concurrent)
asknews_throttle = Throttle(
    max_concurrent=settings.asknews_max_concurrent,
    min_interval=settings.asknews_min_interval,
)
trends_throttle = Throttle(
    max_concurrent=settings.trends_max_concurrent,
    min_interval=settings.trends_min_interval,
)
fred_throttle = Throttle(max_concurrent=settings.fred_max_concurrent)
arxiv_throttle = Throttle(
    max_concurrent=settings.arxiv_max_concurrent,
    min_interval=settings.arxiv_min_interval,
)
markets_throttle = Throttle(max_concurrent=settings.markets_max_concurrent)
