from models.slotted import SlotItem


class Clothing(SlotItem):
    class Slots:
        IN_HAND = 1
        SHIELD = 2
        HEAD = 3
        NECK = 4
        TORSO = 5
        HIPS = 6

    def __init__(self, name):
        self.name = name
