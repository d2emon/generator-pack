from v1.fixtures.data_block import fill_data
from v1.fixtures import genders
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import AngelName
from v1.factories.fng.name_factory import NameFactory, GenderFactory


class AngelNameFactory(GenderFactory):
    """Angel Name Factory

    These angel names are great for any fantasy story, especially those with a more traditional style in terms of names.

    The names have been divided into male, female and neutral. The neutral names are also part of the male and female
    names, so you'll likely come across some doubles if you're looking in multiple sections."""

    class MaleNameFactory(NameFactory):
        model = AngelName
        block_map = {
            'nm1': 1,
        }

    class FemaleNameFactory(NameFactory):
        model = AngelName
        block_map = {
            'nm1': 2,
        }

    class NeutralNameFactory(NameFactory):
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
