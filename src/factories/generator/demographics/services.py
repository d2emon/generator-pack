"""
In a village of 400 people, just how many inns and taverns are realistic? Not very many. Maybe not even one. When
traveling across the countryside, characters should not run into a convenient sign saying "Motel: Free Cable and
Swimming Pool" every 3 leagues. For the most part, they will have to camp on their own or seek shelter in people's
homes.

Provided they are friendly, the latter option should be no trouble. A farmer can live in a single place all his life,
and he will welcome news and stories of adventures, not to mention any money the heroes might offer!
"""
import random


def round_or_percent(percent):
    if percent < 1:
        return "{}%".format(round(percent * 100))
    return round(percent)


class Service:
    """
    Each type of business is given a Support Value (SV). This is the number of people it takes to support a single
    business of that sort. For instance, the SV for spice merchants is 1,400. This means that there will be one spice
    merchant for every 1,400 people in an area. This can vary by up to 60% in either direction, but provide a useful
    baseline for GMs (the top spots are even more variable as they'll depend on the industries the town specializes in;
    medieval Paris, the model for this list and a fantastic model for any fantasy city, was a shoemaking center). Think
    about the nature of the town or city to decide which numbers to change. A port, for instance, will have more
    fishmongers.
    """
    def __init__(self, name="Service", sv=1):
        self.name = name
        self.sv = sv

    def count(self, population=1000):
        """
        To find the number of, say, inns in a city, divide the population of the city by the SV value for inns (2,000).
        For a village of 400 people, this reveals only 20% of an inn! This means that there is a 20% chance of there
        being one at all. And even if there is one, it will be smaller and less impressive than an urban inn. The SV
        for taverns is 400, so there will be a single tavern.

        :param population:
        :return:
        """
        modifier = self.sv * random.randint(-60, 60) / 100
        sv = self.sv + modifier
        count = population / sv
        res = int(count)
        roll = random.randrange(100) / 100
        if roll < (count - res):
            res += 1
        return res

    def __repr__(self):
        return "<{}>".format(self.name)


"""
Business       	    SV	    Business	    SV
Shoemakers      	150	    Butchers	    1,200
Furriers    	    250	    Fishmongers	    1,200
Maidservants    	250	    Beer-Sellers	1,400
Tailors	            250	    Buckle Makers	1,400
Barbers	            350	    Plasterers	    1,400
Jewelers	        400	    Spice Merchants	1,400
Taverns/Restaurants	400	    Blacksmiths	    1,500
Old-Clothes 	    400	    Painters	    1,500
Pastrycooks	        500	    Doctors	        1,700*
Masons	            500	    Roofers	        1,800
Carpenters  	    550	    Locksmiths	    1,900
Weavers	            600	    Bathers	        1,900
Chandlers	        700	    Ropemakers	    1,900
Mercers	            700	    Inns	        2,000
Coopers	            700	    Tanners	        2,000
Bakers	            800	    Copyists	    2,000
Watercarriers   	850	    Sculptors	    2,000
Scabbardmakers	    850	    Rugmakers	    2,000
Wine-Sellers    	900	    Harness-Makers	2,000
Hatmakers	        950	    Bleachers	    2,100
Saddlers	        1,000	Hay Merchants	2,300
Chicken Butchers	1,000	Cutlers	        2,300
Pursemakers 	    1,100	Glovemakers	    2,400
Woodsellers	        2,400	Woodcarvers	    2,400
Magic-Shops	        2,800	Booksellers	    6,300
Bookbinders	        3,000	Illuminators	3,900
*These are licensed doctors. Total doctor SV is 350.


Some other figures: There will be one noble household per 200 population, one lawyer ("advocate") per 650, one
clergyman per 40 and one priest per 25-30 clergy.

Businesses not listed here will most likely have an SV from 5,000 to 25,000! The "Magic Shop" means a shop where
wizards can purchase spell ingredients, scroll paper and the like, not a place to buy magic swords off the shelf.
"""
SERVICES = [
    Service("Shoemakers", 150),
    Service("Furriers", 250),
    Service("Maidservants", 250),
    Service("Tailors", 250),
    Service("Barbers", 350),
    Service("Jewelers", 400),
    Service("Taverns/Restaurants", 400),
    Service("Old-Clothes", 400),
    Service("Pastrycooks", 500),
    Service("Masons", 500),
    Service("Carpenters", 550),
    Service("Weavers", 600),
    Service("Chandlers", 700),
    Service("Mercers", 700),
    Service("Coopers", 700),
    Service("Bakers", 800),
    Service("Watercarriers", 850),
    Service("Scabbardmakers", 850),
    Service("Wine-Sellers", 900),
    Service("Hatmakers", 950),
    Service("Saddlers", 1000),
    Service("Chicken Butchers", 1000),
    Service("Pursemakers", 1100),
    Service("Woodsellers", 2400),
    Service("Magic-Shops", 2800),
    Service("Bookbinders", 3000),
    Service("Butchers", 1200),
    Service("Fishmongers", 1200),
    Service("Beer-Sellers", 1400),
    Service("Buckle Makers", 1400),
    Service("Plasterers", 1400),
    Service("Spice Merchants", 1400),
    Service("Blacksmiths", 1500),
    Service("Painters", 1500),
    Service("Doctors", 1700),
    Service("Roofers", 1800),
    Service("Locksmiths", 1900),
    Service("Bathers", 1900),
    Service("Ropemakers", 1900),
    Service("Inns", 2000),
    Service("Tanners", 2000),
    Service("Copyists", 2000),
    Service("Sculptors", 2000),
    Service("Rugmakers", 2000),
    Service("Harness-Makers", 2000),
    Service("Bleachers", 2100),
    Service("Hay Merchants", 2300),
    Service("Cutlers", 2300),
    Service("Glovemakers", 2400),
    Service("Woodcarvers", 2400),
    Service("Booksellers", 6300),
    Service("Illuminators", 3900),

    Service("Noble", 200),
    Service("Lawyer", 650),
]
clergy = Service("Clergyman", 40)


class Priest(Service):
    def __init__(self, name="Priest"):
        sv = random.randint(25, 30)
        super().__init__(name, sv)


def populate(population):
    res = []
    for service in SERVICES:
        res += [service] * service.count(population)

    clergy_count = clergy.count(population)
    res += [clergy] * clergy_count

    priest = Priest()
    priest_count = priest.count(clergy_count)
    res += [priest] * priest_count

    return res


def populate_services(population):
    services = {s.name: round_or_percent(population / s.sv) for s in SERVICES}
    services[clergy.name] = round_or_percent(population / clergy.sv)

    priests = Priest()
    services[priests.name] = round_or_percent(services[clergy.name] / priests.sv)
    return services
