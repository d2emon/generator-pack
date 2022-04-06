"""
- Planet (Unused)
- BarrenPlanet
- TelluricPlanet
- GasGiant
"""
# from models.v4.mixins import TerraformedMixin
from .body import PlanetLike, Moon


class Planet(PlanetLike):
    default_name = 'telluric planet'

    moons = PlanetLike.children_property(Moon)


class BarrenPlanet(Planet):
    pass


# class TelluricPlanet(Planet, TerraformedMixin):
class TelluricPlanet(Planet):
    pass


class GasGiant(Planet):
    pass
