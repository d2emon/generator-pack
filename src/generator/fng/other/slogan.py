from generator.generator.generated import ListGenerated
from generator.generator.data_provider import ListProvider


from fixtures.other.slogan import slogans


class Slogan(ListGenerated):
    provider = ListProvider(slogans)
