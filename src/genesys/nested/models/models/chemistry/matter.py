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
from .elements import elements
from .particles import Atom


class Molecule(Model):
    atoms = Model.child_property(Atom)

    default_name = 'molecules'

    class Factory(Model.Factory):
        def children(self):
            yield Atom

    @classmethod
    def from_atoms(cls, *components):
        return map(lambda component: elements.get(component), components)


class Matter(Molecule):
    molecules = Model.child_property(Atom, Molecule)

    default_name = None


class Water(Matter):
    class Factory(Matter.Factory):
        def children(self):
            yield from Matter.from_atoms('H', 'O')


class WaterState(Model):
    water = Model.child_property(Water)

    class Factory(Model.Factory):
        def children(self):
            yield Water


class Dew(WaterState):
    pass


class Ice(WaterState):
    pass


class Snowflakes(WaterState):
    pass


# class Snow(Model):
#     flakes = Model.child_property(Snowflakes)
#
#     class Factory(Model.Factory):
#         class ChildrenFactory(Model.Factory.ChildrenFactory):
#             def builders(self):
#                 yield Snowflakes


class Ammonia(Matter):
    class Factory(Matter.Factory):
        def children(self):
            yield from Matter.from_atoms('N', 'H')


# class Salt(Matter):
#     class Factory(Matter.Factory):
#         class ChildrenFactory(Matter.Factory.ChildrenFactory):
#             def builders(self):
#                 yield from Matter.from_atoms('Na', 'Cl')


class Silica(Matter):
    class Factory(Matter.Factory):
        def children(self):
            yield from Matter.from_atoms('Si', 'O')


# class Steel(Matter):
#     class Factory(Matter.Factory):
#         class ChildrenFactory(Model.Factory.ChildrenFactory):
#             def builders(self):
#                 yield from Matter.from_atoms('Fe', 'C')
