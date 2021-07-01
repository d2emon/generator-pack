from factories.and_why import Factory
from ..providers.clothing_provider import ClothingProvider
from .slot import SlotFactory


class ClothingFactory(Factory):
    def __init__(self, data=ClothingProvider):
        super().__init__()
        self.__data = data
        self.__slot_factory = SlotFactory(data.slots)

    @property
    def data(self):
        return self.__data

    def __fill_with_items(self, items=None, gender=None):
        return self.__slot_factory.fill_with_items(items or self.data.by_gender(gender))

    def __call__(self, gender=None, items=None, *args, **kwargs):
        return (
            item
            for item in self.__fill_with_items(items, gender)
            if item is not None
        )

    def fill(self, doll, items=None):
        for item in self(gender=doll.gender, items=items):
            doll.put_on(item)
