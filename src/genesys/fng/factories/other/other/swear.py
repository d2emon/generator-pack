from factories.generator import Generated
from factories.list_factory import ListFactory


from data.fixtures.fixtures import swears


class Curse(Generated):
    provider = ListFactory(swears)
