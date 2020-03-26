from genesys.generator import Generated
from genesys.generator import ListProvider

from sample_data.fixtures.other import wisdom


class WisdomQuote(Generated):
    provider = ListProvider(wisdom)
