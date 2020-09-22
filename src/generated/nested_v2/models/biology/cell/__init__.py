"""
Cell stuff

- Cell
- Nucleus
- Cytoplasm
- DNA
- Genetic Code
- Nucleotide
"""
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from generated.chemistry import elements, Proteins, Lipids, Glucids, OrganicMolecule, OrganicMatter, Atom
from genesys.nested.data import lookups


class Nucleotide(Model):
    molecule = Model.child_property(OrganicMolecule)

    class Factory(ThingBuilder):
        class DataProvider:
            nucleotide = lookups.nucleotides

        class BaseFactory(ThingBuilder.BaseFactory):
            data = property(lambda self: self.provider.nucleotide)

        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield OrganicMolecule


class GeneticCode(Model):
    nucleotides = Model.child_property(Nucleotide)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Nucleotide.multiple(20, 50)


class DNA(Model):
    genetic_code = Model.child_property(GeneticCode)
    elements = Model.children_property(Atom)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield GeneticCode
                yield elements['H']
                yield elements['O']
                yield elements['N']
                yield elements['C']
                yield elements['P']


class Nucleus(Model):
    dna = Model.child_property(DNA)
    proteins = Model.child_property(Proteins)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield DNA
                yield Proteins


class Cytoplasm(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        class ChildrenFactory(OrganicMatter.Factory.ChildrenFactory):
            def builders(self):
                yield Lipids
                yield Glucids


class Cell(Model):
    nucleus = Model.child_property(Nucleus)
    cytoplasm = Model.child_property(Cytoplasm)

    default_name = 'cells'

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Nucleus
                yield Cytoplasm
