"""
Basic materials and particles
"""
from nestedg.model import Model
from . import particles
from .chemistry import elements, reaction


class Molecule(Model):
    atoms = Model.child_property(particles.Atom)

    class NameGenerator(Model.NameGenerator):
        default = 'molecules'

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield particles.Atom


class Matter(Model):
    contents = Model.children_property(particles.Atom)


class Water(Matter):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from reaction('H', 'O')


class Dew(Model):
    contents = Model.child_property(Water)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield Water


class Ice(Model):
    contents = Model.child_property(Water)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield Water


class Snowflakes(Model):
    contents = Model.child_property(Water)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield Water


class Snow(Model):
    flakes = Model.child_property(Snowflakes)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield Snowflakes


class Salt(Matter):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from reaction('Na', 'Cl')


class Ammonia(Matter):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from reaction('N', 'H')


class Methane(Matter):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from reaction('C', 'H')


class Steel(Matter):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from reaction('Fe', 'C')


class Silica(Matter):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from reaction('Si', 'O')


class Rock(Matter):
    contents = Model.children_property(Silica, particles.Atom)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield Silica
            yield elements['Al'].probable(30)
            yield elements['Fe'].probable(20)
            yield elements['K'].probable(20)
            yield elements['Na'].probable(50)
            yield elements['Ca'].probable(50)


class Diamond(Rock):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield elements['C']


class Magma(Rock):
    pass


# Organic


class OrganicMolecule(Molecule):
    atoms = Model.children_property(particles.Atom)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from reaction('C', 'H', 'O')


class Chitin(OrganicMolecule):
    class NameGenerator(Model.NameGenerator):
        default = 'chitin'

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield from reaction('C', 'H', 'N', 'O')


class Proteins(OrganicMolecule):
    class NameGenerator(Model.NameGenerator):
        default = 'proteins'


class Lipids(OrganicMolecule):
    class NameGenerator(Model.NameGenerator):
        default = 'lipids'


class Glucids(OrganicMolecule):
    class NameGenerator(Model.NameGenerator):
        default = 'glucose'


class Alcohol(Glucids):
    class NameGenerator(Model.NameGenerator):
        default = 'alcohol'


class OrganicMatter(Matter):
    proteins = Model.children_property(Proteins)
    lipids = Model.children_property(Lipids)
    glucids = Model.children_property(Glucids)
    salt = Model.children_property(Salt)

    class ChildrenGenerator(Model.ChildrenGenerator):
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
                yield from Model.BaseGenerator(component).next()
            yield Salt.probable(30)


class Fire(Matter):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield elements['C']
            yield elements['O']


class Ash(Matter):
    contents = Model.children_property(OrganicMatter, particles.Atom)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield OrganicMatter
            yield elements['C']


class Oil(OrganicMatter):
    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield Lipids


class Polymers(Glucids):
    class NameGenerator(Model.NameGenerator):
        default = 'polymers'


class Polymeric(OrganicMatter):
    polymers = Model.children_property(Polymers)

    class ChildrenGenerator(Model.ChildrenGenerator):
        def children_classes(self):
            yield Polymers


class Plastic(Polymeric):
    pass


class Rubber(Polymeric):
    pass
