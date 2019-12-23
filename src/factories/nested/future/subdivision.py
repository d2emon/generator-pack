from . import dummy
from ..land.dummy import City
from factory.thing import Thing
from ..land.subdivision import Continent


class Sprowseship(Thing):
    default_name = "sprowseship"

    @classmethod
    def children_data(cls):
        yield dummy.FutureHomeRoom.multiple_factory(2, 4)
        yield dummy.Nanocollector.multiple_factory(1, 3)


class LivingCenter(Thing):
    default_name = "living center"

    @classmethod
    def children_data(cls):
        yield dummy.FutureBuilding.multiple_factory(20, 30)


class Spaceport(Thing):
    default_name = "spaceport"

    @classmethod
    def children_data(cls):
        yield Sprowseship.multiple_factory(4, 12)
        yield dummy.FuturePerson.multiple_factory(6, 20)
        yield dummy.FutureCommercialBuilding.multiple_factory(2, 6)


class SpendingCenter(Thing):
    default_name = "spending center"

    @classmethod
    def children_data(cls):
        yield dummy.FutureCommercialBuilding.multiple_factory(20, 30)


class FutureCity(City):
    default_name = "citadion"

    @classmethod
    def children_data(cls):
        yield Spaceport.multiple_factory(1, 3)
        yield LivingCenter.multiple_factory(5, 20)
        yield SpendingCenter.multiple_factory(5, 20)


class FutureContinent(Continent):
    default_name = "united continent of {}{}"
    name_parts = [
        Continent.list_factory([
            "Eu", "A", "O", "E", "Ca", "Ma",
        ]),
        Continent.list_factory([
            "rt", "lt", "rm", "t", "tr", "tl", "str", "s", "m", "fr",
        ]),
        Continent.list_factory([
            "a", "o", "e", "i",
        ]),
        Continent.list_factory([
            "ri", "ni", "ti", "fri", "", "",
        ]),
        Continent.list_factory([
            "sia", "nia", "ca",
        ]),
        Continent.list_factory([
            "A", "Eu", "Ame", "Ocea", "Anta", "Atla",
        ]),
        Continent.list_factory([
            "frica", "rtica", "ropa", "rica", "nia", "sia", "ntide",
        ]),
    ]

    @classmethod
    def generate_name(cls):
        return cls.default_name.format(
            cls.name_parts[0].generate(),
            cls.name_parts[1].generate(),
        )

    @classmethod
    def children_data(cls):
        yield FutureCity.multiple_factory(20, 50)


class DysonSegment(Thing):
    default_name = "dyson segment"

    @classmethod
    def children_data(cls):
        yield FutureCity.multiple_factory(4, 20)
        yield dummy.Nanocollector.multiple_factory(12, 20)


class DysonSurface(Thing):
    default_name = "dyson surface"

    @classmethod
    def children_data(cls):
        yield DysonSegment.multiple_factory(16)
