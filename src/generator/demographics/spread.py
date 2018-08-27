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


class CitiesGenerator:
    def __init__(self, population=500000):
        self.population = population

    @classmethod
    def first(cls, population):
        """
        First, determine the population of the largest city in the kingdom. This is equal to (P times M), where P is equal
        to the square root of the country's population, and M is equal to a random roll of 2d4+10 (the average roll is 15).
        :return:
        """
        p = math.sqrt(population)
        m = d(2, 4) + 10
        return int(p * m)

    @classmethod
    def second(cls, first):
        """
        The second-ranking city will be from 20-80% the size of the largest city. To randomly determine this, roll 2d4
        times 10% (the average result is 50%)

        :param first:
        :return:
        """
        return int(d(2, 4) * .10 * first)

    def cities(self):
        """
        Each remaining city will be from 10% to 40% smaller than the previous one (2d4 times 5% - the average result is
        25%); continue listing cities for as long as the results maintain a city-scaled population (8,000 or more).

        :return:
        """
        min_city = 8000

        population = self.population

        city = self.first(population)
        if city <= min_city:
            return
        yield city
        population -= city

        city = self.second(city)
        if city <= min_city:
            return
        yield city
        population -= city

        while True:
            city -= int(d(2, 4) * .05 * city)
            if city <= min_city:
                return
            yield city
            population -= city

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
    def towns(cls, population=1000000, towns_count=10):
        import random
        for _ in range(towns_count):
            town = random.randrange(1000, 8000)
            if town >= population:
                break
            yield town
            population -= town

    @classmethod
    def villages(cls, population=1000):
        """
        The remaining population live in villages, hamlets and smaller settlements; a small number will live in isolated
        dwellings or be itinerent workers and wanderers.

        :param population:
        :param towns:
        :return:
        """
        import random
        while population > 20:
            village = random.randrange(20, 1000)
            if village >= population:
                village = population
            yield village
            population -= village

    def generate(self):
        population = self.population

        cities = list(self.cities())
        for city in cities:
            population -= city

        towns_count = self.towns_count(len(cities))
        towns = list(self.towns(population, towns_count))
        for town in towns:
            population -= town

        villages = list(self.villages(population))
        for village in villages:
            population -= village

        print(len(cities), len(towns), len(villages))
        return cities, towns, villages, population

