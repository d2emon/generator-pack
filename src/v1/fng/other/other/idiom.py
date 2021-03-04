from providers import ListProvider
from factories.generator import Generated
from genesys.fixtures.fixtures.other import idiom


class Idiom(Generated):
    provider = ListProvider(idiom)
