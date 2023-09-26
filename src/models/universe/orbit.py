"""
- Orbit
- PlanetOrbit
- AsteroidBelt
- ?Earth (Unused)
"""
from models.nested_model import TreeModel
# from ..v5.life import Life
from ..planet.body import PlanetLike


class Orbit(TreeModel):
    # life = TreeModel.child_property(Life)
    planets = TreeModel.children_property(PlanetLike)


class PlanetOrbit(Orbit):
    planet = Orbit.child_property(PlanetLike)


class AsteroidBelt(Orbit):
    pass
