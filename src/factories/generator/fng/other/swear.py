from factories.generator import Generated
from factories.generator import ListProvider


from sample_data.fixtures import swears


class Curse(Generated):
    provider = ListProvider(swears)
