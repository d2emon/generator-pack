from models.v5 import life
from genesys.nested.materials.elements import ELEMENTS
from ...body.body_parts import BodyPartFactory, SkinlessSoftBodyPartFactory
from ...body.skeleton import MuscleFactory


class TeethFactory(BodyPartFactory):
    # model = life.Teeth

    def children(self):
        yield ELEMENTS['Ca'].one()
        yield ELEMENTS['P'].one()


class TongueFactory(BodyPartFactory):
    # model = life.Mouth

    def children(self):
        yield MuscleFactory.one()


class MouthFactory(BodyPartFactory):
    # model = life.Mouth

    def children(self):
        yield TeethFactory.one()
        yield TongueFactory.one()


class SimpleMouthFactory(SkinlessSoftBodyPartFactory):
    # TODO: Refactor it
    # default_model = life.SimpleMouth

    def children(self):
        yield TeethFactory()
        yield from super().children()
