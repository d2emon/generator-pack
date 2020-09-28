from generated import life
from ..body_parts import BodyPartFactory
from ..skeleton import MuscleFactory
from ....materials import MoleculeFactory


class TongueFactory(BodyPartFactory):
    default_model = life.Mouth

    def children(self):
        yield MuscleFactory()


class TeethFactory(BodyPartFactory):
    default_model = life.Mouth

    def children(self):
        yield MoleculeFactory.from_elements('Ca')
        yield MoleculeFactory.from_elements('P')


class MouthFactory(BodyPartFactory):
    default_model = life.Mouth

    def children(self):
        yield TeethFactory()
        yield TongueFactory()
