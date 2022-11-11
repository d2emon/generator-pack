from factories.generator import Generated
from factories.list_factory import ListFactory
from data.fixtures.fixtures.other.idiom import idiom


class Idiom(Generated):
    provider = ListFactory(idiom)
