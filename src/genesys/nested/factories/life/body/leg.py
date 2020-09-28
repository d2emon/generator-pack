from generated import life
from .body_parts import BodyPartFactory


class KneeFactory(BodyPartFactory):
    default_model = life.Knee

    def children(self):
        # yield Dust.probable(40)
        # yield Keratin
        yield from super().children()


class ToenailFactory(BodyPartFactory):
    default_model = life.Toenail

    def children(self):
        yield ToenailFactory()
        yield from super().children()


class ToeFactory(BodyPartFactory):
    default_model = life.Toe

    def children(self):
        yield from ToeFactory().multiple(5)
        # yield Sweat.probable(30)
        yield from super().children()


class FootFactory(BodyPartFactory):
    default_model = life.Foot

    def children(self):
        yield from ToeFactory().multiple(5)
        # yield Sweat.probable(30)
        yield from super().children()


class LegFactory(BodyPartFactory):
    default_model = life.Leg

    def children(self):
        yield FootFactory()
        yield KneeFactory()
        yield from super().children()
