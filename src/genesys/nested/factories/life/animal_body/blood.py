from generated import life
from ...factory import Factory
from ..cell import CellFactory
from ..single_celled import BacteriaFactory


class BloodCellFactory(CellFactory):
    default_model = life.BloodCell


class BloodFactory(Factory):
    default_model = life.Blood

    def children(self):
        yield BloodCellFactory()


class BloodVesselsFactory(Factory):
    default_model = life.BloodVessels

    def children(self):
        yield BacteriaFactory().probable(30)
        yield BloodFactory()
