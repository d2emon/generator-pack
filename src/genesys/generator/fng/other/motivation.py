from genesys.generator import Generated
from genesys.generator import ListProvider


from sample_data.fixtures import motivation


class CharacterGoal(Generated):
    provider = ListProvider(motivation)
