from factories.nested_factory import NestedFactory
from models.universe.orbit import AsteroidBelt
from models.planet.body import Asteroid
from .body import PlanetLikeFactory


# Asteroid Belt
# Earth
# Asteroid


class AsteroidBeltFactory(NestedFactory):
    default_model = AsteroidBelt

    def life(self):
        # yield AsteroidBeltLifeFactory()
        # galactic life,20%
        yield None

    def contents(self):
        yield AsteroidFactory.multiple(10, 30)


class EarthFactory(AsteroidBeltFactory):
    default_name = 'Earth'


class AsteroidFactory(PlanetLikeFactory):
    default_model = Asteroid

    def life(self):
        # yield AsteroidLifeFactory()
        # space animal,0.5%
        yield None

    def continents(self):
        # rock
        yield None

    def oceans(self):
        # ice,30%
        yield None


"""
new Thing("asteroid belt",[
    "galactic life,20%",
    "asteroid,10-30"
]);
new Thing("earth",[
    ".asteroid belt"
],"Earth");
new Thing("asteroid",[
    "space animal,0.5%",
    "rock",
    "ice,30%"
],"asteroid");
"""
