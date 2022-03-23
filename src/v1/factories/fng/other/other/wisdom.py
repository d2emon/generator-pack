from providers.list_provider import ListProvider
from factories.generator import Generated

from genesys.fixtures.fixtures.other.wisdom import wisdom


class WisdomQuote(Generated):
    provider = ListProvider(wisdom)
