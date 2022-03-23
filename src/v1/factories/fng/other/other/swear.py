from providers.list_provider import ListProvider
from factories.generator import Generated


from genesys.fixtures.fixtures import swears


class Curse(Generated):
    provider = ListProvider(swears)
