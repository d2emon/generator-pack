from factories.generator import Generated
from factories.generator import ListProvider

from sample_data.fixtures.other import wisdom


class WisdomQuote(Generated):
    provider = ListProvider(wisdom)
