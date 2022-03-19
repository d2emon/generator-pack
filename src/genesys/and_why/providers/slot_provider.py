from data.and_why.slots import SLOTS
from genesys.model.keyed.slotted import SlotItem


class SlotProvider:
    slots = SLOTS

    @classmethod
    def by_slot(cls, slot, items):
        return list(SlotItem.by_slot(slot, items))
