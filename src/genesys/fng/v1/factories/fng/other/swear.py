from providers import ListProvider
from factories.generator import Generated


from sample_data.fixtures import swears


class Curse(Generated):
    provider = ListProvider(swears)
