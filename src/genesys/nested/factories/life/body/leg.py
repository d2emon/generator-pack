from models.v5 import life
from ...materials import SweatFactory, KeratinFactory
from ..animal_body.body_parts import BodyPartFactory


class KneeFactory(BodyPartFactory):
    default_model = life.Knee


class ToenailFactory(BodyPartFactory):
    default_model = life.Toenail

    def children(self):
        # "dust,40%"
        yield KeratinFactory()


class ToeFactory(BodyPartFactory):
    default_model = life.Toe

    def children(self):
        yield from ToenailFactory()
        yield from super().children()


class FootFactory(BodyPartFactory):
    default_model = life.Foot

    def children(self):
        yield from ToeFactory().multiple(5)
        yield SweatFactory().probable(30)
        yield from super().children()


class LegFactory(BodyPartFactory):
    default_model = life.Leg

    def children(self):
        yield FootFactory()
        yield KneeFactory()
        yield from super().children()
