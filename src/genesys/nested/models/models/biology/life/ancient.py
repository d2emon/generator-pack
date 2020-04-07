from ...unknown import Dinosaur
from .life import LandLife, ForestLife, JungleLife, MountainLife


class AncientLandLife(LandLife):
    class Factory(LandLife.Factory):
        class ChildrenFactory(LandLife.Factory.ChildrenFactory):
            def builders(self):
                yield from Dinosaur.multiple(0, 8)
                yield from super().builders()


class AncientForestLife(ForestLife):
    class Factory(ForestLife.Factory):
        class ChildrenFactory(ForestLife.Factory.ChildrenFactory):
            def builders(self):
                yield from Dinosaur.multiple(0, 5)
                yield from super().builders()


class AncientJungleLife(JungleLife):
    class Factory(JungleLife.Factory):
        class ChildrenFactory(JungleLife.Factory.ChildrenFactory):
            def builders(self):
                yield from Dinosaur.multiple(0, 5)
                yield from super().builders()


class AncientMountainLife(MountainLife):
    class Factory(MountainLife.Factory):
        class ChildrenFactory(MountainLife.Factory.ChildrenFactory):
            def builders(self):
                yield from Dinosaur.multiple(0, 3)
                yield from super().builders()
