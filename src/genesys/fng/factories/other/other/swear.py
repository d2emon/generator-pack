from factories.generator import Generated
from factories.list_factory import ListFactory


from genesys.fixtures.fixtures import swears


class Curse(Generated):
    provider = ListFactory(swears)
