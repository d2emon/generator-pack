from factories.generator import Generated
from factories.generator import ListProvider


from sample_data.fixtures import mottos


class Motto(Generated):
    provider = ListProvider(mottos)
