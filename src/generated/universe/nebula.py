"""
- InterstellarCloud
- Nebula
"""
from genesys.model.model import Model
from ..materials import Gas
from .star import StarSystem


class InterstellarCloud(Gas):
    pass


class Nebula(Model):
    # Habitat
    stars = Model.children_property(StarSystem)
    clouds = Model.children_property(InterstellarCloud)
