from models.v5 import life
from utils.nested import select_item
from ...body.body_parts import BodyPartFactory
from ...body.skin import DandruffFactory
from ..hair import HairFactory
from .ear import EarFactory
from .eye import EyeFactory
from .mouth import MouthFactory
from .nose import NoseFactory
from .skull import SkullFactory


class HeadHairFactory(HairFactory):
    model = life.HeadHair

    def name_factory(self, data, *args, **kwargs):
        return f"{select_item(*data.head_hair)} hair"

    def children(self):
        yield DandruffFactory.one()
        yield from super().children()


class HeadFactory(BodyPartFactory):
    # TODO: Make child of MammalHeadFactory
    model = life.Head

    def mouth(self):
        yield MouthFactory.one()

    def nose(self):
        yield NoseFactory.one()

    def eyes(self):
        yield EyeFactory.probable(99)
        yield EyeFactory.probable(99)

    def ears(self):
        yield EarFactory.multiple(2)

    def skull(self):
        yield SkullFactory.one()

    def hair(self):
        yield HeadHairFactory.probable(85)

    def children(self):
        yield from self.mouth()
        yield from self.nose()
        yield from self.eyes()
        yield from self.ears()
        yield from self.skull()
        yield from self.hair()
        yield from super().children()
