from models.universe.planet.plate import Plate
from factories.thing.nested_factory import NestedFactory as Factory
from ...materials import RockFactory, IceFactory


class PlateFactory(Factory):
    # TODO: Refactor it
    default_model = Plate
    ice_probability = 50

    def children(self):
        yield RockFactory.one()
        yield IceFactory.probable(self.ice_probability)


class MoonPlateFactory(PlateFactory):
    # TODO: Refactor it
    ice_probability = 0


class AsteroidPlateFactory(PlateFactory):
    # TODO: Refactor it
    ice_probability = 30
