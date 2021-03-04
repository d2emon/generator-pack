from v1.fixtures.data_block import load_data
from v1.fixtures.fng.names import fantasy
from v1.models.fng.names.fantasy import AmazonName
from v1.factories.fng.name_factory import NameFactory, ComplexNameFactory


class AmazonNameFactory(ComplexNameFactory):
    """Amazon Name Factory

    The names are heavily based on the Amazons of ancient Greece, so while most names will have various melodic sounds,
    most names do tend to have a Greek feel to it.

    The Amazons are female warriors who lived in an all-female society. They're known for their strength and power,
    their way of life, and their victories gave them a legendary status. The term Amazon was soon synonymous with female
    warrior.
    Men weren't allowed in the Amazon towns, with the exception of once a year to make sure their tribe didn't go
    extinct.

    The Amazons have been depicted in many modern works of fiction, and their legendary status usually accompanies them,
    like Wonder Woman.
    Even in these modern versions, the Amazon women tend to have Greek or Greek sounding names, like Hippolyta, the
    queen of the Amazons and mother of Diana, otherwise known as Wonder Woman."""

    class AmazonNameFactory1(NameFactory):
        name_class = AmazonName
        blocks_map = {
            1: 1,
            2: 2,
            3: 3,
            4: 5,
            5: 6,
        }

    class AmazonNameFactory2(NameFactory):
        name_class = AmazonName
        blocks_map = {
            1: 1,
            2: 2,
            3: 3,
            4: 2,
            5: 6,
        }

    factory_classes = {
        0: AmazonNameFactory1,
        1: AmazonNameFactory2,
    }
    default_blocks = load_data({
        1: fantasy.amazon.names1,
        2: fantasy.amazon.names2,
        3: fantasy.amazon.names3,
        4: fantasy.amazon.names4,
        5: fantasy.amazon.names5,
        6: fantasy.amazon.names6,
    })

    def get_factory(self, factory_id):
        if factory_id < 50:
            return self.factories[0]
        else:
            return self.factories[1]
