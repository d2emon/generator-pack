from data.and_why import egypt
from orm.models.data_item import DataItem
from providers import RandomItemProvider
from ..models import clothing
from .slot_provider import SlotProvider
from .gender_provider import GenderProvider


class ClothingProvider:
    slots = SlotProvider

    __classes = {
        'Accessory': clothing.Accessory,
        'Headdress': clothing.Headdress,
        'Collar': clothing.Collar,
        'Shendyt': clothing.Shendyt,
        'Kalasiris': clothing.Kalasiris,
        'Weapon': clothing.Weapon,
        'Shield': clothing.Shield,
    }
    __factories = {gender: RandomItemProvider(gender) for gender in GenderProvider.genders}

    @classmethod
    def by_gender(cls, gender):
        factory = cls.__factories.get(gender)
        return factory.data if factory else None

    @classmethod
    def __get_clothing(cls, values):
        clothing_class = cls.__classes.get(values.get('type'))
        if not clothing_class:
            raise ValueError()
        return clothing_class(values.get('name', ''))

    @classmethod
    def fill(cls):
        male = map(cls.__get_clothing, egypt.MALE)
        DataItem.add_values(GenderProvider.male, male)

        female = map(cls.__get_clothing, egypt.FEMALE)
        DataItem.add_values(GenderProvider.female, female)


ClothingProvider.fill()