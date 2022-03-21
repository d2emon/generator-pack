import random
from data.and_why.slots import SLOTS
from genesys.model.keyed.slotted import SlotItem


class SlotProvider:
    def __init__(self):
        self.slots = SLOTS.values()

    def item_for_slot(self, slot, items):
        available_items = list(self.items_by_slot(slot, items))
        return random.choice(available_items) if len(available_items) > 0 else None

    def items_by_slot(self, slot, items):
        return SlotItem.by_slot(slot, items)


SLOT_PROVIDER = SlotProvider()
