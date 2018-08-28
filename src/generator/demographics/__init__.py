"""
    Fantasy worlds come in many varieties, from the "hard core" medieval-simulation school to the more fanciful realms
of high fantasy, with alabaster castles and jeweled gardens in the place of the more traditional muddy squalor. Despite
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

    The SV list was taken (mostly) from the tax list of Paris in 1292, and checked against other sources. This list can
be found in Life in a Medieval City by Joseph and Francis Geis (Harper and Row, 1981). This is a fine book by amateur
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


class City:
    options = (
        (10, "Barren, Desolate"),
        (15, "Rocky, Chilly"),
        (20, "Cool, Dry; Swampy"),
        (30, "Hilly, Temperate"),
        (40, "Abundant Arable Land"),
        (50, "Fertile, Warm, Idyllic"),
    )

    def __init__(self, city_type=0, kingdom=None, population=5000, enforcement_type=1):
        self.option = self.options[city_type][0]
        self.settlement_type = city_type
        self.kingdom = kingdom
        self.population = population
        self.enforcement_type = enforcement_type

        self.area = 0
        self.size = 0

        self.army = 0
        self.pop_business = 0

        self.businessAutoCalc()
        self.cityDesc()

    def businessAutoCalc(self):
        """

        :return:
        """
        self.pop_business = self.option
        self.businessCalc()

    def businessCalc(self):
        """
        function businessCalc()
        {
          var iCityDensity = 15000
          var iCityArea = (document.formDomesday.pop_business.value / iCityDensity)
          if (iCityArea < 1)
          {
            document.formDomesday.citysize_km2.value = Math.ceil(iCityArea * 100) / 100;
          }
          else
          {
            document.formDomesday.citysize_km2.value = Math.ceil(iCityArea * 10) / 10;
          }
          document.formDomesday.citysize_acres.value = Math.ceil(iCityArea * 1000000 / 4047);

          document.formDomesday.num_thugs.value = roundOrPercent(document.formDomesday.pop_business.value * document.formDomesday.thug_zeal.options[document.formDomesday.thug_zeal.selectedIndex].value / 150 );

          document.formDomesday.num_clergy.value = roundOrPercent(document.formDomesday.pop_business.value / 40);
          document.formDomesday.num_shoemakers.value = roundOrPercent(document.formDomesday.pop_business.value / 150);
          document.formDomesday.num_nobles.value = roundOrPercent(document.formDomesday.pop_business.value / 200);
          document.formDomesday.num_furriers.value = roundOrPercent(document.formDomesday.pop_business.value / 250);
          document.formDomesday.num_maidservants.value = roundOrPercent(document.formDomesday.pop_business.value / 250);
          document.formDomesday.num_tailors.value = roundOrPercent(document.formDomesday.pop_business.value / 250);
          document.formDomesday.num_barbers.value = roundOrPercent(document.formDomesday.pop_business.value / 350);
          document.formDomesday.num_jewelers.value = roundOrPercent(document.formDomesday.pop_business.value / 400);
          document.formDomesday.num_taverns.value = roundOrPercent(document.formDomesday.pop_business.value / 400);
          document.formDomesday.num_oldclothes.value = roundOrPercent(document.formDomesday.pop_business.value / 400);
          document.formDomesday.num_pastrycooks.value = roundOrPercent(document.formDomesday.pop_business.value / 500);
          document.formDomesday.num_masons.value = roundOrPercent(document.formDomesday.pop_business.value / 500);
          document.formDomesday.num_carpenters.value = roundOrPercent(document.formDomesday.pop_business.value / 550);
          document.formDomesday.num_weavers.value = roundOrPercent(document.formDomesday.pop_business.value / 600);
          document.formDomesday.num_lawyers.value = roundOrPercent(document.formDomesday.pop_business.value / 650);
          document.formDomesday.num_chandlers.value = roundOrPercent(document.formDomesday.pop_business.value / 700);
          document.formDomesday.num_mercers.value = roundOrPercent(document.formDomesday.pop_business.value / 700);
          document.formDomesday.num_coopers.value = roundOrPercent(document.formDomesday.pop_business.value / 700);
          document.formDomesday.num_woodsellers.value = roundOrPercent(document.formDomesday.pop_business.value / 700);
          document.formDomesday.num_bakers.value = roundOrPercent(document.formDomesday.pop_business.value / 800);
          document.formDomesday.num_watercarriers.value = roundOrPercent(document.formDomesday.pop_business.value / 850);
          document.formDomesday.num_scabbardmakers.value = roundOrPercent(document.formDomesday.pop_business.value / 850);
          document.formDomesday.num_winesellers.value = roundOrPercent(document.formDomesday.pop_business.value / 900);
          document.formDomesday.num_hatmakers.value = roundOrPercent(document.formDomesday.pop_business.value / 950);
          document.formDomesday.num_saddlers.value = roundOrPercent(document.formDomesday.pop_business.value / 1000);
          document.formDomesday.num_chickenbutchers.value = roundOrPercent(document.formDomesday.pop_business.value / 1000);
          document.formDomesday.num_pursemakers.value = roundOrPercent(document.formDomesday.pop_business.value / 1100);
          document.formDomesday.num_butchers.value = roundOrPercent(document.formDomesday.pop_business.value / 1200);
          document.formDomesday.num_fishmongers.value = roundOrPercent(document.formDomesday.pop_business.value / 1200);
          document.formDomesday.num_priests.value = roundOrPercent(document.formDomesday.pop_business.value / 1200);
          document.formDomesday.num_beersellers.value = roundOrPercent(document.formDomesday.pop_business.value / 1400);
          document.formDomesday.num_bucklemakers.value = roundOrPercent(document.formDomesday.pop_business.value / 1400);
          document.formDomesday.num_plasterers.value = roundOrPercent(document.formDomesday.pop_business.value / 1400);
          document.formDomesday.num_spicemerchants.value = roundOrPercent(document.formDomesday.pop_business.value / 1400);
          document.formDomesday.num_blacksmiths.value = roundOrPercent(document.formDomesday.pop_business.value / 1500);
          document.formDomesday.num_painters.value = roundOrPercent(document.formDomesday.pop_business.value / 1500);
          document.formDomesday.num_doctors.value = roundOrPercent(document.formDomesday.pop_business.value / 1700);
          document.formDomesday.num_roofers.value = roundOrPercent(document.formDomesday.pop_business.value / 1800);
          document.formDomesday.num_locksmiths.value = roundOrPercent(document.formDomesday.pop_business.value / 1900);
          document.formDomesday.num_bathers.value = roundOrPercent(document.formDomesday.pop_business.value / 1900);
          document.formDomesday.num_ropemakers.value = roundOrPercent(document.formDomesday.pop_business.value / 1900);
          document.formDomesday.num_inns.value = roundOrPercent(document.formDomesday.pop_business.value / 2000);
          document.formDomesday.num_tanners.value = roundOrPercent(document.formDomesday.pop_business.value / 2000);
          document.formDomesday.num_copyists.value = roundOrPercent(document.formDomesday.pop_business.value / 2000);
          document.formDomesday.num_sculptors.value = roundOrPercent(document.formDomesday.pop_business.value / 2000);
          document.formDomesday.num_rugmakers.value = roundOrPercent(document.formDomesday.pop_business.value / 2000);
          document.formDomesday.num_harnessmakers.value = roundOrPercent(document.formDomesday.pop_business.value / 2000);
          document.formDomesday.num_bleachers.value = roundOrPercent(document.formDomesday.pop_business.value / 2100);
          document.formDomesday.num_haymerchants.value = roundOrPercent(document.formDomesday.pop_business.value / 2300);
          document.formDomesday.num_cutlers.value = roundOrPercent(document.formDomesday.pop_business.value / 2300);
          document.formDomesday.num_glovemakers.value = roundOrPercent(document.formDomesday.pop_business.value / 2400);
          document.formDomesday.num_woodcarvers.value = roundOrPercent(document.formDomesday.pop_business.value / 2400);
          document.formDomesday.num_apothecaries.value = roundOrPercent(document.formDomesday.pop_business.value / 2800);
          document.formDomesday.num_bookbinders.value = roundOrPercent(document.formDomesday.pop_business.value / 3000);
          document.formDomesday.num_illuminators.value = roundOrPercent(document.formDomesday.pop_business.value / 3900);
          document.formDomesday.num_booksellers.value = roundOrPercent(document.formDomesday.pop_business.value / 6300);
        }

        :return:
        """
        density = 15000
        self.area = (self.pop_business / density)
        if self.area < 1:
            self.size = math.ceil(self.area * 100) / 100
        else:
            self.size = math.ceil(self.area * 10) / 10

        # self.num_thugs = round_or_percent(self.pop_business * self.thug_zeal[self.thug_zeal_index] / 150)

    @property
    def acres(self):
        return math.ceil(self.area * 1000000 / 4047)

    def cityDesc(self):
        """

        :return:
        """
        self.city_text = self.city.description

    def description(self):
        services = ""
        return ("Towns and Cities\n"
                + "A settlement (e.g. {type}) in {kingdom} with a population of {population} will occupy roughly "
                + "{area}km^2 ({acres} acres).\n"
                + "A settlement this size with {enforcement_type} law enforcement will probably have {army} armed "
                + "agents of the ruling authority (guardsmen, watchmen, etc.).\n"
                + "This settlement will probably have the following businesses and services available. (A percentage "
                + "chance is indicated where no certainty exists.)\n"
                + "{}").format(
            type=self.settlement_type,
            kingdom=self.kingdom.name,
            population=self.population,
            area=self.size,
            acres=self.acres,
            enforcement_type=self.enforcement_type,
            army=self.army,
            services=services,
        )


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

        self.city = city or City()

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

        self.populationCalc()
        self.castleCalc()

    """
    function kingdomName()
    {
      var sKingdom = document.formDomesday.kingdom_name.value;
      document.formDomesday.kingdom_001.value = sKingdom;
      document.formDomesday.kingdom_002.value = sKingdom;
      document.formDomesday.kingdom_003.value = sKingdom;
      document.formDomesday.kingdom_004.value = sKingdom;
      document.formDomesday.kingdom_005.value = sKingdom;
      document.formDomesday.kingdom_006.value = sKingdom;
      document.formDomesday.kingdom_007.value = sKingdom;
    }
    """

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

    def populationCalc(self):
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

    def castleCalc(self):
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
