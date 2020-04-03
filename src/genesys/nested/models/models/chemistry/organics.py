from .particles import Atom
from .elements import elements
from .matter import Molecule, Matter, Salt, Water


class OrganicMolecule(Molecule):
    class ChildrenFactory(Molecule.ChildrenFactory):
        def children_classes(self):
            yield from Molecule.from_atoms('C', 'H', 'O')


class Chitin(OrganicMolecule):
    class NameFactory(OrganicMolecule.NameFactory):
        default = 'chitin'

    class ChildrenFactory(OrganicMolecule.ChildrenFactory):
        def children_classes(self):
            yield from Molecule.from_atoms('C', 'H', 'N', 'O')


class Proteins(OrganicMolecule):
    class NameFactory(OrganicMolecule.NameFactory):
        default = 'proteins'


class Lipids(OrganicMolecule):
    class NameFactory(OrganicMolecule.NameFactory):
        default = 'lipids'


class Glucids(OrganicMolecule):
    class NameFactory(OrganicMolecule.NameFactory):
        default = 'glucose'


class Ammonia(Matter):
    class ChildrenFactory(Matter.ChildrenFactory):
        def children_classes(self):
            yield from Matter.from_atoms('N', 'H')


class Methane(Matter):
    class ChildrenFactory(Matter.ChildrenFactory):
        def children_classes(self):
            yield from Matter.from_atoms('C', 'H')


class Alcohol(Glucids):
    class NameFactory(Glucids.NameFactory):
        default = 'alcohol'


class Polymers(Glucids):
    class NameFactory(Glucids.NameFactory):
        default = 'polymers'


class OrganicMatter(Matter):
    proteins = Matter.children_property(Proteins)
    lipids = Matter.children_property(Lipids)
    glucids = Matter.children_property(Glucids)
    water = Matter.children_property(Water)
    salt = Matter.children_property(Salt)
    polymers = Matter.children_property(Polymers)

    class ChildrenFactory(Matter.ChildrenFactory):
        components = [
            [
                Proteins,
                Lipids,
                Glucids,
            ],
            [
                Proteins,
                Lipids,
                Glucids,
                None,
            ],
        ]

        def children_classes(self):
            for component in self.components:
                yield from Matter.BaseFactory(component).next()
            yield Salt.probable(30)


class Polymeric(OrganicMatter):
    class ChildrenFactory(OrganicMatter.ChildrenFactory):
        def children_classes(self):
            yield Polymers


class Plastic(Polymeric):
    pass


class Rubber(Polymeric):
    pass


class Oil(OrganicMatter):
    class ChildrenFactory(Matter.ChildrenFactory):
        def children_classes(self):
            yield Lipids


class Keratin(OrganicMatter):
    class ChildrenFactory(OrganicMatter.ChildrenFactory):
        def children_classes(self):
            yield Proteins


class Sweat(OrganicMatter):
    class ChildrenFactory(OrganicMatter.ChildrenFactory):
        def children_classes(self):
            yield Water
            yield Salt
            yield Glucids


class Ash(Matter):
    contents = Matter.children_property(OrganicMatter, Atom)

    class ChildrenFactory(Matter.ChildrenFactory):
        def children_classes(self):
            yield OrganicMatter
            yield elements['C']
