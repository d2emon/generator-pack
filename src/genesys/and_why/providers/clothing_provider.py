import random
from data.and_why.egypt import EGYPT
from data.and_why.genders import GENDERS
from models.v4.keyed.slotted import SlotItem
from factories.providers.random_item import RandomItemProvider
from ..models import clothing
from .provider_query import ProviderQuery
from .slot_provider import SlotProvider
from .gender_provider import GenderProvider


class ClothingItems(ProviderQuery):
    def by_slot(self, slot):
        return self.__class__(SlotItem.by_slot(slot, self.values))


class BaseClothingProvider:
    @property
    def slot_provider(self):
        raise NotImplementedError()

    def by_gender(self, gender):
        raise NotImplementedError()


class ClothingProvider(BaseClothingProvider):
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

        # Providers
        self.__slot_provider = SlotProvider()
        self.__item_providers = { gender: RandomItemProvider(gender) for gender in GENDERS.values() }

    @property
    def slot_provider(self):
        return self.__slot_provider

    def __get_clothing(self, values):
        clothing_class = self.__classes.get(values.get('type'))

        if not clothing_class:
            raise ValueError()

        return clothing_class(values.get('name', ''))

    def by_gender(self, gender):
        provider = self.__item_providers.get(gender)
        return ClothingItems(map(self.__get_clothing, provider.data)) if provider else None


CLOTHING_PROVIDER = ClothingProvider()
