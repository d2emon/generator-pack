from factories.thing.nested_factory import NestedFactory as Factory
from models.v5 import materials
from .molecules import MoleculeFactory


class AmmoniaMoleculeFactory(MoleculeFactory):
    contents = 'N', 'H'


class MethaneMoleculeFactory(MoleculeFactory):
    model = materials.Methane
    contents = 'C', 'H'


# Gases


class AmmoniaFactory(Factory):
    model = materials.Ammonia

    def children(self):
        yield AmmoniaMoleculeFactory.one()


class MethaneFactory(Factory):
    model = materials.Methane

    def children(self):
        yield MethaneMoleculeFactory.one()
