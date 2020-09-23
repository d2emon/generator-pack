from ..model import Model
from .matter import Gas, Matter, Molecule
from .minerals import Salt
from .water import Water


class Methane(Gas):
    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('C'),
            kwargs.get('H'),
        ]


class OrganicMolecule(Molecule):
    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('C'),
            kwargs.get('H'),
            kwargs.get('O'),
        ]


class Chitin(OrganicMolecule):
    default_name = 'chitin'

    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('C'),
            kwargs.get('H'),
            kwargs.get('N'),
            kwargs.get('O'),
        ]


class Proteins(OrganicMolecule):
    default_name = 'proteins'


class Lipids(OrganicMolecule):
    default_name = 'lipids'


class Glucids(OrganicMolecule):
    default_name = 'glucose'


class Alcohol(Glucids):
    default = 'alcohol'


class Polymers(Glucids):
    default = 'polymers'


class OrganicMatter(Matter):
    proteins = Matter.children_property(Proteins)
    lipids = Matter.children_property(Lipids)
    glucids = Matter.children_property(Glucids)
    water = Matter.children_property(Water)
    salt = Matter.children_property(Salt)
    polymers = Matter.children_property(Polymers)

    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('proteins'),
            kwargs.get('lipids'),
            kwargs.get('glucids'),
            kwargs.get('salt'),
        ]


class Polymeric(OrganicMatter):
    def __init__(self, **kwargs):
        super().__init__()
        self.contents = [
            kwargs.get('polymers'),
        ]


class Plastic(Polymeric):
    pass


class Rubber(Polymeric):
    pass


class Oil:
    def __init__(self, **kwargs):
        self.contents = [
            kwargs.get('lipids'),
        ]


# class Keratin(OrganicMatter):
#     class Factory(OrganicMatter.Factory):
#         def children(self):
#             yield Proteins


# class Sweat(OrganicMatter):
#     class Factory(OrganicMatter.Factory):
#         def children(self):
#             yield Water
#             yield Salt
#             yield Glucids
