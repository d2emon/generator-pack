"""
- GrassBlade
- Grass
"""
from genesys.model.model import Model
from ...mind import Psyche
from .twig import Twig


class GrassBlade(Twig):
    psyche = Twig.child_property(Psyche)


class Grass(Model):
    grass_blades = Model.children_property(GrassBlade)
