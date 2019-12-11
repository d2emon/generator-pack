from genesys.generator import Generated
from genesys.generator import ListProvider


from fixtures.other.motivation import motivation


class CharacterGoal(Generated):
    provider = ListProvider(motivation)
