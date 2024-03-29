from factories.generator import Generated
from factories.list_factory import ListFactory

from data.fixtures.fixtures.other.wisdom import wisdom


class WisdomQuote(Generated):
    provider = ListFactory(wisdom)
