"""
Single-celled Organisms

- Bacteria
- BacteriaBody
"""
from models.nested_model import Model
from ..cell import Cell
from ...mind import Psyche


class BacteriaBody(Cell):
    default_name = 'body'


class Bacteria(Model):
    body = Model.child_property(BacteriaBody)
    psyche = Model.child_property(Psyche)
