"""
- PlanetLike
- Asteroid
- Moon
- TerraformedMoon
"""
from models.nested_model import NestedModel
from models.v4.mixins import TerraformedMixin
from models.v5.life import Life
from models.v5.terrain import Ocean, Sky
from ..atmosphere import Atmosphere
from .plate import Plate
from .core import PlanetCore


class PlanetLike(NestedModel):
    atmosphere = NestedModel.child_property(Atmosphere)
    biosphere = NestedModel.child_property(Life)
    core = NestedModel.child_property(PlanetCore)
    plates = NestedModel.children_property(Plate)
    sky = NestedModel.child_property(Sky)
    # land = NestedModel.children_property(Continent)
    water = NestedModel.children_property(Ocean)
    # visited = NestedModel.children_property(VisitorCity, VisitorInstallation)


class Asteroid(PlanetLike):
    pass


class Moon(PlanetLike):
    pass


class TerraformedMoon(Moon, TerraformedMixin):
    pass
