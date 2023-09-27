from models.nested_model import NestedModel


class Plate(NestedModel):
    CONTINENT_PLATE = 'CONTINENT'
    OCEAN_PLATE = 'OCEAN'

    plate_type = None


class ContinentPlate(Plate):
    plate_type = Plate.CONTINENT_PLATE


class OceanPlate(Plate):
    plate_type = Plate.OCEAN_PLATE
