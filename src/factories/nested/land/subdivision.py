from . import dummy
from factory.thing import Thing
from . import town


class Biome(Thing):
    default_name = "biome"
    forest_types = Thing.list_factory([
        dummy.Forest.multiple_factory(0, 4),
        dummy.Jungle.multiple_factory(0, 4),
    ])

    @classmethod
    def children_data(cls):
        yield dummy.Plain.multiple_factory(1, 5)
        yield cls.forest_types.next()
        yield dummy.Mountain.multiple_factory(0, 3)


class Region(Thing):
    default_name = "{}{} region"
    directions = Thing.list_factory([
        "north ", "east ", "south ", "west ", "north-west ", "north-east ", "south-west ", "south-east ", "center ",
        "oversea ",
    ])
    biome_types = Thing.list_factory([
        "hilly", "rainy", "lush", "foggy", "desertic", "green", "tropical", "rich", "barren", "scorched",
    ])

    @classmethod
    def children_data(cls):
        yield town.Capital
        yield town.City.multiple_factory(1, 10)
        yield town.Village.multiple_factory(2, 15)

    @property
    def capital(self):
        return self.find_one(town.Capital)

    @property
    def cities(self):
        return self.find(town.City)

    @property
    def villages(self):
        return self.find(town.Village)


class Land(Biome):
    @classmethod
    def region_factory(cls):
        yield Region.multiple_factory(1, 10)

    @classmethod
    def battlefield_factory(cls):
        yield dummy.Battlefield.probable_factory(10)

    @classmethod
    def biome_factory(cls):
        yield from Biome.children_data()

    @classmethod
    def children_data(cls):
        yield from cls.region_factory()
        yield from cls.battlefield_factory()
        yield from cls.biome_factory()

    @property
    def regions(self):
        return self.find(Region)

    @property
    def battlefields(self):
        return self.find(dummy.Battlefield)

    @property
    def biomes(self):
        return self.find(dummy.BiomeType)


class Country(Land):
    default_name = "country of {}{}"
    name_parts = [
        Thing.list_factory([
            "Li", "Arme", "Le", "Molda", "Slove", "Tur", "Afgha", "Alba", "Alge", "Tu", "Fran", "Baha", "Su", "Austra",
            "Germa", "In", "Ara", "Austri", "Be", "Ba", "Bra", "Ru", "Chi", "Ja", "Tai", "Bangla", "Gha", "Bou", "Bo",
            "Tas", "Ze", "Mon", "Mo", "Ne", "Neder", "Spai", "Portu", "Po", "Por", "Mol", "Bul", "Bru", "Bur", "Gro",
            "Syl", "Gui", "Da", "Gree", "Bri", "Ita"
        ]),
        Thing.list_factory([
            "ly", "dania", "mas", "vania", "ce", "nea", "nau", "topia", "garia", "gal", "laska", "golia", "nisia",
            "land", "snia", "livia", "mania", "than", "nin", "pan", "wan", "zil", "ssia", "na", "rein", "lgium", "bia",
            "ny", "ce", "stan", "distan", "nistan", "dan", "lia", "nia", "via", "sia", "tia", "key", "desh", "dia",
        ]),
    ]


class Continent(Thing):
    @classmethod
    def land_factory(cls):
        yield Country.multiple_factory(1, 10)

    @classmethod
    def children_data(cls):
        yield from cls.land_factory()
        yield dummy.Sea.multiple_factory(1, 5)

    @property
    def lands(self):
        return self.find(Land)

    @property
    def seas(self):
        return self.find(dummy.Sea)


class ModernContinent(Continent):
    default_name = "continent of {}{}"
    name_parts = [
        Thing.list_factory([
            "A", "Eu", "Ame", "Ocea", "Anta", "Atla",
        ]),
        Thing.list_factory([
            "frica", "rtica", "ropa", "rica", "nia", "sia", "ntide",
        ]),
        Thing.list_factory([
            "Eu", "A", "O", "E",
        ]),
        Thing.list_factory([
            "rt", "lt", "rm", "t", "tr", "tl", "str", "s", "m", "fr",
        ]),
        Thing.list_factory([
            "a", "o", "e", "i",
        ]),
        Thing.list_factory([
            "ri", "ni", "ti", "fri", "", "",
        ]),
        Thing.list_factory([
            "sia", "nia", "ca",
        ]),
    ]

    @classmethod
    def generate_name(cls):
        return cls.default_name.format(
            cls.name_parts[0].generate(),
            cls.name_parts[1].generate(),
        )
