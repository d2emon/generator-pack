"""
Cell stuff
"""
from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from utils.nested import select_item
from genesys.nested.materials.organics import GlucidsFactory, LipidsFactory, OrganicFactory, OrganicMoleculeFactory, ProteinsFactory


class NucleotideFactory(NestedFactory):
    def name_factory(self, data, *args, **kwargs):
        return select_item(*data.nucleotide)

    def children(self):
        yield OrganicMoleculeFactory.one()


class GeneticCodeFactory(NestedFactory):
    def children(self):
        yield NucleotideFactory.multiple(20, 50)


class DNAFactory(OrganicMoleculeFactory):
    model = life.DNA
    contents = 'H', 'O', 'N', 'C', 'P'

    def children(self):
        yield GeneticCodeFactory()
        yield from super().children()


class NucleusFactory(OrganicFactory):
    model = life.Nucleus

    def children(self):
        yield DNAFactory.one()
        yield ProteinsFactory.one()


class CytoplasmFactory(OrganicFactory):
    model = life.Cytoplasm

    def children(self):
        yield GlucidsFactory.one()
        yield LipidsFactory.one()


class CellFactory(NestedFactory):
    model = life.Cell

    def children(self):
        yield NucleusFactory.one()
        yield CytoplasmFactory.one()


FACTORIES = {
    'cell': CellFactory,
    'nucleus': NucleusFactory,
    'cytoplasm': CytoplasmFactory,
    'dna': DNAFactory,
    'genetic code': GeneticCodeFactory,
    'nucleotide': NucleotideFactory,
}
