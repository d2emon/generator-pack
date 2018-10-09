from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider

from fixtures.other.wisdom import wisdom


class WisdomQuote(ListGenerated):
    provider = ListProvider(wisdom)
