import random

from generator.generator.generated import ListGenerated
from generator.generator.generator_data import ListData
from generator.generator.mathgen import TwoPoint

from fixtures.space.multiverse import multiverse


class Multiverse(ListGenerated):
    data = {'value': ListData(multiverse)}

    def __init__(self, value):
        super().__init__(value)
        self.positions = TwoPoint()
        self._universes = None

    @property
    def universes(self):
        if not self._universes:
            universes_count = random.randrange(10, 30)
            self._universes = [self.positions.generate() for _ in range(universes_count)]
        return self._universes
