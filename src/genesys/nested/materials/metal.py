from models.materials import metal
from .elements import MoleculeFactory


class IronFactory(MoleculeFactory):
    model = metal.Iron
    contents = 'Fe',


class SteelFactory(MoleculeFactory):
    model = metal.Steel
    contents = 'Fe', 'C',
