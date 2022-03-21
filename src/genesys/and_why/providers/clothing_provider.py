from data.and_why import egypt
from orm.models.data_item import DataItem
from providers import RandomItemProvider
from utils.genders import MALE, FEMALE
from ..models import clothing
from .slot_provider import SlotProvider
from .gender_provider import GenderProvider


class ClothingProvider:
    __filled = False

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
        return map(self.__get_clothing, self.gender_provider.by_gender(gender))

    def fill(self):
        if self.__filled:
            return

        male = list(map(self.__get_clothing, egypt.EGYPT.by_gender(MALE)))
        DataItem.add_values(self.gender_provider.male, male)

        female = list(map(self.__get_clothing, egypt.EGYPT.by_gender(FEMALE)))
        DataItem.add_values(self.gender_provider.female, female)

        self.__filled = True
