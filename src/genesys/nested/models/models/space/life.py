from genesys.nested.models.models.unknown import Ghost
# from ..biology import Crustacean, GalacticLife, SpaceMonster
from ..biology import Life


class BlackHoleLife(Life):
    class Factory(Life.Factory):
        def children(self):
            # yield Crustacean.probable(0.2)
            yield None


class GalacticLife(Life):
    class Factory(Life.Factory):
        probability = 100

        def children(self):
            if not self.check_probability(self.probability):
                return
            # yield SpaceMonster.probable(1)
            # yield from SpaceAnimal.multiple(1, 12)
            yield None


class GalaxyCenterLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        probability = 0


class GalaxyArmLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        probability = 5


class NebulaLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        probability = 15


class StarLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        def children(self):
            yield Ghost.probable(0.1)
            # yield SpaceMonster.probable(0.2)


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
