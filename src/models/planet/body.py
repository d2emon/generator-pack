"""
- PlanetLike
- Asteroid
- Moon
- TerraformedMoon
"""
from models.nested_model import NestedModel
# from models.mixins import TerraformedMixin
# from models.v5.life import Life
# from models.v5.terrain import Ocean, Sky
from .atmosphere import Atmosphere
from .plate import Plate
from .core import PlanetCore


class PlanetLike(NestedModel):
    core = NestedModel.child_property(PlanetCore)
    plates = NestedModel.children_property(Plate)
    # # land = NestedModel.children_property(Continent)
    # # water = NestedModel.children_property(Ocean)
    # # visited = NestedModel.children_property(VisitorCity, VisitorInstallation)
    # life
    # # biosphere = NestedModel.child_property(Life)
    # sky = NestedModel.child_property(Sky)
    atmosphere = NestedModel.child_property(Atmosphere)


class Asteroid(PlanetLike):
    pass


class Moon(PlanetLike):
    pass


# class TerraformedMoon(Moon, TerraformedMixin):
class TerraformedMoon(Moon):
    pass
