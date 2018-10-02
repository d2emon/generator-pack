from generator.generator.generated import ListGenerated
from generator.generator.generator_data import ListData

from fixtures.other.wisdom import wisdom


class WisdomQuote(ListGenerated):
    data = {'value': ListData(wisdom)}
