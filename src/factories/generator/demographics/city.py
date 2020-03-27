"""
Large population centers of any scale are the result of traffic. Coastlines, navigable rivers and overland trade-routes
form a criss-crossing pattern of trade-arteries, and the towns and cities grow along those lines. The larger the
artery, the larger the town. And where several large arteries converge, you have a city. Villages are scattered densely
through the country between the larger settlements.
"""
import random
import math


MIN_VILLAGE = 20
MIN_TOWN = 1000
MIN_CITY = 8000
MIN_BIG_CITY = 12000

MAX_VILLAGE = MIN_TOWN
MAX_TOWN = MIN_CITY
MAX_CITY = MIN_BIG_CITY
MAX_BIG_CITY = 100000

MIN_FOR_VILLAGE = 20
MIN_FOR_TOWN = 15000
MIN_FOR_CITY = 300000
MIN_FOR_BIG_CITY = 2400000


class Settlement:
    """
    For purposes of this article, settlements will be divided into Villages, Towns, Cities and Big Cities (known as
    "supercities" in the parlance of urban historians).
    """
    min_population = 0
    max_population = MIN_VILLAGE
    min_size = 0
    max_size = None
    min_percent = 0
    max_percent = 0
    density = 1

    type_name = "Settlement"
    average_population = 1
    description = ""

    def __init__(self, name, population=None):
        self.name = name
        self.population = population

    @classmethod
    def generate(cls, name, min_population=None, max_population=None):
        min_population = min_population or cls.min_population
        max_population = max_population or cls.max_population
        population = random.randint(min_population, max_population)
        return cls(name, population)

    @classmethod
    def generate_population(cls, population):
        if population < cls.min_size:
            return 0
        if cls.max_size and population < cls.max_size:
            return int(population * cls.max_percent)
        return int(population * cls.min_percent)

    @classmethod
    def generate_count(cls, population, total):
        return math.ceil(population / cls.density)

    @classmethod
    def generate_distance(cls, count, area):
        if count <= 1:
            return None
        return math.ceil(math.sqrt(area / count))

    def __repr__(self):
        return "<{} \"{}({})\">".format(type(self).__name__, self.name, self.population)


class Village(Settlement):
    """
    Villages range from 20 to 1,000 people, with typical villages ranging from 50-300. Most kingdoms will have
    thousands of them. Villages are agrarian communities within the safe folds of civilization. They provide the basic
    source of food and land-stability in a feudal system. Usually, a village that supports orchards (instead of
    grainfields) is called a "hamlet." Occasionally, game writers use the term to apply to a very small village,
    regardless of what food it produces.
    """
    min_population = MIN_VILLAGE
    max_population = MAX_VILLAGE
    min_size = MIN_FOR_VILLAGE
    max_size = MIN_FOR_TOWN
    min_percent = .89
    max_percent = .98
    density = 450

    type_name = "village"
    average_population = 700
    description = """Villages range from 20 to 1,000 people, with typical villages ranging from 50-300. Most kingdoms
        will have thousands of them. Villages are agrarian communities within the safe folds of civilization. They
        provide the basic source of food and land-stability in a feudal system. Usually, a village that supports
        orchards (instead of grainfields) is called a "hamlet." Occasionally, game writers use the term to apply to a
        very small village, regardless of what food it produces."""


class TinyVillage(Village):
    type_name = "tiny village"
    average_population = 30


class SmallVillage(Village):
    type_name = "small village"
    average_population = 100


class Town(Settlement):
    """
    Towns range in population from 1,000-8,000 people, with typical values somewhere around 2,500. Culturally, these
    are the equivalent to the smaller American cities that line the interstates. Cities and towns tend to have walls
    only if they are frequently threatened.
    """
    min_population = MIN_TOWN
    max_population = MAX_TOWN
    min_size = MIN_FOR_TOWN
    max_size = MIN_FOR_CITY
    min_percent = .06
    max_percent = .09
    density = 5000

    type_name = "town"
    average_population = 5000
    description = """Towns range in population from 1,000-8,000 people, with typical values somewhere around 2,500.
        Culturally, these are the equivalent to the smaller American cities that line the interstates. Cities and
        towns tend to have walls only if they are frequently threatened."""


class SmallTown(Town):
    type_name = "small town"
    average_population = 1000


class LargeTown(Town):
    type_name = "large town"
    average_population = 8000


class City(Settlement):
    """
    Cities tend to be from 8,000-12,000 people, with an average in the middle of that range. A typical large kingdom
    will have only a few cities in this population range. Centers of scholarly pursuits (the Universities) tend to be
    in cities of this size, with only the rare exception thriving in a Big City.
    """
    min_population = MIN_CITY
    max_population = MAX_CITY
    min_size = MIN_FOR_CITY
    max_size = MIN_FOR_BIG_CITY
    min_percent = .025
    max_percent = .03
    density = 12000

    type_name = "city"
    average_population = 10000
    description = """Cities tend to be from 8,000-12,000 people, with an average in the middle of that range. A typical
        large kingdom will have only a few cities in this population range. Centers of scholarly pursuits (the
        Universities) tend to be in cities of this size, with only the rare exception thriving in a Big City."""


class BigCity(Settlement):
    """
    Big Cities range from 12,000-100,000 people, with some exceptional cities exceeding this scale. Some historical
    examples include London (25,000-40,000), Paris (50,000-80,000), Genoa (75,000-100,000), and Venice (100,000+).
    Moscow in the 15th century had a population in excess of 200,000!
    """
    min_population = MIN_BIG_CITY
    max_population = MAX_BIG_CITY
    min_size = MIN_FOR_BIG_CITY
    min_percent = .005

    type_name = "big city"
    average_population = 40000
    description = """Big Cities range from 12,000-100,000 people, with some exceptional cities exceeding this scale.
        Some historical examples include London (25,000-40,000), Paris (50,000-80,000), Genoa (75,000-100,000), and
        Venice (100,000+). Moscow in the 15th century had a population in excess of 200,000!"""

    @classmethod
    def generate_count(cls, population, total):
        if math.sqrt(total) <= 0:
            return 0
        return math.ceil(population / (math.sqrt(total) * 15))


class HugeCity(BigCity):
    type_name = "huge city"
    average_population = 150000


London = BigCity("London", population=random.randrange(25000, 40000))
Paris = BigCity("Paris", population=random.randrange(50000, 80000))
Genoa = BigCity("Genoa", population=random.randrange(75000, 100000))
Venice = BigCity("Venice", population=100000)
Moscow = BigCity("Moscow", population=200000)
