"""
- Nest
- Bark
- TreeTrunk
- Leaf
- Leaves
- Branch
- Branches
- Fruits
- Pollen
- Flowers
- Tree
- Trees
- Humus
"""
from genesys.model.model import Model
from ...materials import OrganicMatter
from ...mind import Thoughts
from .twig import Twig


class Nest(Model):
    # bird = Model.child_property(Bird)
    # eggs = Model.children_property(EggShell, BirdEgg)
    twigs = Model.children_property(Twig)


class Bark(Model):
    # wood = Model.child_property(Wood)
    pass


class TreeTrunk(Model):
    bark = Model.child_property(Bark)
    # wood = Model.child_property(Wood)


class Leaf(Twig):
    pass


class Leaves(Model):
    leaves = Model.children_property(Leaf)


class Branch(Twig):
    leaves = Model.children_property(Leaf)


class Branches(Model):
    branches = Model.children_property(Branch)


class Fruits(Twig):
    # sugar = Model.child_property(Sugar)
    pass


class Pollen(Twig):
    # sugar = Model.child_property(Sugar)
    pass


class Flowers(Twig):
    pollen = Model.child_property(Pollen)


class Tree(Model):
    thoughts = Model.child_property(Thoughts)
    trunk = Model.child_property(TreeTrunk)
    branches = Model.child_property(Branches)
    leaves = Model.child_property(Leaves)
    nests = Model.children_property(Nest)
    fruits = Model.child_property(Fruits)
    flowers = Model.child_property(Flowers)


class Trees(Model):
    trees = Model.children_property(Tree)


class Humus(Model):
    # insects = Model.children_property(Insect)
    # worms = Model.children_property(Worm)
    twigs = Model.children_property(Twig)
    leaves = Model.children_property(Leaf)
    organic = Model.child_property(OrganicMatter)
    # dirt = Model.child_property(Dirt)
