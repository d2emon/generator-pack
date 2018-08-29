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


def round_or_percent(percent):
    if percent < 1:
        return "{}%".format(round(percent * 100))
    return round(percent)


class Hex:
    def __init__(self, width=30):
        self.width = width

    @property
    def area(self):
        return round((self.width * 0.9305347) ** 2)


class Kingdom:
    densities = (
        10,
        15,
        20,
        30,
        40,
        50,
    )
    density_description = (
        "Barren, Desolate",
        "Rocky, Chilly",
        "Cool, Dry; Swampy",
        "Hilly, Temperate",
        "Abundant Arable Land",
        "Fertile, Warm, Idyllic",
    )

    def __init__(self, name="Kingdom", area=780, density=3, age=300, city=None, map_hex=None):
        self.name = name

        self.hex = map_hex or Hex()

        self.area = area
        self.density = self.densities[density]
        self.age = age

        # self.city = city or City()

        self.arable = 0

        self.population = 0
        self.hermits = 0
        self.village_population = 0
        self.town_population = 0
        self.city_population = 0
        self.big_city_population = 0

        self.villages = 0
        self.towns = 0
        self.cities = 0
        self.big_cities = 0

        self.village_distance = 0
        self.town_distance = 0
        self.city_distance = 0

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
    def hexes(self):
        if not self.hex:
            return 0
        if self.hex.area <= 0:
            return 0
        if self.area / self.hex.area >= 1:
            return round(self.area / self.hex.area)
        return round(self.area / self.hex.area, 1)

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
        self.population = self.density * self.area
        self.arable = int(self.population / 69.5)

        if self.population < 20:
            self.village_population = 0
            self.town_population = 0
            self.city_population = 0
            self.big_city_population = 0
        elif self.population < 15000:
            self.village_population = int(self.population * .98)
            self.town_population = 0
            self.city_population = 0
            self.big_city_population = 0
        elif self.population < 300000:
            self.village_population = int(self.population * .89)
            self.town_population = int(self.population * .09)
            self.city_population = 0
            self.big_city_population = 0
        elif self.population < 2400000:
            self.village_population = int(self.population * .89)
            self.town_population = int(self.population * .06)
            self.city_population = int(self.population * .03)
            self.big_city_population = 0
        else:
            self.village_population = int(self.population * .89)
            self.town_population = int(self.population * .06)
            self.city_population = int(self.population * .025)
            self.big_city_population = int(self.population * .005)
        self.hermits = self.population - (
                self.village_population
                + self.town_population
                + self.city_population
                + self.big_city_population)

        self.villages = math.ceil(self.village_population / 450)
        self.towns = math.ceil(self.town_population / 5000)
        self.cities = math.ceil(self.city_population / 12000)

        if math.sqrt(self.population) > 0:
            self.big_cities = math.ceil(self.big_city_population / (math.sqrt(self.population) * 15))
        else:
            self.big_cities = 0

        if self.villages > 1:
            self.village_distance = round(math.sqrt(self.area / self.villages))
        else:
            self.village_distance = None

        if self.towns > 1:
            self.town_distance = round(math.sqrt(self.area / self.towns))
        else:
            self.town_distance = None

        if self.cities > 1:
            self.city_distance = round(math.sqrt(self.area / (self.cities + self.big_cities)))
        else:
            self.city_distance = None

        if self.population >= 27300000:
            self.universities = int(self.population / 27300000)
        else:
            self.universities = 0

        self.livestock = int(self.population * 2.2)
        self.fowl = int(self.livestock * .68)
        self.meat_animals = self.livestock - self.fowl

        self.castleCalc()

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

    @property
    def land_mass_description(self):
        hex_text = ""
        if self.hex:
            hex_text = " ({hexes} hexes, each {hex.width}km across and roughly {hex.area}km^2 in area)".format(
                hex=self.hex,
                hexes=self.hexes,
            )

        return ("The population density of {name}, due to factors such as climate, geography, and political "
                + "environment, is {density} persons per km^2.\n"
                + "{name} occupies {area}km^2{hex}. Roughly {percent_arable}% of this is arable land, or {arable}km^2. "
                + "The remaining {wilderness}km^2 is divided among wilderness, rivers, lakes, and the like.").format(
            name=self.name,
            density=self.density,
            area=self.area,
            hex=hex_text,
            percent_arable=self.arable_percent,
            arable=self.arable,
            wilderness=self.wilderness
        )

    @property
    def population_description(self):
        return ("{name}'s population is approximately {population} persons.\n"
                + "{hermits} residents are isolated or itinerant.\n"
                + "{village_population} residents live in {villages} villages.\n"
                + "{town_population} residents live in {towns} towns.\n"
                + "{city_population} residents live in {cities} cities.\n"
                + "{big_city_population} residents live in {big_cities} big cities.\n"
                + "The average distance between villages is {village_distance}km.\n"
                + "The average distance between towns is {town_distance}km.\n"
                + "The average distance between cities (including big cities) is {city_distance}km.\n"
                + "{name} supports {universities} Universities.\n"
                + "{name} supports {livestock} head of livestock:\n"
                + "{fowl} fowl (e.g. chickens, geese, ducks).\n"
                + "{meat_animals} dairy and meat animals (e.g. cows, goats, pigs, sheep).").format(
            name=self.name,
            population=self.population,
            hermits=self.hermits,
            villages=self.villages,
            village_population=self.village_population,
            village_distance=self.village_distance,
            towns=self.towns,
            town_population=self.town_population,
            town_distance=self.town_distance,
            cities=self.cities,
            city_population=self.city_population,
            city_distance=self.city_distance,
            big_cities=self.big_cities,
            big_city_population=self.big_city_population,
            universities=self.universities,
            livestock=self.livestock,
            fowl=self.fowl,
            meat_animals=self.meat_animals,
        )

    @property
    def castles_description(self):
        return ("The inhabitants of {name} have been building castles for the last {age} years.\n"
                + "There are approximately {castles} standing fortifications in {name}.\n"
                + "{castles_active} castles are in active use.\n"
                + "{ruins} castles are ruined or abandoned.\n"
                + "{castles_civilized} castles are located in settled areas.\n"
                + "{castles_wilderness} castles are located in remote areas, unsettled areas, or wilderness.\n"
                + "(All numbers are approximate, particularly where ruins and wilderness are concerned.)").format(
            name=self.name,
            age=self.age,
            castles=self.castles,
            castles_active=self.castles_active,
            ruins=self.ruins,
            castles_civilized=self.castles_civilized,
            castles_wilderness=self.castles_wilderness,
        )

    @property
    def description(self):
        return ("Land Mass\n{}\n"
                +"Population\n{}\n"
                +"Castles and Fortifications\n{}\n").format(
            self.land_mass_description,
            self.population_description,
            self.castles_description,
        )


class SettlementType:
    def __init__(self, name="", population=5000, description=""):
        self.name = name
        self.population = population
        self.description = description


class EnforcementType:
    def __init__(self, name="", value=1.0):
        self.name = name
        self.value = value

    def generate(self, population):
        return round_or_percent(population * self.value / 150)


class City:
    types = (
        SettlementType("tiny village", 30, """Villages range from 20 to 1,000 people, with typical villages ranging
        from 50-300. Most kingdoms will have thousands of them. Villages are agrarian communities within the safe folds
        of civilization. They provide the basic source of food and land-stability in a feudal system. Usually, a
        village that supports orchards (instead of grainfields) is called a "hamlet." Occasionally, game writers use
        the term to apply to a very small village, regardless of what food it produces."""),
        SettlementType("small village", 100, """Villages range from 20 to 1,000 people, with typical villages ranging
        from 50-300. Most kingdoms will have thousands of them. Villages are agrarian communities within the safe folds
        of civilization. They provide the basic source of food and land-stability in a feudal system. Usually, a
        village that supports orchards (instead of grainfields) is called a "hamlet." Occasionally, game writers use
        the term to apply to a very small village, regardless of what food it produces."""),
        SettlementType("village", 700, """Villages range from 20 to 1,000 people, with typical villages ranging from
        50-300. Most kingdoms will have thousands of them. Villages are agrarian communities within the safe folds of
        civilization. They provide the basic source of food and land-stability in a feudal system. Usually, a village
        that supports orchards (instead of grainfields) is called a "hamlet." Occasionally, game writers use the term
        to apply to a very small village, regardless of what food it produces."""),
        SettlementType("small town", 1000, """Towns range in population from 1,000-8,000 people, with typical values
        somewhere around 2,500. Culturally, these are the equivalent to the smaller American cities that line the
        interstates. Cities and towns tend to have walls only if they are frequently threatened."""),
        SettlementType("town", 5000, """Towns range in population from 1,000-8,000 people, with typical values
        somewhere around 2,500. Culturally, these are the equivalent to the smaller American cities that line the
        interstates. Cities and towns tend to have walls only if they are frequently threatened."""),
        SettlementType("large town", 8000, """Towns range in population from 1,000-8,000 people, with typical values
        somewhere around 2,500. Culturally, these are the equivalent to the smaller American cities that line the
        interstates. Cities and towns tend to have walls only if they are frequently threatened."""),
        SettlementType("city", 10000, """Cities tend to be from 8,000-12,000 people, with an average in the middle of
        that range. A typical large kingdom will have only a few cities in this population range. Centers of scholarly
        pursuits (the Universities) tend to be in cities of this size, with only the rare exception thriving in a
        Big City."""),
        SettlementType("big city", 40000, """Big Cities range from 12,000-100,000 people, with some exceptional cities
        exceeding this scale. Some historical examples include London (25,000-40,000), Paris (50,000-80,000), Genoa
        (75,000-100,000), and Venice (100,000+). Moscow in the 15th century had a population in excess of 200,000!"""),
        SettlementType("huge city", 150000, """Big Cities range from 12,000-100,000 people, with some exceptional
        cities exceeding this scale. Some historical examples include London (25,000-40,000), Paris (50,000-80,000),
        Genoa (75,000-100,000), and Venice (100,000+). Moscow in the 15th century had a population in excess of
        200,000!"""),
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
        self.pop_business = self.settlement_type.population
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
            type=self.settlement_type.name,
            kingdom=self.kingdom.name,
            population=self.population,
            area=self.size,
            acres=self.acres,
            enforcement_type=self.enforcement_type.name,
            army=self.army,
            services=services,
        )