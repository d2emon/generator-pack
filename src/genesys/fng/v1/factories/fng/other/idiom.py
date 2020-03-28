from factories.providers import ListProvider
from factories.generator import Generated
from sample_data.fixtures.other import idiom


class Idiom(Generated):
    provider = ListProvider(idiom)
