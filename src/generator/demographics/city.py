"""
Large population centers of any scale are the result of traffic. Coastlines, navigable rivers and overland trade-routes
form a criss-crossing pattern of trade-arteries, and the towns and cities grow along those lines. The larger the
artery, the larger the town. And where several large arteries converge, you have a city. Villages are scattered densely
through the country between the larger settlements.
"""
import random


class Settlement:
    """
    For purposes of this article, settlements will be divided into Villages, Towns, Cities and Big Cities (known as
    "supercities" in the parlance of urban historians).
    """
    min_population = 0
    max_population = 20

    def __init__(self, name, population=None):
        self.name = name
        self.population = population

    @classmethod
    def generate_population(cls):
        return random.randrange(cls.min_population, cls.max_population)


class Village(Settlement):
    """
    Villages range from 20 to 1,000 people, with typical villages ranging from 50-300. Most kingdoms will have
    thousands of them. Villages are agrarian communities within the safe folds of civilization. They provide the basic
    source of food and land-stability in a feudal system. Usually, a village that supports orchards (instead of
    grainfields) is called a "hamlet." Occasionally, game writers use the term to apply to a very small village,
    regardless of what food it produces.
    """
    min_population = 20
    max_population = 1000


class Town(Settlement):
    """
    Towns range in population from 1,000-8,000 people, with typical values somewhere around 2,500. Culturally, these
    are the equivalent to the smaller American cities that line the interstates. Cities and towns tend to have walls
    only if they are frequently threatened.
    """
    min_population = 1000
    max_population = 8000


class City(Settlement):
    """
    Cities tend to be from 8,000-12,000 people, with an average in the middle of that range. A typical large kingdom
    will have only a few cities in this population range. Centers of scholarly pursuits (the Universities) tend to be
    in cities of this size, with only the rare exception thriving in a Big City.
    """
    min_population = 8000
    max_population = 12000


class BigCity(Settlement):
    """
    Big Cities range from 12,000-100,000 people, with some exceptional cities exceeding this scale. Some historical
    examples include London (25,000-40,000), Paris (50,000-80,000), Genoa (75,000-100,000), and Venice (100,000+).
    Moscow in the 15th century had a population in excess of 200,000!
    """
    min_population = 12000
    max_population = 100000


London = BigCity("London", population=random.randrange(25000, 40000))
Paris = BigCity("Paris", population=random.randrange(50000, 80000))
Genoa = BigCity("Genoa", population=random.randrange(75000, 100000))
Venice = BigCity("Venice", population=100000)
Moscow = BigCity("Moscow", population=200000)
