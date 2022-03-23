from factories.factory import Factory
from ..providers.clothing_provider import CLOTHING_PROVIDER
from .slot import SlotFactory


class ClothingFactory(Factory):
    def __init__(self, data=None):
        super().__init__()

        # Providers
        self.__clothing_provider = data or CLOTHING_PROVIDER
        self.__slot_provider = self.__clothing_provider.slot_provider

        # Factories
        self.__slot_factory = SlotFactory(self.__slot_provider)

    def __call__(self, gender=None, items=None, *args, **kwargs):
        to_fill = items or self.__clothing_provider.by_gender(gender)

        for slot in self.__slot_factory():
            item = to_fill.by_slot(slot).random_item()
            if item is not None:
                yield item

    def fill(self, doll, items=None):
        for item in self(gender=doll.gender, items=items):
            doll.put_on(item)
