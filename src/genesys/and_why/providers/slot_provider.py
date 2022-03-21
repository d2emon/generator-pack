from data.and_why.slots import SLOTS
from genesys.model.keyed.slotted import SlotItem


class SlotProvider:

    def __init__(self):
        self.slots = SLOTS.values()

    def by_slot(self, slot, items):
        return list(SlotItem.by_slot(slot, items))
