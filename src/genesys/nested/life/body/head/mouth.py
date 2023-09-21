from models.v5 import life
from ....materials import MoleculeFactory
from ..body_parts import BodyPartFactory, SkinlessSoftBodyPartFactory
from ..skeleton import MuscleFactory


class TeethFactory(BodyPartFactory):
    default_model = life.Teeth

    def children(self):
        yield MoleculeFactory.element_factories('Ca', 'P')


class SimpleMouthFactory(SkinlessSoftBodyPartFactory):
    default_model = life.SimpleMouth

    def children(self):
        yield TeethFactory()
        yield from super().children()


class TongueFactory(BodyPartFactory):
    default_model = life.Mouth

    def children(self):
        yield MuscleFactory()


class MouthFactory(BodyPartFactory):
    default_model = life.Mouth

    def children(self):
        yield TeethFactory()
        yield TongueFactory()
