"""
Amusement park name.

This name generator will give you random names for amusement parks, theme parks and other similar
businesses.

The names in this generator have been based on existing amusement park names, but I mostly stuck to
the fairly generic names. Real parks usually have those names, but sometimes also include a place
name or a person's name in their name (sort of like Disneyland Paris in a way).
"""

from data.fng.names.place.amusement_park import first1, first2, second1, second2
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import MultipleFactoryNameFactory
from genesys.fng.factories.name_factory import ComplexFactory
from models.fng.names.name import Name


DB = Database('amusement-park', {
    'first1': first1,
    'first2': first2,
    'last1': second1,
    'last2': second2,
})


class AmusementPark(Name):
    """Amusement park name model."""

    @property
    def value(self) -> str:
        """
        Get model value.

        Returns:
            str: Value for model
        """
        if isinstance(self.built_with, AmusementParkFactory2):
            return " ".join(self.values)

        return "".join(self.values)


class AmusementParkFactory1(ComplexFactory):
    """
    Method #1.

    2 word combinations which form a one word name. Names like 'Thrillville', 'Spiritrealm' and
    'Questworld'.
    """

    parts = [
        'first1',
        'last1',
    ]
    model = AmusementPark


class AmusementParkFactory2(ComplexFactory):
    """
    Method #2.

    2-4 word names, names like 'Kids Paradise', 'Family Fun World', 'Magic Dome', and 'Shadow
    Kingdom'.
    """

    parts = [
        'first2',
        'last2',
    ]
    model = AmusementPark


class AmusementParkFactory(MultipleFactoryNameFactory):
    """
    Amusement park name factory.

    This name generator will give you 10 random names for amusement parks, theme parks and other
    similar businesses.

    The names in this generator have been based on existing amusement park names, but I mostly
    stuck to the fairly generic names. Real parks usually have those names, but sometimes also
    include a place name or a person's name in their name (sort of like Disneyland Paris in a way).
    """

    default_data = DB
    factory_classes = [
        AmusementParkFactory1,
        AmusementParkFactory2,
    ]
    model = AmusementPark
