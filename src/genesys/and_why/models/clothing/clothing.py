from orm.models.slotted import SlotItem


class Clothing(SlotItem):
    def __init__(self, name, **fields):
        super().__init__(**fields)
        self.name = name
