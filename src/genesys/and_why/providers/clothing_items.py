from database.array_database import ArrayDatabase
from models.v4.keyed.slotted import SlotItem


class ClothingItems(ArrayDatabase):
    def __init__(self, data):
        super().__init__()
        self.__data = list(data)

    @property
    def data(self):
        return self.__data

    def by_slot(self, slot):
        return self.__class__(SlotItem.by_slot(slot, self.data))

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.data}>"

    def __str__(self):
        return str(self.data)
