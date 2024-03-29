from database.data_block import fill_data
from utils import genders
from data.fng.names import fantasy
from models.fng.names.fantasy import AngelName
from genesys.fng.factories.name_factory import ComplexNameFactory, GenderFactory
from genesys.fng.factories.name_block_factory import NameBlockFactory, GenderNameBlockFactory


class AngelNameFactory(GenderNameBlockFactory):
    """Angel Name Factory

    These angel names are great for any fantasy story, especially those with a more traditional style in terms of names.

    The names have been divided into male, female and neutral. The neutral names are also part of the male and female
    names, so you'll likely come across some doubles if you're looking in multiple sections."""

    class MaleNameFactory(ComplexNameFactory):
        model = AngelName

        block_map = {
            'nm1': 1,
        }

    class FemaleNameFactory(ComplexNameFactory):
        model = AngelName

        block_map = {
            'nm1': 2,
        }

    class NeutralNameFactory(ComplexNameFactory):
        model = AngelName

        block_map = {
            'nm1': 3,
        }

    factory_classes = {
        genders.MALE: MaleNameFactory,
        genders.FEMALE: FemaleNameFactory,
        genders.NEUTRAL: NeutralNameFactory,
    }

    default_data = fill_data(group_id='angel')({
        1: fantasy.angel.names1,
        2: fantasy.angel.names2,
        3: fantasy.angel.names3,
    })
