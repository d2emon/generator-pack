from genesys.nested.factories.nested_factory import NestedFactory
from models import minerals
from .molecules import MoleculeFactory


class AmmoniaMoleculeFactory(MoleculeFactory):
    contents = 'N', 'H'


class MethaneMoleculeFactory(MoleculeFactory):
    contents = 'C', 'H'


# Gases


class AmmoniaFactory(NestedFactory):
    model = minerals.Ammonia

    def children(self):
        yield AmmoniaMoleculeFactory.one()


class MethaneFactory(NestedFactory):
    model = minerals.Methane

    def children(self):
        yield MethaneMoleculeFactory.one()
