from factories.list_factory import ListFactory
from factories.generator import Generated
from data.fixtures.fixtures import mottos


class Motto(Generated):
    provider = ListFactory(mottos)
