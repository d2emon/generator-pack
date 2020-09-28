"""
- BoneCell
- Bones
- Bone
- MuscleCell
- Muscles
- Fat
"""
from genesys.model.model import Model
from ..cell import Cell
from ...materials import Molecule, OrganicMatter


class BoneCell(Cell):
    default_name = 'bone cells'


class Bones(Model):
    cells = Model.child_property(Cell)
    elements = Model.children_property(Molecule)


class Bone(Bones):
    pass


class MuscleCell(Cell):
    default_name = 'muscle cells'


class Muscles(Model):
    cells = Model.child_property(Cell)


class Fat(OrganicMatter):
    pass
