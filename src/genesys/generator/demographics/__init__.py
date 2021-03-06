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
from .density import DEFAULT_DEVELOPMENT, generate_density
from .city import *
from .population import SimpleCitiesGenerator
from .services import populate_services, round_or_percent
from .agriculture import Agriculture
from .castles import ruins, castles, civilized
from .miscellany import univercity, livestock, fowl


class Kingdom(SimpleCitiesGenerator):
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

        # Population spread
        super().__init__(self.population, self.area)
        self.agriculture = Agriculture(self.population, self.area)

        self.universities = 0

        self.fowl = 0
        self.meat_animals = 0

        self.ruins = 0
        self.castles_active = 0
        self.castles_civilized = 0

        self.generate_population()
        self.generate_castles()

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
    def livestock(self):
        return self.fowl + self.meat_animals

    def generate_population(self):
        """

        :return:
        """
        self.universities = univercity(self.population)

        total_livestock = livestock(self.population)
        self.fowl = fowl(total_livestock)
        self.meat_animals = total_livestock - self.fowl

    @property
    def castles(self):
        return self.castles_active + self.ruins

    @property
    def castles_wilderness(self):
        return self.castles - self.castles_civilized

    def generate_castles(self):
        """

        :return:
        """
        self.ruins = ruins(self.population, self.age)
        self.castles_active = castles(self.population)
        self.castles_civilized = civilized(self.castles)


class EnforcementType:
    def __init__(self, name="", value=1.0):
        self.name = name
        self.value = value

    def generate(self, population):
        return round_or_percent(population * self.value / 150)


class CityDescription:
    enforcements = (
        EnforcementType("little to no", .25),
        EnforcementType("indifferent", .5),
        EnforcementType("undependable", .75),
        EnforcementType("typical", 1),
        EnforcementType("zealous", 1.5),
        EnforcementType("oppresive", 2),
        EnforcementType("tyrannical", 3),
    )

    def __init__(self, settlement_type=Town, enforcement_id=3, kingdom=None, population=5000):
        self.settlement_type = settlement_type
        self.enforcement_type = self.enforcements[enforcement_id]

        self.kingdom = kingdom or Kingdom()
        self.population = population

        self.army = 0
        self.services = dict()

        self.generate()

    @property
    def average_population(self):
        return self.settlement_type.average_population

    @property
    def area(self):
        density = 15000
        return self.average_population / density

    @property
    def acres(self):
        return self.area * 1000000 / 4047

    def generate(self):
        """

        :return:
        """
        self.army = self.enforcement_type.generate(self.average_population)
        self.services = populate_services(self.average_population)


    @property
    def description(self):
        return ("Towns and Cities\n"
                + "{description}\n"
                + "A settlement (e.g. {type}) in {kingdom} with a population of {population} will occupy roughly "
                + "{area:.2f}km² ({acres:.2f} acres).\n"
                + "A settlement this size with {enforcement_type} law enforcement will probably have {army} armed "
                + "agents of the ruling authority (guardsmen, watchmen, etc.).\n"
                + "This settlement will probably have the following businesses and services available. (A percentage "
                + "chance is indicated where no certainty exists.)\n"
                + "{services}").format(
            description=self.settlement_type.description,
            type=self.settlement_type.type_name,
            kingdom=self.kingdom.name,
            population=self.population,
            area=self.area,
            acres=self.acres,
            enforcement_type=self.enforcement_type.name,
            army=self.army,
            services="\n".join(["{} {}".format(value, key) for key, value in self.services.items()]),
        )


def calculate_population(
        area=0,
        age=0,
        density=None,
        urban=None,
        isolated=None,
    ):
    """
    Densities:
        Random
        Low (30-50)
        Medium (60-80)
        High (90-120)

    Urban:
        Random
        Low (1-3)%
        Medium (4-5)%
        High (6-8)%

    Isolated:
        Random
        Low (2-3)%
        High (4-5)%

    :arg area: Land size (square miles)
    :arg age: Kingdom age (years)
    :arg density: Desired density (people per square mile)
    :arg urban: Urban percentage
    :arg isolated: Isolated percentage
    :return:
    """
    print(area, age, density, urban, isolated)


def population_center(
        population=0,
        enable_dnd=False,
        city_type=0,
        races=(),
        classes=(),
    ):
    """
    Populations:
        Village (20-1000)
        Town (1000-8000)
        City (8000-12000)
        Big City(12000-100000)

    City Types:
        Isolated - 4 races, little divercity
        Mixed - 7 races, more divercity
        Integrated - 7 races, most divercity

    Races:
        Human
        Halfling
        Elf
        Dwarf
        Gnome
        Half-Elf
        Half-Orc
        OtherA
        OtherB
        OtherC
        OtherD
        OtherE
        OtherF
        OtherG

    Classes:
        Barbarian   (dom)
        Bard
        Cleric
        Druid
        Fighter
        Monk        (dom)
        Paladin
        Ranger
        Rogue
        Sorcerer
        Wizard
        Adept
        Aristocrat
        Expert
        Warrior
        Commoner

    Class.priority:
        Low/Normal
        High

    :arg population: Specific population or randomly generated
    :arg enable_dnd: Enable D&D calculations
    :arg city_type: Population Type
    :arg races: Races
    :arg classes: Highest levels (before city modifiers)
    :return:
    """
    print(population, enable_dnd, city_type, races, classes)
