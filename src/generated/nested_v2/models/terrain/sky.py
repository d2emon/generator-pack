from generated.nested_v2.models import VisitorShip, Plane, Rocketship, Sprowseship
from genesys.nested.models import Model
from generated.materials.chemistry import Gas, Ice, WaterState, elements
from generated.materials import Rock
from ..biology import Habitat
# from ..biology import SkyLife, SpaceAnimal


class Meteorite(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield SpaceAnimal.probable(6)
            yield Ice.probable(60)
            yield Rock
            yield elements['Fe'].probable(40)


class Ozone(Gas):
    class Factory(Gas.Factory):
        def children(self):
            yield Gas.from_atoms('O')


class Cloud(WaterState):
    pass


class Precipitation(WaterState):
    class BaseFactory(WaterState.BaseFactory):
        default = ['rain', 'snow', 'hail', 'mist', 'fog', 'drizzle', 'storm']


class Sky(Habitat):
    transport = Habitat.children_property(VisitorShip)
    meteorites = Habitat.children_property(Meteorite)
    precipitations = Habitat.children_property(Precipitation)
    clouds = Habitat.children_property(Cloud)
    gases = Habitat.children_property(Gas)

    class Factory(Model.Factory):
        @classmethod
        def transport(cls):
            yield VisitorShip.probable(10)

        @classmethod
        def meteorites(cls):
            yield Meteorite.probable(3)

        @classmethod
        def life(cls):
            # yield SkyLife
            yield None

        @classmethod
        def precipitations(cls):
            yield Precipitation.probable(50)
            yield from Cloud.multiple(2, 8)

        @classmethod
        def clouds(cls):
            yield Gas.from_atoms('O')
            yield Gas.from_atoms('C')
            yield Ozone

        def children(self):
            yield from self.transport()
            yield from self.meteorites()
            yield from self.life()
            yield from self.precipitations()
            yield from self.clouds()


class TerraformedSky(Sky):
    class Factory(Sky.Factory):
        @classmethod
        def transport(cls):
            yield from Plane.multiple(1, 8)
            yield Rocketship.probable(20)


class FutureSky(Sky):
    class Factory(Sky.Factory):
        @classmethod
        def transport(cls):
            yield from Sprowseship.multiple(1, 8)
