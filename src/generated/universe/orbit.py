"""
- Orbit
- PlanetOrbit
- AsteroidBelt
- ?Earth (Unused)
"""
from genesys.model.model import Model
from ..life import Life
from .planet.body import PlanetLike


class Orbit(Model):
    life = Model.child_property(Life)
    planets = Model.children_property(PlanetLike)


class PlanetOrbit(Orbit):
    planet = Model.child_property(PlanetLike)


class AsteroidBelt(Orbit):
    pass
