import random
from factories.list_factory import ListFactory
from ..providers.slot_provider import SLOT_PROVIDER


class SlotFactory(ListFactory):
    probability = 75

    def __init__(self, data=None):
        super().__init__(data or SLOT_PROVIDER)

    def __check_probability(self):
        return random.randrange(100) < self.probability

    def __call__(self, *args, **kwargs):
        return (
            slot
            for slot in self.data.slots
            if self.__check_probability()
        )
