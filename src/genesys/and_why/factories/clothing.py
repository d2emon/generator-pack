from factories.factory import Factory
from .slot import SlotFactory
from ..providers import PROVIDER


class ClothingFactory(Factory):
    def __init__(self, data=None):
        super().__init__()

        # Providers
        self.__provider = data or PROVIDER

        # Factories
        self.__slot_factory = SlotFactory(self.__provider)

    def __call__(self, gender=None, items=None, *args, **kwargs):
        to_fill = items or self.__provider.by_gender(gender)
        if not to_fill:
            return

        for slot in self.__slot_factory():
            item = to_fill.by_slot(slot).random()
            if item is not None:
                yield item

    def fill(self, doll, items=None):
        for item in self(gender=doll.gender, items=items):
            doll.put_on(item)
