from models.thing import Thing
from . import dummy


class Locality(Thing):
    pass


class Village(Locality):
    default_name = "village"

    @classmethod
    def children_data(cls):
        yield dummy.ResidentalArea.multiple_factory(1, 4)
        yield dummy.CommercialArea.probable_factory(90)
        yield dummy.PoliceStation.probable_factory(50)
        yield dummy.FireDepartment.probable_factory(40)
        yield dummy.Museum.probable_factory(5)
        yield dummy.Library.probable_factory(40)
        yield dummy.Farm.multiple_factory(0, 6)
        yield dummy.Factory.multiple_factory(0, 2)
        yield dummy.Cemetery.probable_factory(60)
        yield dummy.ResearchFacility.probable_factory(4)


class City(Locality):
    default_name = "city"

    @classmethod
    def children_data(cls):
        yield dummy.Monument.probable_factory(15)
        yield dummy.Monument.probable_factory(5)
        yield dummy.ResidentalArea.multiple_factory(4, 9)
        yield dummy.CommercialArea.multiple_factory(1, 5)
        yield dummy.PoliceStation
        yield dummy.PoliceStation.probable_factory(50)
        yield dummy.FireDepartment
        yield dummy.FireDepartment.probable_factory(50)
        yield dummy.Museum.probable_factory(40)
        yield dummy.Library.probable_factory(60)
        yield dummy.Hospital
        yield dummy.Farm.multiple_factory(0, 3)
        yield dummy.Factory.multiple_factory(1, 4)
        yield dummy.Cemetery
        yield dummy.ResearchFacility.probable_factory(2)


class Capital(Locality):
    default_name = "capital"

    @classmethod
    def children_data(cls):
        yield dummy.Monument.probable_factory(70)
        yield dummy.Monument.probable_factory(40)
        yield dummy.Monument.probable_factory(10)
        yield dummy.ResidentalArea.multiple_factory(7, 15)
        yield dummy.CommercialArea.multiple_factory(3, 9)
        yield dummy.PoliceStation.multiple_factory(2, 5)
        yield dummy.FireDepartment.multiple_factory(1, 3)
        yield dummy.Museum.multiple_factory(1, 2)
        yield dummy.Library.multiple_factory(1, 3)
        yield dummy.Hospital.multiple_factory(1, 3)
        yield dummy.Farm.multiple_factory(0, 2)
        yield dummy.Factory.multiple_factory(2, 6)
        yield dummy.Cemetery
        yield dummy.Cemetery.probable_factory(50)
        yield dummy.ResearchFacility.probable_factory(1)
