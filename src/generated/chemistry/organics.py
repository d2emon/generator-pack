from genesys.nested.factories.thing_builder import ListFactory
from .matter import Gas, Matter, Molecule, Salt
from .water import Water


class Methane(Gas):
    class Factory(Gas.Factory):
        def children(self):
            yield from Gas.from_atoms('C', 'H')


class OrganicMolecule(Molecule):
    class Factory(Molecule.Factory):
        def children(self):
            yield from Molecule.from_atoms('C', 'H', 'O')


class Chitin(OrganicMolecule):
    default_name = 'chitin'

    class Factory(OrganicMolecule.Factory):
        def children(self):
            yield from OrganicMolecule.from_atoms('C', 'H', 'N', 'O')


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

    class Factory(Matter.Factory):
        def children(self):
            yield from next(ListFactory([
                Proteins,
                Lipids,
                Glucids,
            ]))
            yield from next(ListFactory([
                Proteins,
                Lipids,
                Glucids,
                None,
            ]))
            yield Salt.probable(30)


class Polymeric(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        def children(self):
            yield Polymers


class Plastic(Polymeric):
    pass


class Rubber(Polymeric):
    pass


class Oil(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        def children(self):
            yield Lipids


class Keratin(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        def children(self):
            yield Proteins


class Sweat(OrganicMatter):
    class Factory(OrganicMatter.Factory):
        def children(self):
            yield Water
            yield Salt
            yield Glucids
