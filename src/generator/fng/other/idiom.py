from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider

from fixtures.other.idiom import idiom


class Idiom(Generated):
    provider = ListProvider(idiom)
