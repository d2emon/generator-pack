from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider


from fixtures.other.motivation import motivation


class CharacterGoal(Generated):
    provider = ListProvider(motivation)
