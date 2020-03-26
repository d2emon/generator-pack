from genesys.generator import Generated
from genesys.generator import ListProvider


from sample_data.fixtures import swears


class Curse(Generated):
    provider = ListProvider(swears)
