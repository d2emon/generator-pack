import random
from data.and_why.egypt import EGYPT
from genesys.model.keyed.slotted import SlotItem
from utils.genders import MALE, FEMALE
from ..models import clothing
from .slot_provider import SlotProvider
from .gender_provider import GenderProvider


class ClothingItems:
    def __init__(self, data):
        self.data = data
        self.__values = None

    @property
    def values(self):
        if self.__values is None:
            self.__values = list(self.data)
        return list(self.__values)

    def random_item(self):
        values = self.values
        return random.choice(values) if len(values) > 0 else None

    def filter(self, condition):
        return ClothingItems(filter(condition, self.values))

    def by_slot(self, slot):
        return ClothingItems(SlotItem.by_slot(slot, self.values))


class ClothingProvider:
    def __init__(self):
        self.__classes = {
            'Accessory': clothing.Accessory,
            'Headdress': clothing.Headdress,
            'Collar': clothing.Collar,
            'Shendyt': clothing.Shendyt,
            'Kalasiris': clothing.Kalasiris,
            'Weapon': clothing.Weapon,
            'Shield': clothing.Shield,
        }

        self.gender_provider = GenderProvider()
        self.slot_provider = SlotProvider()

    def __get_clothing(self, values):
        clothing_class = self.__classes.get(values.get('type'))

        if not clothing_class:
            raise ValueError()

        return clothing_class(values.get('name', ''))

    def by_gender(self, gender):
        d = list(self.gender_provider.by_gender(gender))
        items = map(self.__get_clothing, d)
        i = list(items)
        return ClothingItems(i)


CLOTHING_PROVIDER = ClothingProvider()
