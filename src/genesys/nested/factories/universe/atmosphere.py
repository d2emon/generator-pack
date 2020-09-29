from generated import universe, terrain
from ..factory import Factory
from ..materials import MoleculeFactory, SteamFactory, AmmoniaFactory, MethaneFactory
from ..temporary import GasGiantLifeFactory


class OzoneFactory(MoleculeFactory):
    default_model = terrain.Ozone

    def children(self):
        yield from self.elements('O')


class AtmosphereFactory(Factory):
    default_model = universe.Atmosphere

    # Habitat
    def life(self):
        yield None

    def gases(self):
        yield MoleculeFactory.from_elements('O')
        yield MoleculeFactory.from_elements('C')
        yield OzoneFactory()

    def children(self):
        yield from self.life()
        yield from self.gases()


class GasGiantAtmosphereFactory(AtmosphereFactory):
    def life(self):
        yield GasGiantLifeFactory()

    def gases(self):
        yield MoleculeFactory.from_elements('He')
        yield MoleculeFactory.from_elements('H')
        yield SteamFactory().probable(50)
        yield AmmoniaFactory().probable(50)
        yield MethaneFactory().probable(50)
