from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider

from fixtures.other.idiom import idiom


class Idiom(ListGenerated):
    provider = ListProvider(idiom)
