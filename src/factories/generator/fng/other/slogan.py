from factories.providers import ListProvider
from factories.generator import Generated


from sample_data.fixtures import slogans


class Slogan(Generated):
    provider = ListProvider(slogans)
