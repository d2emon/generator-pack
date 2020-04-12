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
        def biosphere(self):
            # yield SpaceAnimal.probable(0.5)
            yield None

        def plates(self):
            yield AsteroidPlate


class AsteroidBelt(Orbit, EncounteredMixin):
    asteroids = Orbit.children_property(Asteroid)

    class Factory(Orbit.Factory):
        def children(self):
            # yield GalacticLife.probable(20)
            yield from Asteroid.multiple(10, 30)


class Earth(AsteroidBelt):
    default_name = 'Earth'
