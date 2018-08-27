"""
Chamlek is an island kingdom with a total land area of 88,700 square miles, with a good climate and only a few rocky
hills disturbing a well-watered countryside. Her population is just over 6.6 million, with an average density of about
75 people per square mile (an average roll of the dice using the recommended range for a developed land).

Using average rolls for city sizes and town spreads, we can determine the following about Chamlek: It's largest city,
Restagg, has a population of 39,000. The next-ranking major cities are Volthyrm (19,000), McClannach (15,000),
Cormidigar (11,000), and Oberthrush (8,000). There are 5 cities and 45 towns all told, with a total urban population of
just over 200,000 (about 3% of the kingdom). The rest is rural - there's approximately 1 urban center for every 1,800
square miles. If we used the early-medieval method of continuing the city scheme to determine the towns, there'd be
only 7 towns (one urban center every 7,500 square miles).
"""
from .city import BigCity, City, Town, Village


class Kingdom:
    def __init__(self, area=50000, density=75, population=6600000, settlements=[]):
        self.area = area
        self.density = density
        self.population = population
        self.settlements = settlements


Chamlek = Kingdom(
    area=88700,
    density=75,
    population=6600000,
    settlements=[
        BigCity("Restagg", 39000),
        City("Volthyrm", 19000),
        City("McClannach", 15000),
        City("Cormidigar", 11000),
        City("Oberthrush", 8000),
    ] + [Town.generate("Town") for _ in range(45)],
)
