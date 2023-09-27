from genesys.nested.factories.nested_factory import NestedFactory
from models.planet import plate
from ...materials import RockFactory, IceFactory


class PlateFactory(NestedFactory):
    model = plate.Plate


class IcePlateFactory(PlateFactory):
    model = plate.OceanPlate

    def children(self):
        yield IceFactory.one()


class RockPlateFactory(PlateFactory):
    model = plate.ContinentPlate

    def children(self):
        yield RockFactory.one()
