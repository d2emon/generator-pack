"""
Cell stuff
"""
from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from utils.nested import select_item
from ..materials import OrganicMoleculeFactory, LipidsFactory, GlucidsFactory, ProteinsFactory


class NucleotideFactory(Factory):
    names = ["A", "T", "G", "C"]

    def generate_name(self):
        return select_item(*self.names)

    def children(self):
        yield OrganicMoleculeFactory()


class GeneticCodeFactory(Factory):
    def children(self):
        yield NucleotideFactory().multiple(20, 50)


class DNAFactory(OrganicMoleculeFactory):
    model = life.DNA
    contents = 'H', 'O', 'N', 'C', 'P'

    def children(self):
        yield GeneticCodeFactory()
        yield from super().children()


class CytoplasmFactory(Factory):
    default_model = life.Cytoplasm

    def children(self):
        yield LipidsFactory()
        yield GlucidsFactory()


class NucleusFactory(Factory):
    default_model = life.Nucleus

    def children(self):
        yield DNAFactory()
        yield ProteinsFactory()


class CellFactory(Factory):
    default_model = life.Cell

    def children(self):
        yield NucleusFactory()
        yield CytoplasmFactory()


FACTORIES = {
    'cell': CellFactory(),
    'nucleus': NucleusFactory(),
    'cytoplasm': CytoplasmFactory(),
    'dna': DNAFactory(),
    'genetic code': GeneticCodeFactory(),
    'nucleotide': NucleotideFactory(),
}
