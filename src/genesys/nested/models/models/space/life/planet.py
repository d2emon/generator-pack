from genesys.nested.models.models.unknown import Ghost
from .space import GalacticLife


class PlanetCoreLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        def children(self):
            # yield SpaceMonster.probable(0.5)
            yield None


class GasGiantLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        probability = 10


class BarrenPlanetLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        probability = 10


class VisitorPlanetLife(GalacticLife):
    pass


class MoonLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        def children(self):
            yield Ghost.probable(0.1)


class AsteroidLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        def children(self):
            # yield SpaceAnimal.probable(0.5)
            yield None


class AsteroidBeltLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        probability = 20
