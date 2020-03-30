from providers import ListProvider
from factories.generator import Generated

from sample_data.fixtures.other import wisdom


class WisdomQuote(Generated):
    provider = ListProvider(wisdom)
