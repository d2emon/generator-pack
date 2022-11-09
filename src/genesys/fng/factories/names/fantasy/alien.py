"""
Alien Species Name.

It's both easy and difficult to create alien names, as they can be anything in any language. But
the names have to sound like a good fit for the species you've invented, so I've tried to make
sure many different types of names can be generated, but they generally fit in 3 different
categories.

Attributes:
    DB (Database): Default database for factory.

Classes:
    AlienNameFactory: Alien Species Name Factory.
"""

from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import MultipleFactoryNameFactory
from genesys.fng.factories.name_factory import ComplexFactory
from genesys.fng.factories.validators import item_is_unique, item_is_not_empty, validate_if
from models.fng.names.fantasy import AlienName


DB = Database('aliens', {
    1: fantasy.alien.nm1,
    2: fantasy.alien.nm2,
    3: fantasy.alien.nm3,
    4: fantasy.alien.nm4,
    5: fantasy.alien.nm5,

    6: fantasy.alien.nm6,
    7: fantasy.alien.nm7,
    8: fantasy.alien.nm8,
    # 9
    10: fantasy.alien.nm10,

    11: fantasy.alien.nm11,
    12: fantasy.alien.nm12,
    13: fantasy.alien.nm13,
    14: fantasy.alien.nm14,
    15: fantasy.alien.nm15,

    16: fantasy.alien.nm16,
})


class AlienNameFactory(MultipleFactoryNameFactory):
    """
    Alien Species Name Factory.

    Attributes:
        data (Database): Database for factory. Inherited from DBFactory.
        default_data (Database): Default database for factory.
        factories (list[Factory]): Nested factories. Inherited from MultipleFactoryNameFactory.
        factory_classes (list[class]): Classes for nested factories.
        model (Model): Model to build.
    """

    class AlienNameFactory1(ComplexFactory):
        """
        Method #1.

        Names with a much higher chance of having a more guttural sound to them, ideal for the
        stronger and brutish looking aliens.

        Attributes:
            block_map (dict): Map model fields to database blocks
            model (Model): Model to build
            validators (dict[function]): Validators for model fields
        """

        block_map = {
            'nm1': 1,
            'nm2': 2,
            'nm3': 3,
            'nm4': 4,
            'nm5': 5,
        }
        model = AlienName
        validators = {
            'nm3': lambda items: item_is_unique([items['nm1'], items['nm5']]),
            'nm4': lambda items: validate_if(
                lambda: str(items['nm3']) != '',
                item_is_not_empty(),
            ),
        }
        update_values = {
            'nm4': lambda self, items: '' if str(items['nm3']) == '' else items['nm4'],
        }

    class AlienNameFactory2(ComplexFactory):
        """
        Method #2.

        Names that have a much higher chance of having a more melodic sound to them, making
        them ideal for the softer and gentle looking aliens.

        Attributes:
            block_map (dict): Map model fields to database blocks
            model (Model): Model to build
            validators (dict[function]): Validators for model fields
        """

        block_map = {
            'nm1': 6,
            'nm2': 7,
            'nm3': 8,
            'nm4': 10,
            'nm5': 11,
        }
        model = AlienName
        validators = {
            'nm3': lambda items: item_is_unique([items['nm1'], items['nm5']]),
        }

    class AlienNameFactory3(ComplexFactory):
        """
        Method #3.

        Names that can sound both guttural and melodic and anything in between. These names are
        more randomized than the previous 2 types and unlike the other 2 types, these aren't
        always easy to pronounce in English.

        Attributes:
            block_map (dict): Map model fields to database blocks
            model (Model): Model to build
            validators (dict[function]): Validators for model fields
        """

        block_map = {
            'nm1': 12,
            'nm2': 13,
            'nm3': 14,
            'nm4': 15,
            'nm5': 16,
        }
        model = AlienName
        validators = {
            'nm3': lambda items: item_is_unique([items['nm1'], items['nm5']]),
            'nm4': lambda items: validate_if(
                lambda: str(items['nm3']) != '',
                item_is_not_empty(),
            ),
        }
        update_values = {
            'nm4': lambda self, items: '' if str(items['nm3']) == '' else items['nm4'],
        }

    default_data = DB
    factory_classes = [
        AlienNameFactory1,
        AlienNameFactory2,
        AlienNameFactory3,
    ]
    model = AlienName
