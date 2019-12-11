from genesys.generator import Generated
from genesys.generator import ListProvider


from fixtures.other import slogans


class Slogan(Generated):
    provider = ListProvider(slogans)
