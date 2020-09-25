from generated import universe
from ...factory import Factory
from ...materials import RockFactory, IceFactory


class PlateFactory(Factory):
    default_model = universe.Plate
    ice_probability = 50

    def children(self):
        yield RockFactory()
        yield IceFactory().probable(self.ice_probability)


class MoonPlateFactory(PlateFactory):
    ice_probability = 0


class AsteroidPlateFactory(PlateFactory):
    ice_probability = 30
