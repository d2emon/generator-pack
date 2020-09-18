import random
from orm.models.slotted import Slotted, SlotItem
from .. import slots


class DollModel(Slotted):
    SLOTS = slots.SLOTS

    def __init__(self, gender):
        super().__init__()
        self.gender = gender

    def pop(self, item):
        if item is None:
            return
        print("Takes off {}".format(item.name))
        super().pop(item)

    def push(self, item):
        if item is None:
            return
        self.release(*item.slots)
        print("Puts on {}".format(item.name))
        super().push(item)

    def take_off(self, item):
        self.pop(item)

    def put_on(self, item):
        self.push(item)

    def __random_slots(self):
        return (slot for slot in self.SLOTS if random.randrange(100) < 75)

    @classmethod
    def __random_item(cls, slot, items):
        available_items = list(SlotItem.by_slot(slot, items))
        return random.choice(available_items) if len(available_items) > 0 else None

    def fill(self, items):
        items = list(items)
        for slot in self.__random_slots():
            self.put_on(self.__random_item(slot, items))
