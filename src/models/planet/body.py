"""
- PlanetLike
- Asteroid
- Moon
- TerraformedMoon
"""
from models.nested_model import TreeModel
# from models.mixins import TerraformedMixin
# from models.v5.life import Life
# from models.v5.terrain import Ocean, Sky
from .atmosphere import Atmosphere
from .plate import Plate
from .core import PlanetCore


class PlanetLike(TreeModel):
    atmosphere = TreeModel.child_property(Atmosphere)
    # biosphere = TreeModel.child_property(Life)
    core = TreeModel.child_property(PlanetCore)
    plates = TreeModel.children_property(Plate)
    # sky = TreeModel.child_property(Sky)
    # # land = TreeModel.children_property(Continent)
    # water = TreeModel.children_property(Ocean)
    # # visited = TreeModel.children_property(VisitorCity, VisitorInstallation)


class Asteroid(PlanetLike):
    pass


class Moon(PlanetLike):
    pass


# class TerraformedMoon(Moon, TerraformedMixin):
class TerraformedMoon(Moon):
    pass
