from generated.materials.matter import Matter, Silica
from generated.materials.organics import Lipids
from .matter import MatterFactory
from .organics import OrganicMatterFactory


class RockFactory(MatterFactory):
    def children(self):
        yield Silica
        yield Matter.from_atoms('Al').probable(30)
        yield Matter.from_atoms('Fe').probable(20)
        yield Matter.from_atoms('K').probable(20)
        yield Matter.from_atoms('Na').probable(50)
        yield Matter.from_atoms('Ca').probable(50)


class DiamondFactory(RockFactory):
    def children(self):
        yield Matter.from_atoms('C')


class MagmaFactory(RockFactory):
    pass


class IronFactory(RockFactory):
    def children(self):
        yield Matter.from_atoms('Fe')


class SaltFactory(MatterFactory):
    def children(self):
        yield from Matter.from_atoms('Na', 'Cl')


class OilFactory(OrganicMatterFactory):
    def children(self):
        yield Lipids
