"""
Cell stuff

- Cell
- Nucleus
- Cytoplasm
- DNA
- Genetic Code
- Nucleotide
"""
from models.v4.model import Model
from ..materials import OrganicMolecule, OrganicMatter


class Nucleotide(Model):
    molecule = Model.child_property(OrganicMolecule)


class GeneticCode(Model):
    nucleotides = Model.child_property(Nucleotide)


class DNA(OrganicMolecule):
    default_name = 'DNA'
    genetic_code = Model.child_property(GeneticCode)


class Nucleus(OrganicMatter):
    dna = Model.child_property(DNA)


class Cytoplasm(OrganicMatter):
    pass


class Cell(Model):
    nucleus = Model.child_property(Nucleus)
    cytoplasm = Model.child_property(Cytoplasm)

    default_name = 'cells'
