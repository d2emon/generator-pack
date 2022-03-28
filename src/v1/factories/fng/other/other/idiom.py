from factories.generator import Generated
from factories.list_factory import ListFactory
from genesys.fixtures.fixtures.other.idiom import idiom


class Idiom(Generated):
    provider = ListFactory(idiom)
