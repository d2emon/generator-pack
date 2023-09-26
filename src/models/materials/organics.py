from .elements import Molecule
from .matter import Matter


# Molecule


class OrganicMolecule(Molecule):
    pass


class Proteins(OrganicMolecule):
    pass


class Lipids(OrganicMolecule):
    pass


class Glucids(OrganicMolecule):
    default_name = 'glucose'


class Alcohol(Glucids):
    pass


class Polymers(Glucids):
    pass


# Matter


class OrganicMatter(Matter):
    pass


class Oil(OrganicMatter):
    state = OrganicMatter.LIQUID


class Chitin(OrganicMatter):
    state = OrganicMatter.SOLID


class Polymeric(OrganicMatter):
    pass


class Plastic(Polymeric):
    pass


class Rubber(Polymeric):
    pass


class Keratin(OrganicMatter):
    # TODO: Refactor it
    pass


class Sweat(OrganicMatter):
    # TODO: Refactor it
    pass
