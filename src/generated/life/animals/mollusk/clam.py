"""
- Clam
- Clam Body
- ClamShell
"""
from models.v4.model import Model
from ....materials import Molecule
from ..animal import Animal, AnimalBody


class ClamShell(Model):
    elements = Model.children_property(Molecule)


class ClamBody(AnimalBody):
    shells = Model.children_property(ClamShell)


class Clam(Animal):
    pass
