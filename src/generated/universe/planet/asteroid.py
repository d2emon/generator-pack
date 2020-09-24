from genesys.model.model import Model
from .planet_like import Orbit, PlanetLike, Plate
from generated.universe.space.life import AsteroidLife, AsteroidBeltLife
from generated.materials.chemistry import Ice
from generated.materials import Rock


class AsteroidPlate(Plate):
    class Factory(Plate.Factory):
        def children(self):
            yield Rock
            yield Ice.probable(30)


class Asteroid(PlanetLike):
    class Factory(PlanetLike.Factory):
        @classmethod
        def biosphere(cls):
            yield AsteroidLife

        @classmethod
        def plates(cls):
            yield AsteroidPlate


class AsteroidBelt(Orbit):
    asteroids = Orbit.children_property(Asteroid)

    class Factory(Orbit.Factory):
        @classmethod
        def life(cls):
            yield AsteroidBeltLife

        @classmethod
        def asteroids(cls):
            yield from Asteroid.multiple(10, 30)

        def children(self):
            yield from self.life()
            yield from self.asteroids()


class Earth(AsteroidBelt):
    default_name = 'Earth'
