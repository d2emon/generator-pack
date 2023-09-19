from models.v5 import materials
from factories.thing.nested_factory import NestedFactory as Factory
from .matter import MoleculeFactory


class AmmoniaMoleculeFactory(MoleculeFactory):
    contents = 'N', 'H'


class SilicaFactory(MoleculeFactory):
    model = materials.Silica
    contents = 'Si', 'O'


class SaltFactory(MoleculeFactory):
    model = materials.Salt
    contents = 'Na', 'Cl'


class AmmoniaFactory(Factory):
    model = materials.Ammonia

    def children(self):
        yield AmmoniaMoleculeFactory()


class RockFactory(Factory):
    model = materials.Rock

    def children(self):
        yield SilicaFactory.one()
        yield MoleculeFactory.from_elements('Al').probable(30)
        yield MoleculeFactory.from_elements('Fe').probable(20)
        yield MoleculeFactory.from_elements('K').probable(20)
        yield MoleculeFactory.from_elements('Na').probable(50)
        yield MoleculeFactory.from_elements('Ca').probable(50)


class CarbonFactory(RockFactory):
    model = materials.Carbon

    def children(self):
        yield MoleculeFactory.from_elements('C')


class DiamondFactory(CarbonFactory):
    model = materials.Diamond


class MagmaFactory(RockFactory):
    model = materials.Magma


class IronFactory(RockFactory):
    # TODO: Refactor it
    default_model = materials.Iron

    def children(self):
        yield MoleculeFactory.from_elements('Fe')
