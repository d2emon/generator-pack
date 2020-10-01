"""
Single-celled Organisms

- Bacteria
- BacteriaBody
"""
from ..animals.animal import Animal
from ..cell import Cell


class BacteriaBody(Cell):
    default_name = 'body'


class Bacteria(Animal):
    body = Animal.child_property(BacteriaBody)
