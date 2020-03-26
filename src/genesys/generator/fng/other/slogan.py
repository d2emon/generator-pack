from genesys.generator import Generated
from genesys.generator import ListProvider


from sample_data.fixtures import slogans


class Slogan(Generated):
    provider = ListProvider(slogans)
