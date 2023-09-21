from genesys.nested.factories.nested_factory import NestedFactory
from models.universe import planet
from models.v5 import terrain
from ...materials import MoleculeFactory


class OzoneFactory(MoleculeFactory):
    # TODO: Refactor it
    default_model = terrain.Ozone
    contents = 'O'


class AtmosphereFactory(NestedFactory):
    # TODO: Refactor it
    default_model = planet.atmosphere.Atmosphere

    def life(self):
        yield None

    def gases(self):
        yield MoleculeFactory.element_factories('O', 'C')
        yield OzoneFactory()

    def children(self):
        yield from self.life()
        yield from self.gases()
