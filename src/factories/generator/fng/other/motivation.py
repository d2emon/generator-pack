from factories.generator import Generated
from factories.generator import ListProvider


from sample_data.fixtures import motivation


class CharacterGoal(Generated):
    provider = ListProvider(motivation)
