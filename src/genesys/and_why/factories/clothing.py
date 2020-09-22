from factories import Factory
from .slot import SlotFactory
from ..managers import DollManager


class ClothingFactory(Factory):
    def __init__(self, provider=None):
        super().__init__()
        self.__data = provider
        self.__slot_factory = SlotFactory(provider)
        self.__manager = DollManager(provider)

    @property
    def data(self):
        return self.__data

    def build(self, gender=None, items=None, *args, **kwargs):
        items = list(items or self.__manager.by_gender(gender))
        return (item for item in self.__slot_factory.select_items(items) if item is not None)

    def fill(self, doll, items=None):
        for item in self.build(gender=doll.gender, items=items):
            doll.put_on(item)
