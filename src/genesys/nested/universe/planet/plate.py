from genesys.nested.factories.nested_factory import NestedFactory
from models.universe.planet.plate import Plate
from ...materials import RockFactory, IceFactory


class PlateFactory(NestedFactory):
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
