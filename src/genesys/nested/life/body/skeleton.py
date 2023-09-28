from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from genesys.nested.materials.elements import ELEMENTS
from genesys.nested.materials.organics import LipidsFactory
from ..cell import CellFactory


class BoneCellFactory(CellFactory):
    # model = life.BoneCell
    pass


class BonesFactory(NestedFactory):
    # model = life.Bones

    def children(self):
        yield BoneCellFactory.one()
        yield ELEMENTS['Ca'].one()


class BoneFactory(BonesFactory):
    # model = life.Bone
    pass


class MuscleCellFactory(CellFactory):
    # model = life.MuscleCell
    pass


class MuscleFactory(NestedFactory):
    # model = life.Muscles

    def children(self):
        yield MuscleCellFactory.one()


class FatFactory(NestedFactory):
    # model = life.Fat

    def children(self):
        yield LipidsFactory.one()


class SkeletonFactory(NestedFactory):
    # TODO: Refactor it
    # default_model = life.Skeleton

    def children(self):
        yield BonesFactory()
