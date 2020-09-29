from .land import PlainFactory, ForestFactory, JungleFactory, MountainFactory, CaveFactory


class AncientPlainFactory(PlainFactory):
    @classmethod
    def life(cls):
        # yield CavemanSettlement.probable(40)
        # yield AncientLandLife
        yield None


class AncientForestFactory(ForestFactory):
    @classmethod
    def life(cls):
        # yield CavemanSettlement.probable(40)
        # yield AncientForestLife
        yield None


class AncientJungleFactory(JungleFactory):
    @classmethod
    def life(cls):
        # yield CavemanSettlement.probable(40)
        # yield AncientJungleLife
        yield None


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
        # yield AncientMountainLife
        yield None

    @classmethod
    def cave(cls):
        yield AncientCaveFactory().probable(30)
        yield AncientCaveFactory().probable(30)
        yield AncientCaveFactory().probable(20)
