from models.v5 import life
from ..body.body_parts import BodyPartFactory

from ...unsorted_organics import DustFactory, KeratinFactory, SweatFactory


class ToenailFactory(BodyPartFactory):
    # model = life.Toenail

    def children(self):
        yield DustFactory.probable(40)
        yield KeratinFactory.one()


class ToeFactory(BodyPartFactory):
    # model = life.Toe

    def children(self):
        yield ToenailFactory.one()
        yield from super().children()


class FootFactory(BodyPartFactory):
    # model = life.Foot

    def children(self):
        yield ToeFactory.multiple(5)
        yield SweatFactory.probable(30)
        yield from super().children()


class KneeFactory(BodyPartFactory):
    # model = life.Knee
    pass


class LegFactory(BodyPartFactory):
    # model = life.Leg

    def children(self):
        yield FootFactory.one()
        yield KneeFactory.one()
        yield from super().children()
