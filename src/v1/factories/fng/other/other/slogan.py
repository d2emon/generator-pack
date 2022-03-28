from factories.generator import Generated
from factories.list_factory import ListFactory


from genesys.fixtures.fixtures import slogans


class Slogan(Generated):
    provider = ListFactory(slogans)
