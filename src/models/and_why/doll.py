import random
from models.slotted import Slotted
from . import slots


class Doll(Slotted):
    SLOTS = (
        slots.IN_HAND,
        slots.SHIELD,
        slots.HEAD,
        slots.NECK,
        slots.TORSO,
        slots.HIPS,
    )

    def pop(self, item):
        if item is None:
            return
        print("Takes off {}".format(item.name))
        super().pop(item)

    def push(self, item):
        if item is None:
            return
        self.release(item.slots)
        print("Puts on {}".format(item.name))
        super().push(item)

    def take_off(self, item):
        self.pop(item)

    def put_on(self, item):
        self.push(item)

    def fill_slot(self, slot, items):
        available_items = [item for item in items if slot in item.slots]
        if len(available_items) == 0:
            return
        else:
            self.put_on(random.choice(available_items))

    def fill(self, items):
        chosen_slots = (slot for slot in self.slots if random.randrange(100) < 75)
        for slot in chosen_slots:
            self.fill_slot(slot, items)
