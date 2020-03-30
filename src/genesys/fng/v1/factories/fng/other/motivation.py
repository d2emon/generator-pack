from providers import ListProvider
from factories.generator import Generated
from sample_data.fixtures import motivation


class CharacterGoal(Generated):
    provider = ListProvider(motivation)
