from genesys.generator import Generated
from genesys.generator import ListProvider

from sample_data.fixtures.other import idiom


class Idiom(Generated):
    provider = ListProvider(idiom)
