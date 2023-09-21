from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import materials
from .molecules import MoleculeFactory


class AmmoniaMoleculeFactory(MoleculeFactory):
    contents = 'N', 'H'


class MethaneMoleculeFactory(MoleculeFactory):
    model = materials.Methane
    contents = 'C', 'H'


# Gases


class AmmoniaFactory(NestedFactory):
    model = materials.Ammonia

    def children(self):
        yield AmmoniaMoleculeFactory.one()


class MethaneFactory(NestedFactory):
    model = materials.Methane

    def children(self):
        yield MethaneMoleculeFactory.one()
