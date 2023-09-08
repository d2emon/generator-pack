from factories.data_item_factory import DataItemFactory
from factories.list_factory import ListFactory
from .clothing_items import ClothingItems
from ..data.genders import DEFAULT, MALE, FEMALE
from ..database.genders import GENDERS
from ..database.slots import SLOTS
from ..models import clothing

import data.and_why.egypt


class Provider:
    """
    Provider for slots.

    Attributes:
        clothing_models: Dict for clothing models
        probability: Probability to fill slot
        slots: List of slots
    """

    __clothing_models = {
        'Accessory': clothing.Accessory,
        'Headdress': clothing.Headdress,
        'Collar': clothing.Collar,
        'Shendyt': clothing.Shendyt,
        'Kalasiris': clothing.Kalasiris,
        'Weapon': clothing.Weapon,
        'Shield': clothing.Shield,
    }

    def __init__(self):
        """Create data provider"""
        self.__genders = GENDERS.values()
        self.__slots = SLOTS.values()

        # Factories
        self.__gender_item_providers = { gender: DataItemFactory(gender) for gender in self.__genders }
        self.__gender_factory = ListFactory(self.__genders)

    @property
    def clothing_models(self):
        """Clothing models for ...

        Returns:
            dict: Dict with clothing models
        """
        return self.__clothing_models

    @property
    def probability(self):
        return 75

    @property
    def slots(self):
        return self.__slots

    @property
    def default_gender(self):
        return DEFAULT

    @property
    def male(self):
        return MALE

    @property
    def female(self):
        return FEMALE

    @property
    def gender_item_providers(self):
        return self.__gender_item_providers

    def gender(self):
        """
        Build gender by factory.

        Returns:
            Gender from factory.
        """
        return self.__gender_factory()

    def data_by_gender(self, gender):
        """
        Get data from provider for gender.

        Args:
            gender: Gender for data provider.

        Returns:
            Data from provider.
        """
        provider = self.gender_item_providers.get(gender)
        return provider.data if provider else None

    def by_gender(self, gender):
        """
        Create clothing items for gender.

        Args:
            gender: Gender to create clothing items.

        Returns:
            ClothingItems: Clothing items for gender.
        """
        data = self.data_by_gender(gender)
        return ClothingItems.by_data(data, self.clothing_models)


PROVIDER = Provider()
