import random
from factories.and_why import ListFactory
from ..providers.slot_provider import SlotProvider


class SlotFactory(ListFactory):
    probability = 75

    def __init__(self, data=None):
        super().__init__(data or SlotProvider())

    def by_slot(self, slot, items):
        available_items = self.data.by_slot(slot, items)
        return random.choice(available_items) if len(available_items) > 0 else None

    def fill_with_items(self, items):
        for slot in self():
            yield self.by_slot(slot, items)

    def __check_probability(self):
        return random.randrange(100) < self.probability

    def __call__(self, *args, **kwargs):
        return (
            slot
            for slot in self.data.slots
            if self.__check_probability()
        )
