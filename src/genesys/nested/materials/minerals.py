from genesys.nested.factories.nested_factory import NestedFactory
from models import minerals
from .molecules import MoleculeFactory, SilicaFactory


class RockFactory(NestedFactory):
    model = minerals.Rock

    def children(self):
        yield SilicaFactory.one()
        yield MoleculeFactory.element_factory('Al').probable(30)
        yield MoleculeFactory.element_factory('Fe').probable(20)
        yield MoleculeFactory.element_factory('K').probable(20)
        yield MoleculeFactory.element_factory('Na').probable(50)
        yield MoleculeFactory.element_factory('Ca').probable(50)


class CarbonFactory(RockFactory):
    model = minerals.Carbon

    def children(self):
        yield MoleculeFactory.element_factory('C')


class DiamondFactory(CarbonFactory):
    model = minerals.Diamond


class MagmaFactory(RockFactory):
    model = minerals.Magma
