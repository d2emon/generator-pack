from data.and_why.slots import SLOTS
from data.and_why.genders import DEFAULT, GENDERS
from factories.data_item_factory import DataItemFactory
from factories.list_factory import ListFactory
from utils.genders import MALE, FEMALE
from .clothing_items import ClothingItems
from ..models import clothing

import data.and_why.egypt


class Provider:
    """
    Provider for slots.

    Attributes:
        clothing_classes: Classes for clothing
        probability: Probability to fill slot
        slots: List of slots
    """

    __classes = {
        'Accessory': clothing.Accessory,
        'Headdress': clothing.Headdress,
        'Collar': clothing.Collar,
        'Shendyt': clothing.Shendyt,
        'Kalasiris': clothing.Kalasiris,
        'Weapon': clothing.Weapon,
        'Shield': clothing.Shield,
    }

    def __init__(self):
        self.__gender_item_providers = { gender: DataItemFactory(gender) for gender in GENDERS.values() }
        self.__slots = SLOTS.values()

        # Factories
        self.__gender_factory = ListFactory(self.__gender_item_providers.keys())

    @property
    def clothing_classes(self):
        return self.__classes

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

    def __clothing_class(self, clothing_type):
        """
        Translate clothing type to clothing class.

        Args:
            clothing_type: Type of clothing.

        Returns:
            __class__: Class for clothing.
        """
        return self.clothing_classes.get(clothing_type)

    def __clothing(self, values):
        """
        Create clothing item.

        Args:
            values: values for clothing.

        Returns:
            Clothing: Clothing from provider classes.
        """
        clothing_class = self.__clothing_class(values.get('type'))

        if not clothing_class:
            raise ValueError()

        return clothing_class(values.get('name', ''))

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
        provider = self.__gender_item_providers.get(gender)
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
        if data is None:
            return None

        return ClothingItems((self.__clothing(values) for values in data))


PROVIDER = Provider()
