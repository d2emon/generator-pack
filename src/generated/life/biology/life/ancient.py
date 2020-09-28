from generated.nested_v2.models.unknown import Dinosaur
from .life import LandLife, ForestLife, JungleLife, MountainLife


class AncientLandLife(LandLife):
    class Factory(LandLife.Factory):
        def children(self):
            yield from Dinosaur.multiple(0, 8)
            yield from super().children()


class AncientForestLife(ForestLife):
    class Factory(ForestLife.Factory):
        def children(self):
            yield from Dinosaur.multiple(0, 5)
            yield from super().children()


class AncientJungleLife(JungleLife):
    class Factory(JungleLife.Factory):
        def children(self):
            yield from Dinosaur.multiple(0, 5)
            yield from super().children()


class AncientMountainLife(MountainLife):
    class Factory(MountainLife.Factory):
        def children(self):
            yield from Dinosaur.multiple(0, 3)
            yield from super().children()
