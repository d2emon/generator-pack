from database.array_database import ArrayDatabase
from models.slotted import SlotItem


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

    @classmethod
    def __create_item(cls, data, models):
        """
        Create clothing item.

        Args:
            data: Clothing data.
            models: Clothing models.

        Returns:
            Clothing: Clothing item.
        """
        clothing_type = data.get('type')
        name = data.get('name', '')

        model = models.get(clothing_type)

        if not model:
            raise ValueError()

        return model(name)


    @classmethod
    def by_data(cls, data, models):
        if data is None:
            return None

        items = (cls.__create_item(item, models) for item in data)
        return cls(items)
