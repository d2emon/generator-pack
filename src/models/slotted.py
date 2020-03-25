class SlotItem:
    slots = ()

    @classmethod
    def by_slot(cls, slot, items):
        return (item for item in items if slot in item.slots)


class Slotted:
    def __init__(self):
        self.slots = {}

    def in_slot(self, slot):
        return self.slots.get(slot)

    def release(self, *slots):
        for slot in slots:
            self.pop(self.in_slot(slot))

    def pop(self, item):
        if item is None:
            return
        for slot in item.slots:
            self.slots[slot] = None

    def push(self, item):
        if item is None:
            return
        for slot in item.slots:
            self.slots[slot] = item
