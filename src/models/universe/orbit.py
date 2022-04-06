"""
- Orbit
- PlanetOrbit
- AsteroidBelt
- ?Earth (Unused)
"""
from models.nested_model import NestedModel
from ..v5.life import Life
from .planet.body import PlanetLike


class Orbit(NestedModel):
    life = NestedModel.child_property(Life)
    planets = NestedModel.children_property(PlanetLike)


class PlanetOrbit(Orbit):
    planet = Orbit.child_property(PlanetLike)


class AsteroidBelt(Orbit):
    pass
