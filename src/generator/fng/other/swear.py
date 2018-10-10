from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider


from fixtures.other.swear import swears


class Curse(ListGenerated):
    provider = ListProvider(swears)
