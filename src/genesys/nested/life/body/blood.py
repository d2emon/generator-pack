from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from ..cell import CellFactory
# ???
from ...unsorted_life import BacteriaFactory


class BloodCellFactory(CellFactory):
    # model = life.BloodCell
    pass


class BloodFactory(NestedFactory):
    # model = life.Blood

    def children(self):
        yield BloodCellFactory.one()


class BloodVesselsFactory(NestedFactory):
    # model = life.BloodVessels

    def children(self):
        yield BacteriaFactory.probable(30)
        yield BloodFactory.one()
