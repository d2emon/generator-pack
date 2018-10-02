"""
Okay, so you know how big your kingdom is, and how many people live there. How many people live in the cities, and how
many cities are there? How many live in smaller settlements, like towns and villages?



    Adjusting the Number of Towns: The ratio of towns to cities given above presumes the existence of a notable and
thriving mercantile community. Adjust the upward by 50% or more for a fantasy world on the verge of Renaissance, but
adjust it sharply downward for a pre-Crusades type world (if trade is limited and local, there won't be many more towns
than there are cities; just continue the 10%-40% city-reduction scale to produce a single list of cities and towns).
Historically, the number of town charters in many European countries multiplied nearly by 10 from the 11th-13th
centuries as economic shifts reshaped the agrarian scheme into something more robustly mercantile. If your world has a
visible share of merchants and rogues and other town-living types (as most do) use the 2d8 roll or even more. For a
world in transition between these extremes, find a middle ground you like the looks of.
"""
import math

from dice import d

from .city import BigCity, City, Town, Village


class PopulationGroup:
    def __init__(self, settlement_type, population, area):
        self.population = population
        self.settlements = population
        if settlement_type:
            self.population = settlement_type.generate_population(population)
            self.settlements = settlement_type.generate_count(self.population, population)

        self.distance = 0
        if self.settlements > 1:
            self.distance = math.sqrt(area / self.settlements)

    @classmethod
    def generate(cls, items, settlement_type, population, area):
        population_group = cls(settlement_type, population, area)
        population_group.population = 0
        for item in items:
            population_group.population += item.population
        return population_group


class SimpleCitiesGenerator:
    def __init__(self, population=500000, area=5000):
        self._population = population
        self._area = area

        self.hermits = None
        self.villages = None
        self.towns = None
        self.cities = None
        self.big_cities = None
        self.generate()

    def generate(self):
        self.villages = PopulationGroup(Village, self.population, self.area)
        self.towns = PopulationGroup(Town, self.population, self.area)
        self.cities = PopulationGroup(City, self.population, self.area)
        self.big_cities = PopulationGroup(BigCity, self.population, self.area)
        self.hermits = PopulationGroup(
            None,
            self.population - (
                self.villages.population
                + self.towns.population
                + self.cities.population
                + self.big_cities.population
            ),
            self.area,
        )
        self.cities.distance = City.generate_distance(self.cities.population + self.big_cities.population, self.area)


class CitiesGenerator(SimpleCitiesGenerator):
    @classmethod
    def first(cls, population):
        """
        First, determine the population of the largest city in the kingdom. This is equal to (P times M), where P is equal
        to the square root of the country's population, and M is equal to a random roll of 2d4+10 (the average roll is 15).
        :return:
        """
        p = math.sqrt(population)
        m = d(2, 4) + 10
        city_population = int(p * m)
        if city_population < City.min_population:
            return None
        if city_population >= City.max_population:
            return BigCity("First", city_population)
        return City("First", city_population)

    @classmethod
    def second(cls, first):
        """
        The second-ranking city will be from 20-80% the size of the largest city. To randomly determine this, roll 2d4
        times 10% (the average result is 50%)

        :param first:
        :return:
        """
        population = int(d(2, 4) * .10 * first.population)
        if population < City.min_population:
            return None
        return City("Second", population)

    @classmethod
    def next(cls, city):
        """
        Each remaining city will be from 10% to 40% smaller than the previous one (2d4 times 5% - the average result is
        25%); continue listing cities for as long as the results maintain a city-scaled population (8,000 or more).

        :return:

        """
        population = city.population - int(d(2, 4) * .05 * city.population)
        if population < City.min_population:
            return None
        return City("City", population)

    def cities_generator(self):
        population = self.population

        city = self.first(population)
        if not city:
            return
        yield city
        population -= city.population

        city = self.second(city)
        if not city:
            return
        yield city
        population -= city.population

        while True:
            city = self.next(city)
            if not city:
                return
            yield city
            population -= city.population

    @classmethod
    def towns_count(cls, cities_count=10):
        """
        To determine the number of towns, start with the number of cities, and multiply it by a roll of 2d8 (the average
        result is 9).

        :param cities:
        :return:
        """
        return d(2, 8) * cities_count

    @classmethod
    def towns_generator(cls, population=1000000, towns_count=10):
        for _ in range(towns_count):
            town = Town.generate("Town")
            population -= town.population
            if population < town.min_population:
                break
            yield town

    @classmethod
    def villages_generator(cls, population=1000):
        """
        The remaining population live in villages, hamlets and smaller settlements; a small number will live in isolated
        dwellings or be itinerent workers and wanderers.

        :param population:
        :param towns:
        :return:
        """
        while population > 20:
            village = Village.generate("Village")
            if village.population >= population:
                village.population = population
            yield village
            population -= village.population

    def generate(self):
        population = self.population
        self.big_cities = PopulationGroup(BigCity, population, self.area)

        cities_list = list(self.cities_generator())
        self.cities = PopulationGroup.generate(cities_list, City, population, self.area)
        population -= self.cities.population

        towns_count = self.towns_count(len(cities_list))
        towns_list = list(self.towns_generator(population, towns_count))
        self.towns = PopulationGroup.generate(towns_list, Town, population, self.area)
        population -= self.towns.population

        villages_list = list(self.villages_generator(population))
        self.villages = PopulationGroup.generate(villages_list, Village, population, self.area)
        population -= self.villages.population

        self.hermits = PopulationGroup(None, population, self.area)
        self.cities.distance = City.generate_distance(self.cities.population + self.big_cities.population, self.area)
