from generated import life
from ...factory import Factory
from ...materials import SweatFactory
from ..cell import CellFactory


class SkinCellFactory(CellFactory):
    default_model = life.SkinCell


class DeadSkinFactory(Factory):
    default_model = life.DeadSkin


class ScarFactory(Factory):
    default_model = life.Scar

    def children(self):
        yield DeadSkinFactory()


class PoresFactory(Factory):
    default_model = life.Pores

    def children(self):
        # yield Bacteria.multiple(1, 3)
        yield SkinCellFactory()
        yield DeadSkinFactory().probable(50)
        yield SweatFactory().probable(40)


class SkinFactory(Factory):
    default_model = life.Skin

    def children(self):
        # yield Bacteria.multiple(1, 3)
        yield ScarFactory().probable(0.5)
        yield PoresFactory()
        yield SkinCellFactory()
        yield DeadSkinFactory()
        # yield Dust.probable(20)
        yield SweatFactory().probable(20)
