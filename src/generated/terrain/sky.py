"""
- Meteorite
- Ozone
- Cloud
- Precipitation
- Sky
    - TerraformedSky
    - FutureSky
"""
from genesys.model.model import Model
from ..materials import Gas, Steam, Water


class Meteorite(Model):
    pass


class Ozone(Gas):
    pass


class Cloud(Steam):
    pass


class Precipitation(Water):
    pass


class Sky(Model):
    # Habitat
    # transport = Model.children_property(VisitorShip)
    meteorites = Model.children_property(Meteorite)
    precipitations = Model.children_property(Precipitation)
    clouds = Model.children_property(Cloud)
