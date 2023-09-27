from genesys.nested.factories.nested_factory import NestedFactory
from models.planet import atmosphere
from models.v5 import terrain
from genesys.nested.materials.elements import MoleculeFactory


class OzoneFactory(MoleculeFactory):
    # TODO: Refactor it
    default_model = terrain.Ozone
    contents = 'O'


class AtmosphereFactory(NestedFactory):
    # TODO: Refactor it
    default_model = atmosphere.Atmosphere

    def life(self):
        yield None

    def gases(self):
        yield MoleculeFactory.element_factories('O', 'C')
        yield OzoneFactory()

    def children(self):
        yield from self.life()
        yield from self.gases()
