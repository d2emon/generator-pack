from providers import ListProvider
from factories.generator import Generated
from genesys.fixtures.fixtures.other.idiom import idiom


class Idiom(Generated):
    provider = ListProvider(idiom)
