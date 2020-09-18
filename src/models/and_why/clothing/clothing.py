from orm.models.slotted import SlotItem


class Clothing(SlotItem):
    def __init__(self, name):
        self.name = name
