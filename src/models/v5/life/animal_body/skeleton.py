"""
- BoneCell
- Bones
- Bone
- MuscleCell
- Muscles
- Fat
- Skeleton
"""
from models.nested_model import Model
from ...materials import Molecule, OrganicMatter
from ..cell import Cell


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


class Skeleton(Model):
    bones = Model.child_property(Bones)
