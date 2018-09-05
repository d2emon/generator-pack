from generator.generator.generated import ListGenerated
from generator.generator.generator_data import ListData

from fixtures.space.multiverse import multiverse


class Multiverse(ListGenerated):
    data = {'value': ListData(multiverse)}
