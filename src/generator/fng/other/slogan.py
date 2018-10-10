from generator.generator.generated import Generated
from generator.generator.data_provider import ListProvider


from fixtures.other.slogan import slogans


class Slogan(Generated):
    provider = ListProvider(slogans)
