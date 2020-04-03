"""
Cell stuff

- Cell
- Nucleus
- Cytoplasm
- DNA
- Genetic Code
- Nucleotide
"""
from genesys.nested.models import Model
from ...chemistry import elements, Proteins, Lipids, Glucids, OrganicMolecule
from genesys.nested.data import lookups


class Nucleotide(Model):
    class BaseFactory(Model.BaseFactory):
        default = lookups.nucleotides

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield OrganicMolecule


class GeneticCode(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Nucleotide.multiple(20, 50)


class DNA(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield GeneticCode
            yield elements['H']
            yield elements['O']
            yield elements['N']
            yield elements['C']
            yield elements['P']


class Nucleus(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield DNA
            yield Proteins


class Cytoplasm(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Lipids
            yield Glucids


class Cell(Model):
    class NameFactory(Model.NameFactory):
        default = 'cells'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Nucleus
            yield Cytoplasm
