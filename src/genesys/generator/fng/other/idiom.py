from genesys.generator import Generated
from genesys.generator import ListProvider

from fixtures.other import idiom


class Idiom(Generated):
    provider = ListProvider(idiom)
