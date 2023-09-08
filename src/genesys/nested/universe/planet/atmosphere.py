from models.universe.planet.atmosphere import Atmosphere
from models.v5 import terrain
from factories.thing.nested_factory import NestedFactory as Factory
from ..materials import MoleculeFactory, SteamFactory, AmmoniaFactory, MethaneFactory
from ..life import GasGiantLifeFactory


class OzoneFactory(MoleculeFactory):
    default_model = terrain.Ozone

    def children(self):
        yield from self.elements('O')


class AtmosphereFactory(Factory):
    default_model = Atmosphere

    def life(self):
        yield None

    def gases(self):
        yield MoleculeFactory.from_elements('O')
        yield MoleculeFactory.from_elements('C')
        yield OzoneFactory()

    def children(self):
        yield from self.life()
        yield from self.gases()
