from . import dummy
from ..dummy import Mountain
from factory.thing import Thing
from ..subdivision import Region, Land, Continent, Biome


class MedievalRegion(Region):
    default_name = "{} {}"
    biome_types = Thing.list_factory([
        "hilly", "rainy", "lush", "foggy", "desertic", "green", "tropical", "rich", "barren", "scorched"
    ])
    region_types = Thing.list_factory([
        "shire", "province", "county", "parish", "pale"
    ])

    @classmethod
    def generate_name(cls):
        return cls.default_name.format(
            cls.biome_types.generate(),
            cls.region_types.generate(),
        )

    @classmethod
    def children_data(cls):
        yield dummy.MedievalCapital
        yield dummy.MedievalVillage.multiple_factory(2, 6)
        yield dummy.Dungeon.probable_factory(15)
        yield dummy.Dungeon.probable_factory(5)


class MedievalLand(Land):
    default_name = "{} of {}{}{}{}{}{}"
    land_types = Thing.list_factory([
        "realm", "kingdom", "empire", "dominion"
    ])
    land_name_parts = [
        Thing.list_factory([
            "G", "P", "S", "St", "Sh", "B", "F", "K", "Z", "Az", "Oz",
        ]),
        Thing.list_factory([
            "", "", "", "r", "l",
        ]),
        Thing.list_factory([
            "u", "o", "a", "e",
        ]),
        Thing.list_factory([
            "r", "sh", "nd", "st", "sd", "kl", "kt", "pl", "fr", "ck", "sh", "ff", "gg", "l", "lig", "rag", "sha",
            "pta", "lir", "limd", "lim", "shim", "stel",
        ]),
        Thing.list_factory([
            "i", "u", "o", "oo", "e", "ee", "y", "a",
        ]),
        Thing.list_factory([
            "ll", "th", "h", "k", "lm", "r", "g", "gh", "n", "m", "p", "s", "rg", "lg",
        ]),
    ]

    @classmethod
    def generate_name(cls):
        return cls.default_name.format(
            cls.land_types.generate(),
            cls.land_name_parts[0].generate(),
            cls.land_name_parts[1].generate(),
            cls.land_name_parts[2].generate(),
            cls.land_name_parts[3].generate(),
            cls.land_name_parts[4].generate(),
            cls.land_name_parts[5].generate(),
        )

    @classmethod
    def region_factory(cls):
        yield MedievalRegion.multiple_factory(1, 10)

    @classmethod
    def battlefield_factory(cls):
        yield dummy.MedievalBattlefield.probable_factory(10)


class MedievalContinent(Continent):
    default_name = "explored continent"

    @classmethod
    def land_factory(cls):
        yield MedievalLand.multiple_factory(1, 6)


class AncientBiome(Biome):
    forest_types = Thing.list_factory([
        dummy.AncientForest.multiple_factory(0, 4),
        dummy.AncientJungle.multiple_factory(0, 4),
    ])

    @classmethod
    def children_data(cls):
        yield dummy.AncientPlain.multiple_factory(1, 10)
        yield cls.forest_types.generate()
        yield Mountain.multiple_factory(0, 3)


class AncientLand(Land):
    default_name = "{} land"
    biome_types = Thing.list_factory([
        "hilly", "rainy", "lush", "foggy", "desertic", "green", "tropical", "rich", "barren", "scorched",
    ])

    @classmethod
    def generate_name(cls):
        return cls.default_name.format(cls.biome_types.generate())

    @classmethod
    def region_factory(cls):
        yield from []

    @classmethod
    def battlefield_factory(cls):
        yield from []

    @classmethod
    def biome_factory(cls):
        yield from AncientBiome.children_data()


class AncientContinent(Continent):
    default_name = "continent"

    @classmethod
    def land_factory(cls):
        yield AncientLand.multiple_factory(1, 5)
