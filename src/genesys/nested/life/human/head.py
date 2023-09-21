from models.v5 import life
from utils.nested import select_item
from ..body.body_parts import BodyPartFactory

# ???
# from ..body.skin import DeadSkinFactory
# ???
from ..body.hair import HairFactory, DandruffFactory
# ???
from ..body.head import NoseFactory, EyeFactory, MouthFactory, EarFactory, SkullFactory
# ???
# from ..animals.mammal import MammalHeadFactory


class HeadHairFactory(HairFactory):
    default_model = life.HeadHair
    names = ["brown", "black", "gray", "light", "blonde", "red", "dark"]

    def generate_name(self):
        return f"{select_item(*self.names)} hair"

    def children(self):
        yield DandruffFactory()
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
