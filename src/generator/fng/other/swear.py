from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider


from fixtures.other.swear import swears


class Curse(Generated):
    provider = ListProvider(swears)
