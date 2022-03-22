from providers import ListProvider
from factories.generator import Generated
from genesys.fixtures.fixtures.other.motivation import motivation


class CharacterGoal(Generated):
    provider = ListProvider(motivation)
