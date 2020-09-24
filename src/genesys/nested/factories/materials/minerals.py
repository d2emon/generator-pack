from generated.materials import Salt, Silica, Rock, Diamond, Magma, Carbon, Iron
from ..factory import Factory
from .matter import MoleculeFactory


class SilicaFactory(MoleculeFactory):
    default_model = Silica

    def children(self):
        yield from self.elements('Si', 'O')


class SaltFactory(MoleculeFactory):
    default_model = Salt

    def children(self):
        yield from self.elements('Na', 'Cl')


class RockFactory(Factory):
    default_model = Rock

    def children(self):
        yield SilicaFactory
        yield MoleculeFactory.from_elements('Al').probable(30)
        yield MoleculeFactory.from_elements('Fe').probable(20)
        yield MoleculeFactory.from_elements('K').probable(20)
        yield MoleculeFactory.from_elements('Na').probable(50)
        yield MoleculeFactory.from_elements('Ca').probable(50)


class DiamondFactory(RockFactory):
    default_model = Diamond

    def children(self):
        yield MoleculeFactory.from_elements('C')


class MagmaFactory(RockFactory):
    default_model = Magma


class CarbonFactory(RockFactory):
    default_model = Carbon

    def children(self):
        yield MoleculeFactory.from_elements('C')


class IronFactory(RockFactory):
    default_model = Iron

    def children(self):
        yield MoleculeFactory.from_elements('Fe')
