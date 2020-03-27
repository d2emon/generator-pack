from factories.generator import Generated
from factories.generator import ListProvider


from sample_data.fixtures import slogans


class Slogan(Generated):
    provider = ListProvider(slogans)
