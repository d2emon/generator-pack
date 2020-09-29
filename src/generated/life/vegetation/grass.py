"""
- GrassBlade
- Grass
"""
from genesys.model.model import Model
from ...mind import Thoughts
from .twig import Twig


class GrassBlade(Twig):
    thoughts = Model.child_property(Thoughts)


class Grass(Model):
    grass_blades = Model.children_property(GrassBlade)
