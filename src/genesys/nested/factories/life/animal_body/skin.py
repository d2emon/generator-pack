from generated import life
from factories.nested_factory import NestedFactory as Factory
from ...materials import SweatFactory, KeratinFactory, ChitinFactory
from ..cell import CellFactory
from ..single_celled import BacteriaFactory


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
        yield BacteriaFactory().multiple(1, 3)
        yield SkinCellFactory()
        yield DeadSkinFactory().probable(50)
        yield SweatFactory().probable(40)


class SkinFactory(Factory):
    default_model = life.Skin

    def children(self):
        yield BacteriaFactory().multiple(1, 3)
        yield ScarFactory().probable(0.5)
        yield PoresFactory()
        yield SkinCellFactory()
        yield DeadSkinFactory()
        # yield Dust.probable(20)
        yield SweatFactory().probable(20)


class ScalesFactory(Factory):
    default_model = life.Scales

    def children(self):
        yield KeratinFactory()


class ExoskeletonFactory(SkinFactory):
    default_model = life.Exoskeleton

    def children(self):
        yield ChitinFactory()
