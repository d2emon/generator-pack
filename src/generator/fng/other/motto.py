from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider


from fixtures.other.motto import mottos


class Motto(ListGenerated):
    provider = ListProvider(mottos)
