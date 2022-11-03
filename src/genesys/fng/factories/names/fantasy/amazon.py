"""
Amazon Name.

The names are heavily based on the Amazons of ancient Greece, so while most names will have various
melodic sounds, most names do tend to have a Greek feel to it.

The Amazons are female warriors who lived in an all-female society. They're known for their
strength and power, their way of life, and their victories gave them a legendary status. The term
Amazon was soon synonymous with female warrior.
Men weren't allowed in the Amazon towns, with the exception of once a year to make sure their tribe
didn't go extinct.

The Amazons have been depicted in many modern works of fiction, and their legendary status usually
accompanies them, like Wonder Woman.
Even in these modern versions, the Amazon women tend to have Greek or Greek sounding names, like
Hippolyta, the queen of the Amazons and mother of Diana, otherwise known as Wonder Woman.
"""

from database.data_block import fill_data
from data.fng.names import fantasy
from models.fng.names.fantasy import AmazonName
from genesys.fng.factories.name_factory import ComplexNameFactory
from genesys.fng.factories.name_block_factory import NameBlockFactory


class AmazonNameFactory(NameBlockFactory):
    """Amazon Name Factory."""

    class AmazonNameFactory1(ComplexNameFactory):
        """Method #1."""

        model = AmazonName

        block_map = {
            'nm1': 1,
            'nm2': 2,
            'nm3': 3,
            'nm4': 5,
            'nm5': 6,
        }

    class AmazonNameFactory2(ComplexNameFactory):
        """Method #1."""

        model = AmazonName

        block_map = {
            'nm1': 1,
            'nm2': 2,
            'nm3': 3,
            'nm4': 2,
            'nm5': 6,
        }

    factory_classes = {
        0: AmazonNameFactory1,
        1: AmazonNameFactory2,
    }

    default_data = fill_data(group_id='amazon')({
        1: fantasy.amazon.names1,
        2: fantasy.amazon.names2,
        3: fantasy.amazon.names3,
        4: fantasy.amazon.names4,
        5: fantasy.amazon.names5,
        6: fantasy.amazon.names6,
    })

    def by_percent(self, percent):
        return self.by_percent_2(percent)
