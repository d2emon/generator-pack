from models.v5 import terrain
from factories.thing.nested_factory import NestedFactory as Factory
from ..life import SkyLifeFactory
from ..materials import RockFactory, IronFactory, IceFactory, SteamFactory, WaterFactory


class CloudFactory(SteamFactory):
    default_model = terrain.Cloud


class PrecipitationFactory(WaterFactory):
    default_model = terrain.Precipitation
    names = ['rain', 'snow', 'hail', 'mist', 'fog', 'drizzle', 'storm']

    def generate_name(self):
        return self.select_item(*self.names)


class MeteoriteFactory(Factory):
    default_model = terrain.Meteorite

    def children(self):
        # yield SpaceAnimal.probable(6)
        yield IceFactory().probable(60)
        yield RockFactory()
        yield IronFactory().probable(40)


class SkyFactory(Factory):
    default_model = terrain.Sky

    @classmethod
    def transport(cls):
        # yield VisitorShip.probable(10)
        yield None

    @classmethod
    def meteorites(cls):
        yield MeteoriteFactory().probable(3)

    @classmethod
    def life(cls):
        yield SkyLifeFactory()

    @classmethod
    def precipitations(cls):
        yield PrecipitationFactory().probable(50)

    @classmethod
    def clouds(cls):
        yield from CloudFactory().multiple(2, 8)

    def children(self):
        yield from self.transport()
        yield from self.meteorites()
        yield from self.life()
        yield from self.precipitations()
        yield from self.clouds()


class TerraformedSkyFactory(SkyFactory):
    @classmethod
    def transport(cls):
        # yield from Plane.multiple(1, 8)
        # yield Rocketship.probable(20)
        yield None


class FutureSkyFactory(SkyFactory):
    @classmethod
    def transport(cls):
        # yield from Sprowseship.multiple(1, 8)
        yield None
