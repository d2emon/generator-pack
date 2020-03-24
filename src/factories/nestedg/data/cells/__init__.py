"""
Cell stuff
"""
from nestedg.model import Model
from nestedg.data import materials
from nestedg.data.materials import elements


class Nucleotide(NestedItem):
    nucleotides = ['A', 'T', 'G', 'C']

    @classmethod
    def get_children(cls):
        yield materials.Molecule

    @classmethod
    def get_name(cls):
        return cls.choice(cls.nucleotides)


class GeneticCode(NestedItem):
    @classmethod
    def get_children(cls):
        yield Nucleotide.multiple(20, 50)


class DNA(NestedItem):
    @classmethod
    def get_children(cls):
        yield GeneticCode
        yield elements.Hydrogen
        yield elements.Oxygen
        yield elements.Nitrogen
        yield elements.Carbon
        yield elements.Phosphorus


class Cytoplasm(NestedItem):
    @classmethod
    def get_children(cls):
        yield materials.Lipids
        yield materials.Glucids


class Nucleus(NestedItem):
    @classmethod
    def get_children(cls):
        yield DNA
        yield materials.Proteins


class Cell(NestedItem):
    @classmethod
    def get_children(cls):
        yield Nucleus
        yield Cytoplasm

    @classmethod
    def get_name(cls):
        return 'cells'
