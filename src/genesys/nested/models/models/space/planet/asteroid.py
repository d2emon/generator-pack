from genesys.nested.models.mixins import EncounteredMixin
from .planet_like import Orbit, PlanetLike, Plate
# from ...biology import GalacticLife, SpaceAnimal
from ...chemistry import Ice, Rock


class AsteroidPlate(Plate):
    class Factory(Plate.Factory):
        def children(self):
            yield Rock
            yield Ice.probable(30)


class Asteroid(PlanetLike):
    class Factory(PlanetLike.Factory):
        @classmethod
        def biosphere(cls):
            yield None

        @classmethod
        def plates(cls):
            yield AsteroidPlate


class AsteroidBelt(Orbit, EncounteredMixin):
    asteroids = Orbit.children_property(Asteroid)

    class Factory(Orbit.Factory):
        @classmethod
        def life(cls):
            yield None

        @classmethod
        def asteroids(cls):
            yield from Asteroid.multiple(10, 30)

        def children(self):
            yield from self.life()
            yield from self.asteroids()


class Earth(AsteroidBelt):
    default_name = 'Earth'
