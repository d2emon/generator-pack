from genesys.model.model import Model
from genesys.model.mixins import TerraformedMixin
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