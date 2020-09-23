from genesys.model.keyed.model import Model


class SlotItem(Model):
    slots = ()

    @classmethod
    def by_slot(cls, slot, items):
        return (item for item in items if slot in item.slots)


class Slotted(Model):
    def __init__(self, **fields):
        super().__init__(**fields)
        self.slots = {}

    def __get_slot(self, slot):
        return self.slots.get(slot)

    def __set_slot(self, slot, item):
        self.slots[slot] = item

    def __fill_slots(self, slots, value):
        for slot in slots:
            self.__set_slot(slot, value)

    def in_slot(self, slot):
        return self.__get_slot(slot)

    def pop(self, item):
        if item is not None:
            self.__fill_slots(item.slots, None)

    def push(self, item):
        if item is not None:
            self.__fill_slots(item.slots, item)

    def release(self, *slots):
        for slot in slots:
            self.pop(self.__get_slot(slot))
