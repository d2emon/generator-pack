from providers import ListProvider
from factories.generator import Generated
from genesys.fixtures.fixtures import motivation


class CharacterGoal(Generated):
    provider = ListProvider(motivation)
