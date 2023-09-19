from models.v5 import materials
from .molecules import MoleculeFactory


class MetalFactory(MoleculeFactory):
    pass


class IronFactory(MetalFactory):
    model = materials.Iron
    contents = 'Fe',


class SteelFactory(MetalFactory):
    model = materials.Steel
    contents = 'Fe', 'C',
