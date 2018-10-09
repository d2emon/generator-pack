from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider


from fixtures.other.motivation import motivation


class CharacterGoal(ListGenerated):
    provider = ListProvider(motivation)
