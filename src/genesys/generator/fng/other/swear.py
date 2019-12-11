from genesys.generator import Generated
from genesys.generator import ListProvider


from fixtures.other import swears


class Curse(Generated):
    provider = ListProvider(swears)
