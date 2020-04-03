"""
- Molecule
- Diamond
- Magma
- Rock
- Silica
- Salt
- Water
- Fire
- Dew
- Ice
- Snow
- Snowflakes
- Steel
"""
from genesys.nested.models import Model
from .particles import Atom
from .elements import elements


class Molecule(Model):
    atoms = Model.child_property(Atom)

    class NameFactory(Model.NameFactory):
        default = 'molecules'

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Atom

    @classmethod
    def from_atoms(cls, *components):
        return map(lambda component: elements.get(component), components)


class Matter(Molecule):
    molecules = Model.child_property(Atom, Molecule)


class Water(Matter):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield from Matter.from_atoms('H', 'O')


class WaterState(Model):
    water = Model.child_property(Water)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Water


class Dew(WaterState):
    pass


class Ice(WaterState):
    pass


class Snowflakes(WaterState):
    pass


class Snow(Model):
    flakes = Model.child_property(Snowflakes)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield Snowflakes


class Salt(Matter):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield from Matter.from_atoms('Na', 'Cl')


class Silica(Matter):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield from Matter.from_atoms('Si', 'O')


class Steel(Matter):
    class ChildrenFactory(Matter.ChildrenFactory):
        def children_classes(self):
            yield from Matter.from_atoms('Fe', 'C')
