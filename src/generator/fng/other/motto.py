from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider


from fixtures.other.motto import mottos


class Motto(Generated):
    provider = ListProvider(mottos)
