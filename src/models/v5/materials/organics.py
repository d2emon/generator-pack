"""
- OrganicMolecule
- Methane
- Chitin
- Proteins
- Lipids
- Glucids
- Alcohol
- Polymers
- OrganicMatter
- Oil
- Polymeric
- Plastic
- Rubber
- Keratin
- Sweat
"""
from .matter import Molecule, Matter
from .minerals import Salt
from .water import Water


class OrganicMolecule(Molecule):
    pass


class Methane(OrganicMolecule):
    pass


class Chitin(OrganicMolecule):
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


class OrganicMatter(Matter):
    proteins = Matter.children_property(Proteins)
    lipids = Matter.children_property(Lipids)
    glucids = Matter.children_property(Glucids)
    salt = Matter.children_property(Salt)
    polymers = Matter.children_property(Polymers)
    water = Matter.children_property(Water)
    molecules = Matter.children_property(Molecule)


class Oil(OrganicMatter):
    pass


class Polymeric(OrganicMatter):
    pass


class Plastic(Polymeric):
    pass


class Rubber(Polymeric):
    pass


class Keratin(OrganicMatter):
    pass


class Sweat(OrganicMatter):
    pass
