from factories.providers import ListProvider
from factories.generator import Generated
from sample_data.fixtures import mottos


class Motto(Generated):
    provider = ListProvider(mottos)
