from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from ...materials.elements import ELEMENTS
from ...materials.organics import LipidsFactory
from ..cell import CellFactory


class BoneCellFactory(CellFactory):
    model = life.BoneCell


class BonesFactory(NestedFactory):
    model = life.Bones

    def children(self):
        yield BoneCellFactory.one()
        yield ELEMENTS['Ca'].one()


class BoneFactory(BonesFactory):
    model = life.Bone


class MuscleCellFactory(CellFactory):
    model = life.MuscleCell


class MuscleFactory(NestedFactory):
    model = life.Muscles

    def children(self):
        yield MuscleCellFactory.one()


class FatFactory(NestedFactory):
    model = life.Fat

    def children(self):
        yield LipidsFactory.one()


class SkeletonFactory(NestedFactory):
    # TODO: Refactor it
    default_model = life.Skeleton

    def children(self):
        yield BonesFactory()
