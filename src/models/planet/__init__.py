# from models.mixins import TerraformedMixin
from .body import PlanetLike, Moon


class Planet(PlanetLike):
    default_name = 'telluric planet'

    moons = PlanetLike.children_property(Moon)



class GasGiant(Planet):
    pass
