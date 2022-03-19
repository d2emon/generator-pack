from ..life import AncientLandLifeFactory, AncientForestLifeFactory, AncientJungleLifeFactory, \
    AncientMountainLifeFactory
from .land import PlainFactory, ForestFactory, JungleFactory, MountainFactory, CaveFactory


class AncientPlainFactory(PlainFactory):
    @classmethod
    def life(cls):
        # yield CavemanSettlement.probable(40)
        yield AncientLandLifeFactory()


class AncientForestFactory(ForestFactory):
    @classmethod
    def life(cls):
        # yield CavemanSettlement.probable(40)
        yield AncientForestLifeFactory()


class AncientJungleFactory(JungleFactory):
    @classmethod
    def life(cls):
        # yield CavemanSettlement.probable(40)
        yield AncientJungleLifeFactory()


class AncientCaveFactory(CaveFactory):
    @classmethod
    def life(cls):
        # yield CavemanSettlement.probable(65)
        yield from super().life()

    def children(self):
        # yield WallPainting.probable(50)
        # yield WallPainting.probable(30)
        # yield WallPainting.probable(30)
        yield super().children()


class AncientMountainFactory(MountainFactory):
    @classmethod
    def life(cls):
        # yield CavemanSettlement.probable(40)
        yield AncientMountainLifeFactory()

    @classmethod
    def cave(cls):
        yield AncientCaveFactory().probable(30)
        yield AncientCaveFactory().probable(30)
        yield AncientCaveFactory().probable(20)
