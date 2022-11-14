"""
Basilisk Name.

Traditionally, a basilisk is a small snake-like creature, sometimes with the head of a rooster, and
sometimes merely with a crowned or otherwise crested head. It is capable of causing death with just
its stare and is incredibly venomous.

Today, basilisks are often represented as either huge snakes or as huge lizard-like reptiles. I
focused on these kinds of creatures more for the purposes of this generator as the traditional
basilisk is very similar to the cockatrice, which has its own name generator.

Basilisks don't often have names, but when they do, they're often harsh sounding and with a lot of
reptilian-like sounds, so a lot of hisses, guttural sounds and similar tones made with the back of
their throat.
"""

from data.fng.names import fantasy
from genesys.fng.database import Database
from genesys.fng.factories.name_block_factory import MultipleFactoryNameFactory
from genesys.fng.factories.name_factory import ComplexFactory
from genesys.fng.validators import item_is_unique
from models.fng.names.fantasy import BasiliskName


DB = Database('basilisk', {
    'nm1': fantasy.basilisk.nm1,
    'nm2': fantasy.basilisk.nm2,
    'nm3': fantasy.basilisk.nm3,
    'nm4': fantasy.basilisk.nm4,
    'nm5': fantasy.basilisk.nm5,
})


class BasiliskNameFactory(MultipleFactoryNameFactory):
    """Basilisk Name Factory."""

    class BasiliskNameFactory1(ComplexFactory):
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
            'nm1': 'nm1',
            'nm2': 'nm2',
            'nm3': 'nm3',
            'nm4': 'nm2',
            'nm5': 'nm5',
        }
        model = BasiliskName
        validators = {
            'nm3': lambda items: item_is_unique([items['nm1']]),
            'nm5': lambda items: item_is_unique([items['nm3']]),
        }

    class BasiliskNameFactory2(ComplexFactory):
        """
        Method #2.

        Names that have a much higher chance of having a more melodic sound to them, making
        them ideal for the softer and gentle looking aliens.

        Attributes:
            block_map (dict): Map model fields to database blocks
            model (Model): Model to build
            validators (dict[function]): Validators for model fields

        names = nm1[rnd] + nm2[rnd2] + nm3[rnd3] + nm2[rnd4] + nm4[rnd6] + nm2[rnd7] + nm5[rnd5];
        """

        block_map = {
            'nm1': 'nm1',
            'nm2': 'nm2',
            'nm3': 'nm3',
            'nm4': 'nm4',
            'nm5': 'nm2',
            'nm6': 'nm2',
            'nm7': 'nm5',
        }
        model = BasiliskName
        validators = {
            'nm3': lambda items: item_is_unique([items['nm1']]),
            'nm7': lambda items: item_is_unique([items['nm3']]),
        }


    class BasiliskNameFactory3(ComplexFactory):
        """
        Method #3.

        Names that have a much higher chance of having a more melodic sound to them, making
        them ideal for the softer and gentle looking aliens.

        Attributes:
            block_map (dict): Map model fields to database blocks
            model (Model): Model to build
            validators (dict[function]): Validators for model fields
        """

        block_map = {
            'nm1': 'nm1',
            'nm2': 'nm2',
            'nm3': 'nm4',
            'nm4': 'nm2',
            'nm5': 'nm3',
            'nm6': 'nm2',
            'nm7': 'nm5',
        }
        model = BasiliskName
        validators = {
            'nm5': lambda items: item_is_unique([items['nm1']]),
            'nm7': lambda items: item_is_unique([items['nm5']]),
        }

    class BasiliskNameFactory4(ComplexFactory):
        """
        Method #4.

        Names that can sound both guttural and melodic and anything in between. These names are
        more randomized than the previous 2 types and unlike the other 2 types, these aren't
        always easy to pronounce in English.

        Attributes:
            block_map (dict): Map model fields to database blocks
            model (Model): Model to build
            validators (dict[function]): Validators for model fields
        """

        block_map = {
            'nm1': 'nm1',
            'nm2': 'nm2',
            'nm3': 'nm3',
            'nm4': 'nm2',
            'nm5': 'nm3',
            'nm6': 'nm2',
            'nm7': 'nm5',
        }
        model = BasiliskName
        validators = {
            'nm3': lambda items: item_is_unique([items['nm1']]),
            'nm5': lambda items: item_is_unique([items['nm3']]),
            'nm7': lambda items: item_is_unique([items['nm3']]),
        }

    default_data = DB
    factory_classes = [
        BasiliskNameFactory1,
        BasiliskNameFactory2,
        BasiliskNameFactory3,
    ]
    model = BasiliskName
