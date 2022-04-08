from models.v5 import life
from factories.nested_factory import NestedFactory as Factory
from ...materials import MoleculeFactory, LipidsFactory
from ..cell import CellFactory


class BoneCellFactory(CellFactory):
    default_model = life.BoneCell


class BonesFactory(Factory):
    default_model = life.Bones

    def children(self):
        yield BoneCellFactory()
        yield MoleculeFactory.from_elements('Ca')


class BoneFactory(BonesFactory):
    default_model = life.Bone


class MuscleCellFactory(CellFactory):
    default_model = life.MuscleCell


class MuscleFactory(Factory):
    default_model = life.Muscles

    def children(self):
        yield MuscleCellFactory()


class FatFactory(Factory):
    default_model = life.Fat

    def children(self):
        yield LipidsFactory()


class SkeletonFactory(Factory):
    default_model = life.Skeleton

    def children(self):
        yield BonesFactory()
