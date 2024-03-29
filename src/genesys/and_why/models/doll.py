from data.and_why import genders
from models.v4.keyed.slotted import Slotted


class Doll(Slotted):
    fields = [
        'gender',
    ]

    def __init__(self, gender=None, **fields):
        super().__init__(gender=gender or genders.DEFAULT, **fields)

    @property
    def gender(self):
        return self['gender']

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
