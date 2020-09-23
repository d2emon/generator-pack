from generated.materials.elements import elements
from generated.materials.matter import Matter
from generated.materials.organics import OrganicMatter
from .matter import MatterFactory
from ..factory import Factory


class FireFactory(Factory):
    def children(self):
        yield elements['C']
        yield elements['O']


class Factory(MatterFactory):
    def children(self):
        yield OrganicMatter
        yield Matter.from_atoms('C')
