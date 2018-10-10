from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider

from fixtures.other.wisdom import wisdom


class WisdomQuote(Generated):
    provider = ListProvider(wisdom)
