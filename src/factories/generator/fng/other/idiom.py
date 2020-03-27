from factories.generator import Generated
from factories.generator import ListProvider

from sample_data.fixtures.other import idiom


class Idiom(Generated):
    provider = ListProvider(idiom)
