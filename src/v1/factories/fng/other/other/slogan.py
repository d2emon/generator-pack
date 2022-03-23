from providers.list_provider import ListProvider
from factories.generator import Generated


from genesys.fixtures.fixtures import slogans


class Slogan(Generated):
    provider = ListProvider(slogans)
