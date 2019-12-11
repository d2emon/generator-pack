from genesys.generator import Generated
from genesys.generator import ListProvider

from fixtures.other import wisdom


class WisdomQuote(Generated):
    provider = ListProvider(wisdom)
