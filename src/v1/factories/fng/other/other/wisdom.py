from providers import ListProvider
from factories.generator import Generated

from genesys.fixtures.fixtures.other import wisdom


class WisdomQuote(Generated):
    provider = ListProvider(wisdom)
