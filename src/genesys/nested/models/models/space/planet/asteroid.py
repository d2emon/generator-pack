from genesys.nested.models.models.unknown import SpaceAnimal, GalacticLife
from genesys.nested.models.mixins import EncounteredMixin
from .planet_like import PlanetLike, Orbit
from genesys.nested.models.models.chemistry import Rock, Ice


class Asteroid(PlanetLike):
    class ChildrenFactory(PlanetLike.ChildrenFactory):
        def children_classes(self):
            yield SpaceAnimal.probable(0.5)
            yield Rock
            yield Ice.probable(30)


class AsteroidBelt(Orbit, EncounteredMixin):
    asteroids = Orbit.children_property(Asteroid)

    class ChildrenFactory(Orbit.ChildrenFactory):
        def children_classes(self):
            yield GalacticLife.probable(20)
            yield from Asteroid.multiple(10, 30)


class Earth(AsteroidBelt):
    class NameFactory(AsteroidBelt.NameFactory):
        default = 'Earth'
