from factories.list_factory import ListFactory
from factories.generator import Generated
from data.fixtures.fixtures.other.motivation import motivation


class CharacterGoal(Generated):
    provider = ListFactory(motivation)
