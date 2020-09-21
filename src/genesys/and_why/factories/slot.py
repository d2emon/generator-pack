import random
from factories import ListFactory
from orm.models.slotted import SlotItem
from genesys.and_why.models.slots import SLOTS


class SlotFactory(ListFactory):
    def __init__(self, provider=None, slots=None):
        super().__init__(provider, slots or SLOTS)

    @classmethod
    def item_by_slot(cls, slot, items):
        available_items = list(SlotItem.by_slot(slot, items))
        return random.choice(available_items) if len(available_items) > 0 else None

    def model(self, *args, **kwargs):
        return (slot for slot in self.data if random.randrange(100) < 75)

    def select_items(self, items):
        return (self.item_by_slot(slot, items) for slot in self.model())
