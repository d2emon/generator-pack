from providers import ListProvider
from factories.generator import Generated
from genesys.fixtures.fixtures import mottos


class Motto(Generated):
    provider = ListProvider(mottos)
