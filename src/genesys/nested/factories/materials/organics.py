from genesys.nested.factories.v2.thing_builder import ListFactory
from generated.materials.matter import Molecule, Gas
from generated.materials.minerals import Salt
from generated.materials.organics import OrganicMolecule, Proteins, Lipids, Glucids, Polymers
from .matter import MatterFactory, MoleculeFactory, GasFactory


class MetaneFactory(GasFactory):
    def children(self):
        yield from Gas.from_atoms('C', 'H')


class OrganicMoleculeFactory(MoleculeFactory):
    def children(self):
        yield from Molecule.from_atoms('C', 'H', 'O')


class OrganicMatterFactory(MatterFactory):
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


class ChitinFactory(OrganicMoleculeFactory):
    def children(self):
        yield from OrganicMolecule.from_atoms('C', 'H', 'N', 'O')


class PolymericFactory(OrganicMatterFactory):
    def children(self):
        yield Polymers
