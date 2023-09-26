from models.materials import metal
from .molecules import MoleculeFactory


class IronFactory(MoleculeFactory):
    model = metal.Iron
    contents = 'Fe',


class SteelFactory(MoleculeFactory):
    model = metal.Steel
    contents = 'Fe', 'C',
