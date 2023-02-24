import random
from factories.factory import Factory
from ..providers import PROVIDER


class SlotFactory(Factory):
    def __init__(self, data=None):
        self.data = data or PROVIDER

    @property
    def probability(self):
        return self.data.probability

    @property
    def slots(self):
        return self.data.slots

    def __check_probability(self, value=None):
        if value is None:
            value = random.randrange(100)

        return value < self.probability

    def __call__(self, *args, **kwargs):
        for slot in self.slots:
            if self.__check_probability():
                yield slot
