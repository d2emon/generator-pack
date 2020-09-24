from generated import materials
from ..factory import Factory
from .matter import MoleculeFactory


class AmmoniaFactory(Factory):
    default_model = materials.Ammonia

    def children(self):
        yield MoleculeFactory.from_elements('N', 'H')


class SilicaFactory(MoleculeFactory):
    default_model = materials.Silica

    def children(self):
        yield from self.elements('Si', 'O')


class SaltFactory(MoleculeFactory):
    default_model = materials.Salt

    def children(self):
        yield from self.elements('Na', 'Cl')


class RockFactory(Factory):
    default_model = materials.Rock

    def children(self):
        yield SilicaFactory
        yield MoleculeFactory.from_elements('Al').probable(30)
        yield MoleculeFactory.from_elements('Fe').probable(20)
        yield MoleculeFactory.from_elements('K').probable(20)
        yield MoleculeFactory.from_elements('Na').probable(50)
        yield MoleculeFactory.from_elements('Ca').probable(50)


class CarbonFactory(RockFactory):
    default_model = materials.Carbon

    def children(self):
        yield MoleculeFactory.from_elements('C')


class DiamondFactory(CarbonFactory):
    default_model = materials.Diamond


class MagmaFactory(RockFactory):
    default_model = materials.Magma


class IronFactory(RockFactory):
    default_model = materials.Iron

    def children(self):
        yield MoleculeFactory.from_elements('Fe')
