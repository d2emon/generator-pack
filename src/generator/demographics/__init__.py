"""
Fantasy worlds come in many varieties, from the "hard core" medieval-simulation school to the more fanciful realms of
high fantasy, with alabaster castles and jeweled gardens in the place of the more traditional muddy squalor. Despite
their differences, these share a vital common element: ordinary people. Most realms of fantasy, no matter how baroque
or magical, can not get by without a supply of ordinary farmers, merchants, quarreling princes and palace guards.
Clustered into villages and crowding the cities, they provide the human backdrop for adventure. Of course, doing the
research necessary to find out how common a large city should be, or how many shoemakers can be found in a town, can
take up time not all GMs have available. To the end of more satisfying world design, I've prepared this article.

This article is a distillation of broad possibilities drawn from a variety of historical reference points, focusing
more on results than on the details that create them. The rules here provide a baseline to be deviated from at need,
not numbers cast into iron. Following my favorite FRP traditions, I've focused my lens on a fairly developed version
of the middle ages - I've drawn freely from periods ranging from the 11th to 15th centuries, and from locales as varied
as Russia, England, France, Germany and Italy, but when I've needed a default rather than an average, I opted to look
more closely at late-medieval France as a good model for a trad-fantasy gameworld. Halve things, double things, or
otherwise fiddle with them to suit the feel you're going for; I've included guidelines on shaping the numbers to suit
your needs.

* Population Density: How Many In That Kingdom?
* Town and City Population: How Many In Those Walls?
* Population Spread
* An Example Kingdom: Chamlek
* Merchants and Services
* Agriculture
* Castles
* Miscellany

# Bibliography

The SV list was taken (mostly) from the tax list of Paris in 1292, and checked against other sources. This list can be
found in Life in a Medieval City by Joseph and Francis Geis (Harper and Row, 1981). This is a fine book by amateur
historians, which includes some fascinating descriptions of medieval city life and layout. You can also find the list
(including less-truncated versions) online if you poke around. Other books consulted include:

* Medieval Cities, by Henri Pirenne. Doubleday.
* The Castle Story, by Sheila Sancha. Harper Colophon.
* The Medieval Town, by John H. Mundy and Peter Riesenberg. Robert E. Krieger Publishing Company.
* The Medieval Town, by Fritz Rörig. University of California Press.
* Medieval Regions and Their Cities, by Josiah Cox Russel. David & Charles press.

# Examples

* https://www.rpglibrary.org/utils/meddemog/
* http://www.lucidphoenix.com/dnd/demo/

"""
import math

from .density import DEFAULT_DEVELOPMENT, generate_density
from .city import *


def round_or_percent(percent):
    if percent < 1:
        return "{}%".format(round(percent * 100))
    return round(percent)


class Kingdom:
    def __init__(
        self,
        name="Kingdom",
        area=780,
        development=DEFAULT_DEVELOPMENT,
        density=None,
        population=None,
        age=300,
    ):
        self.name = name

        self.area = area
        self.age = age

        self.development = development
        self._density = density
        self._population = population

        self.arable = 0

        # Population spread
        self.hermits = 0

        self.village_population = 0
        self.villages = 0
        self.village_distance = 0

        self.town_population = 0
        self.towns = 0
        self.town_distance = 0

        self.city_population = 0
        self.cities = 0
        self.city_distance = 0

        self.big_city_population = 0
        self.big_cities = 0

        self.universities = 0

        self.livestock = 0
        self.fowl = 0
        self.meat_animals = 0

        self.ruins = 0
        self.castles_active = 0
        self.castles_civilized = 0

        self.pop_business = 0

        self.city_text = ""

        self.generate_population()
        self.generate_castle()

    @property
    def density(self):
        if not self._density:
            self._density = generate_density(self.development)
        return self._density

    @property
    def population(self):
        if not self._population:
            self._population = int(self.density * self.area)
        return self._population

    @property
    def arable_percent(self):
        return int((self.arable / self.area) * 100)

    @property
    def wilderness(self):
        return int(self.area - self.arable)

    def generate_population(self):
        """

        :return:
        """
        self.arable = int(self.population / 69.5)

        self.village_population = Village.generate_population(self.population)
        self.villages = Village.generate_count(self.village_population, self.population)
        self.village_distance = Village.generate_distance(self.villages, self.area)

        self.town_population = Town.generate_population(self.population)
        self.towns = Town.generate_count(self.town_population, self.population)
        self.town_distance = Town.generate_distance(self.towns, self.area)

        self.city_population = City.generate_population(self.population)
        self.cities = City.generate_count(self.city_population, self.population)

        self.big_city_population = BigCity.generate_population(self.population)
        self.big_cities = BigCity.generate_count(self.big_city_population, self.population)
        self.city_distance = City.generate_distance(self.cities + self.big_cities, self.area)

        self.hermits = self.population - (
                self.village_population
                + self.town_population
                + self.city_population
                + self.big_city_population)
        print(self.area / self.hermits)

        if self.population >= 27300000:
            self.universities = int(self.population / 27300000)
        else:
            self.universities = 0

        self.livestock = int(self.population * 2.2)
        self.fowl = int(self.livestock * .68)
        self.meat_animals = self.livestock - self.fowl

        self.generate_castle()

    @property
    def castles(self):
        return self.castles_active + self.ruins

    @property
    def castles_wilderness(self):
        return self.castles - self.castles_civilized

    def generate_castle(self):
        """

        :return:
        """
        self.ruins = round((self.population / 5000000) * (math.sqrt(self.age)))
        self.castles_active = round(self.population / 50000)
        self.castles_civilized = round(self.castles * .75)


class EnforcementType:
    def __init__(self, name="", value=1.0):
        self.name = name
        self.value = value

    def generate(self, population):
        return round_or_percent(population * self.value / 150)


class CityDescription:
    types = (
        TinyVillage,
        SmallVillage,
        Village,
        SmallTown,
        Town,
        LargeTown,
        City,
        BigCity,
        HugeCity,
    )
    enforcements = (
        EnforcementType("little to no", .25),
        EnforcementType("indifferent", .5),
        EnforcementType("undependable", .75),
        EnforcementType("typical", 1),
        EnforcementType("zealous", 1.5),
        EnforcementType("oppresive", 2),
        EnforcementType("tyrannical", 3),
    )

    def __init__(self, type_id=4, enforcement_id=3, kingdom=None, population=5000):
        self.settlement_type = self.types[type_id]
        self.enforcement_type = self.enforcements[enforcement_id]

        self.kingdom = kingdom or Kingdom()
        self.population = population

        self.area = 0
        self.size = 0

        self.army = 0
        self.pop_business = 0
        self.services = dict()

        self.businessAutoCalc()

    def businessAutoCalc(self):
        """

        :return:
        """
        self.pop_business = self.settlement_type.average_population
        self.businessCalc()

    def businessCalc(self):
        """

        :return:
        """
        density = 15000
        self.area = (self.pop_business / density)
        if self.area < 1:
            self.size = math.ceil(self.area * 100) / 100
        else:
            self.size = math.ceil(self.area * 10) / 10

        self.army = self.enforcement_type.generate(self.pop_business)
        self.services = {
            "Clergy": round_or_percent(self.pop_business / 40),
            "Shoemakers": round_or_percent(self.pop_business / 150),
            "Nobles": round_or_percent(self.pop_business / 200),
            "Furriers": round_or_percent(self.pop_business / 250),
            "Maidservants": round_or_percent(self.pop_business / 250),
            "Tailors": round_or_percent(self.pop_business / 250),
            "Barbers": round_or_percent(self.pop_business / 350),
            "Jewelers": round_or_percent(self.pop_business / 400),
            "Taverns": round_or_percent(self.pop_business / 400),
            "Old-Clothes": round_or_percent(self.pop_business / 400),
            "Pastrycooks": round_or_percent(self.pop_business / 500),
            "Masons": round_or_percent(self.pop_business / 500),
            "Carpenters": round_or_percent(self.pop_business / 550),
            "Weavers": round_or_percent(self.pop_business / 600),
            "Lawyers": round_or_percent(self.pop_business / 650),
            "Chandlers": round_or_percent(self.pop_business / 700),
            "Mercers": round_or_percent(self.pop_business / 700),
            "Coopers": round_or_percent(self.pop_business / 700),
            "Woodsellers": round_or_percent(self.pop_business / 700),
            "Bakers": round_or_percent(self.pop_business / 800),
            "Watercarriers": round_or_percent(self.pop_business / 850),
            "Scabbardmakers": round_or_percent(self.pop_business / 850),
            "Winesellers": round_or_percent(self.pop_business / 900),
            "Hatmakers": round_or_percent(self.pop_business / 950),
            "Saddlers": round_or_percent(self.pop_business / 1000),
            "Chicken Butchers": round_or_percent(self.pop_business / 1000),
            "Pursemakers": round_or_percent(self.pop_business / 1100),
            "Butchers": round_or_percent(self.pop_business / 1200),
            "Fishmongers": round_or_percent(self.pop_business / 1200),
            "Priests": round_or_percent(self.pop_business / 1200),
            "Beer-Sellers": round_or_percent(self.pop_business / 1400),
            "Buckle Makers": round_or_percent(self.pop_business / 1400),
            "Plasterers": round_or_percent(self.pop_business / 1400),
            "Spice Merchants": round_or_percent(self.pop_business / 1400),
            "Blacksmiths": round_or_percent(self.pop_business / 1500),
            "Painters": round_or_percent(self.pop_business / 1500),
            "Doctors": round_or_percent(self.pop_business / 1700),
            "Roofers": round_or_percent(self.pop_business / 1800),
            "Locksmiths": round_or_percent(self.pop_business / 1900),
            "Bathers": round_or_percent(self.pop_business / 1900),
            "Ropemakers": round_or_percent(self.pop_business / 1900),
            "Inns": round_or_percent(self.pop_business / 2000),
            "Tanners": round_or_percent(self.pop_business / 2000),
            "Copyists": round_or_percent(self.pop_business / 2000),
            "Sculptors": round_or_percent(self.pop_business / 2000),
            "Rugmakers": round_or_percent(self.pop_business / 2000),
            "Harness-Makers": round_or_percent(self.pop_business / 2000),
            "Bleachers": round_or_percent(self.pop_business / 2100),
            "Hay Merchants": round_or_percent(self.pop_business / 2300),
            "Cutlers": round_or_percent(self.pop_business / 2300),
            "Glovemakers": round_or_percent(self.pop_business / 2400),
            "Woodcarvers": round_or_percent(self.pop_business / 2400),
            "Apothecaries": round_or_percent(self.pop_business / 2800),
            "Bookbinders": round_or_percent(self.pop_business / 3000),
            "Illuminators": round_or_percent(self.pop_business / 3900),
            "Booksellers": round_or_percent(self.pop_business / 6300),
        }

    @property
    def acres(self):
        return math.ceil(self.area * 1000000 / 4047)

    @property
    def description(self):
        services = ""
        for key, value in self.services.items():
            services += "{} {}\n".format(value, key)

        return ("Towns and Cities\n"
                + "{description}\n"
                + "A settlement (e.g. {type}) in {kingdom} with a population of {population} will occupy roughly "
                + "{area}km^2 ({acres} acres).\n"
                + "A settlement this size with {enforcement_type} law enforcement will probably have {army} armed "
                + "agents of the ruling authority (guardsmen, watchmen, etc.).\n"
                + "This settlement will probably have the following businesses and services available. (A percentage "
                + "chance is indicated where no certainty exists.)\n"
                + "{services}").format(
            description=self.settlement_type.description,
            type=self.settlement_type.type_name,
            kingdom=self.kingdom.name,
            population=self.population,
            area=self.size,
            acres=self.acres,
            enforcement_type=self.enforcement_type.name,
            army=self.army,
            services=services,
        )
