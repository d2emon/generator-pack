"""
- Planet (Unused)
- BarrenPlanet
- TelluricPlanet
- GasGiant
"""
from models.v5.model import Model
from models.v4.mixins import TerraformedMixin
from .body import PlanetLike, Moon


class Planet(PlanetLike):
    default_name = 'telluric planet'

    moons = Model.children_property(Moon)


class BarrenPlanet(Planet):
    pass


class TelluricPlanet(Planet, TerraformedMixin):
    pass


class GasGiant(Planet):
    pass
