from factories.list_factory import ListFactory
from models.fng.names.name import Name

from data.fixtures.fixtures.other.wisdom import wisdom


class WisdomQuote(Name):
    provider = ListFactory(wisdom)
