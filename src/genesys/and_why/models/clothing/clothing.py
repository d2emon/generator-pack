from orm.models.slotted import SlotItem


class Clothing(SlotItem):
    fields = [
        'name'
    ]

    def __init__(self, name, **fields):
        super().__init__(name=name, **fields)

    @property
    def name(self):
        return self['name']

    def __str__(self):
        return str(self.name)
