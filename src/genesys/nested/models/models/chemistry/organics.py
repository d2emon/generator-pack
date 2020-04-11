from .particles import Atom
from .elements import elements
from .matter import Molecule, Matter, Salt, Water


class OrganicMolecule(Molecule):
    class Factory(Molecule.Factory):
        class ChildrenFactory(Molecule.Factory.ChildrenFactory):
            def builders(self):
                yield from Molecule.from_atoms('C', 'H', 'O')


class Chitin(OrganicMolecule):
    default_name = 'chitin'

    class Factory(OrganicMolecule.Factory):
        class ChildrenFactory(OrganicMolecule.Factory.ChildrenFactory):
            def builders(self):
                yield from OrganicMolecule.from_atoms('C', 'H', 'N', 'O')


class Proteins(OrganicMolecule):
    default_name = 'proteins'


class Lipids(OrganicMolecule):
    default_name = 'lipids'


class Glucids(OrganicMolecule):
    default_name = 'glucose'


class Methane(Matter):
    class Factory(Matter.Factory):
        class ChildrenFactory(Matter.Factory.ChildrenFactory):
            def builders(self):
                yield from Matter.from_atoms('C', 'H')


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

    class Factory(Matter.Factory):
        class ChildrenFactory(Matter.Factory.ChildrenFactory):
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

            def builders(self):
                for component in self.components:
                    yield from next(Matter.Factory.BaseFactory(component))
                yield Salt.probable(30)


class Polymeric(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        class ChildrenFactory(OrganicMatter.Factory.ChildrenFactory):
            def builders(self):
                yield Polymers


class Plastic(Polymeric):
    pass


class Rubber(Polymeric):
    pass


class Oil(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        class ChildrenFactory(OrganicMatter.Factory.ChildrenFactory):
            def builders(self):
                yield Lipids


class Keratin(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        class ChildrenFactory(OrganicMatter.Factory.ChildrenFactory):
            def builders(self):
                yield Proteins


class Sweat(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        class ChildrenFactory(OrganicMatter.Factory.ChildrenFactory):
            def builders(self):
                yield Water
                yield Salt
                yield Glucids


class Ash(Matter):
    contents = Matter.children_property(OrganicMatter, Atom)

    class Factory(Matter.Factory):
        class ChildrenFactory(Matter.Factory.ChildrenFactory):
            def builders(self):
                yield OrganicMatter
                yield elements['C']
