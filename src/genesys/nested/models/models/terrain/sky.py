from genesys.nested.models.models.unknown import VisitorShip, Plane, Rocketship, Sprowseship
from genesys.nested.models import Model
from ..chemistry import Ice, Rock, WaterState, elements
from ..biology import SkyLife, SpaceAnimal


class Meteorite(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield SpaceAnimal.probable(6)
            yield Ice.probable(60)
            yield Rock
            yield elements['Fe'].probable(40)


class Ozone(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield elements['O']


class Cloud(WaterState):
    pass


class Precipitation(WaterState):
    class BaseFactory(WaterState.BaseFactory):
        default = ['rain', 'snow', 'hail', 'mist', 'fog', 'drizzle', 'storm']


class Sky(Model):
    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield VisitorShip.probable(10)
            yield Meteorite.probable(3)
            yield SkyLife
            yield Precipitation.probable(50)
            yield from Cloud.multiple(2, 8)
            yield elements['O']
            yield elements['C']
            yield Ozone


class TerraformedSky(Sky):
    class ChildrenFactory(Sky.ChildrenFactory):
        def children_classes(self):
            yield from Plane.multiple(1, 8)
            yield Rocketship.probable(20)
            yield from super().children_classes()


class FutureSky(Sky):
    class ChildrenFactory(Sky.ChildrenFactory):
        def children_classes(self):
            yield from Sprowseship.multiple(1, 8)
            yield from super().children_classes()
