"""
- PlanetLike
- Asteroid
- Moon
- TerraformedMoon
"""
from genesys.model.model import Model
from genesys.model.mixins import TerraformedMixin
from ...life import Life
from ...terrain import Ocean, Sky
from ..atmosphere import Atmosphere
from .plate import Plate
from .core import PlanetCore


class PlanetLike(Model):
    atmosphere = Model.child_property(Atmosphere)
    biosphere = Model.child_property(Life)
    core = Model.child_property(PlanetCore)
    plates = Model.children_property(Plate)
    sky = Model.children_property(Sky)
    # land = Model.children_property(Continent)
    water = Model.children_property(Ocean)
    # visited = Model.children_property(VisitorCity, VisitorInstallation)


class Asteroid(PlanetLike):
    pass


class Moon(PlanetLike):
    pass


class TerraformedMoon(Moon, TerraformedMixin):
    pass
