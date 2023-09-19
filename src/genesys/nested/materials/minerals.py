from models.v5 import materials
from factories.thing.nested_factory import NestedFactory as Factory
from .elements import MoleculeFactory


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
        yield MoleculeFactory.element_factory('Al').probable(30)
        yield MoleculeFactory.element_factory('Fe').probable(20)
        yield MoleculeFactory.element_factory('K').probable(20)
        yield MoleculeFactory.element_factory('Na').probable(50)
        yield MoleculeFactory.element_factory('Ca').probable(50)


class CarbonFactory(RockFactory):
    model = materials.Carbon

    def children(self):
        yield MoleculeFactory.element_factory('C')


class DiamondFactory(CarbonFactory):
    model = materials.Diamond


class MagmaFactory(RockFactory):
    model = materials.Magma
