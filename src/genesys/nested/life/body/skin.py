from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from ..cell import CellFactory

from ...unsorted_organics import DustFactory, KeratinFactory, SweatFactory

# ???
from ...materials.organics import ChitinFactory
# ???
from ...unsorted_life import BacteriaFactory


class SkinCellFactory(CellFactory):
    # model = life.SkinCell
    pass


class DeadSkinFactory(NestedFactory):
    # model = life.DeadSkin

    def children(self):
        yield SkinCellFactory.one()


class ScarFactory(NestedFactory):
    # model = life.Scar

    def children(self):
        yield DeadSkinFactory()


class PoresFactory(NestedFactory):
    # model = life.Pores

    def children(self):
        yield BacteriaFactory.multiple(1, 3)
        yield SkinCellFactory.one()
        yield DeadSkinFactory.probable(50)
        yield SweatFactory.probable(40)


class SkinFactory(NestedFactory):
    # model = life.Skin

    def children(self):
        yield BacteriaFactory.multiple(1, 3)
        yield ScarFactory.probable(0.5)
        yield PoresFactory.one()
        yield SkinCellFactory.one()
        yield DeadSkinFactory.one()
        yield DustFactory.probable(20)
        yield SweatFactory.probable(20)


class DandruffFactory(NestedFactory):
    # model = life.Dandruff

    def children(self):
        yield DeadSkinFactory()


class ScalesFactory(NestedFactory):
    # TODO: Refactor it
    # default_model = life.Scales

    def children(self):
        yield KeratinFactory()


class ExoskeletonFactory(SkinFactory):
    # TODO: Refactor it
    # default_model = life.Exoskeleton

    def children(self):
        yield ChitinFactory()
