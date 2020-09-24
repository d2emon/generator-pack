from generated.materials import Fire, Ash
from ..factory import Factory
from .matter import MoleculeFactory
from .minerals import CarbonFactory
from .organics import OrganicMatterFactory


class FireFactory(Factory):
    default_model = Fire

    def children(self):
        yield from MoleculeFactory.elements('C', 'O')


class AshFactory(Factory):
    default_model = Ash

    def children(self):
        yield OrganicMatterFactory()
        yield CarbonFactory()
