from genesys.nested.factories.nested_factory import NestedFactory
from models.materials import gases
from .elements import MoleculeFactory


class AmmoniaMoleculeFactory(MoleculeFactory):
    contents = 'N', 'H'


class MethaneMoleculeFactory(MoleculeFactory):
    contents = 'C', 'H'


# Gases


class AmmoniaFactory(NestedFactory):
    model = gases.Ammonia

    def children(self):
        yield AmmoniaMoleculeFactory.one()


class MethaneFactory(NestedFactory):
    model = gases.Methane

    def children(self):
        yield MethaneMoleculeFactory.one()
