from models.nested_model import NestedModel
from models.v5.life import Life
from models.planet.body import PlanetLike


class Orbit(NestedModel):
    life = NestedModel.child_property(Life)
    planets = NestedModel.children_property(PlanetLike)


class AsteroidBelt(Orbit):
    pass
