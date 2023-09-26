"""
- OrganicMolecule
- Methane
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
from models.materials.elements import Molecule
from models.materials.matter import Matter
from models.materials.water import Water
from models.minerals import Salt


class OrganicMolecule(Molecule):
    # TODO: Refactor it
    pass


class Proteins(OrganicMolecule):
    # TODO: Refactor it
    pass


class Lipids(OrganicMolecule):
    # TODO: Refactor it
    pass


class Glucids(OrganicMolecule):
    # TODO: Refactor it
    default_name = 'glucose'


class Alcohol(Glucids):
    pass


class Polymers(Glucids):
    pass


class OrganicMatter(Matter):
    # TODO: Refactor it
    proteins = Matter.children_property(Proteins)
    lipids = Matter.children_property(Lipids)
    glucids = Matter.children_property(Glucids)
    salt = Matter.children_property(Salt)
    polymers = Matter.children_property(Polymers)
    water = Matter.children_property(Water)
    molecules = Matter.children_property(Molecule)


class Chitin(OrganicMatter):
    pass


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
