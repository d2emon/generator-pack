from genesys.nested.models.models.unknown import AncientLandLife, AncientForestLife, AncientJungleLife, AncientMountainLife, Trees, JungleTrees,\
    Humus, Grass, CavemanSettlement, WallPainting
from .soil import Soil
from .water import River, Lake
from .land import Plain, Forest, Jungle, Mountain, Cave
from genesys.nested.models.models.chemistry import Fire, Snow, Rock


class AncientPlain(Plain):
    class ChildrenFactory(Plain.ChildrenFactory):
        def children_classes(self):
            yield Fire.probable(0.3)
            yield CavemanSettlement.probable(40)
            yield AncientLandLife
            yield from River.multiple(0, 3)
            yield from Lake.multiple(0, 1)
            yield Grass
            yield Soil
            yield Snow.probable(5)


class AncientForest(Forest):
    class ChildrenFactory(Forest.ChildrenFactory):
        def children_classes(self):
            yield Fire.probable(0.3)
            yield CavemanSettlement.probable(40)
            yield AncientForestLife
            yield from River.multiple(0, 2)
            yield Trees
            yield Grass
            yield Humus
            yield Soil
            yield Snow.probable(5)


class AncientJungle(Jungle):
    class ChildrenFactory(Jungle.ChildrenFactory):
        def children_classes(self):
            yield Fire.probable(0.3)
            yield CavemanSettlement.probable(40)
            yield AncientJungleLife
            yield from River.multiple(0, 2)
            yield JungleTrees
            yield Grass
            yield Humus
            yield Soil


class AncientCave(Cave):
    class ChildrenFactory(Cave.ChildrenFactory):
        def children_classes(self):
            yield CavemanSettlement.probable(65)
            yield WallPainting.probable(50)
            yield WallPainting.probable(30)
            yield WallPainting.probable(30)
            yield super().children_classes()


class AncientMountain(Mountain):
    class ChildrenFactory(Mountain.ChildrenFactory):
        def children_classes(self):
            yield CavemanSettlement.probable(40)
            yield AncientMountainLife
            yield AncientCave.probable(30)
            yield AncientCave.probable(20)
            yield AncientCave.probable(10)
            yield from River.multiple(0, 3)
            yield from Lake.multiple(0, 1)
            yield Trees
            yield Soil
            yield Rock
            yield Snow.probable(40)
