"""
Unless the kingdom is quite young, it is likely riddled with villages, a mile or two apart, covering every (farmable)
inch of the countryside. Agrarian communities on the scale of the village or hamlet exist in vast networks. The only
notable exception to this rule is frontier country, where isolated towns have no choice but to exist. But these towns
will tend to be large and walled-a people huddled together for safety. On the frontier, food and goods are usually
delivered by merchant caravans rather than produced by local agriculture. The presence of monsters would almost
certainly magnify these effects.
"""
from dice import d


MIN_POPULATION_DENSITY = 30
MAX_POPULATION_DENSITY = 120

"""
Some Historical Comparisons: Medieval France tops the list, with a 14th-century density upwards of 100 people/sq. mile.
The French were blessed with an abundance of arable countryside, waiting to be farmed. Modern France has more than
twice this many people. Germany, with a slightly less perfect climate and a lower percentage of arable land, averaged
more like 90 people/sq. mile. Italy was similar (lots of hills and rocky areas). The British Isles were the least
populous, with a little more than 40 people per square mile, most of them clustered in the southern half of the isles.
"""
DENSITY_FRANCE = 100
DENSITY_GERMANY = 90
DENSITY_ITALY = 90
DENSITY_BRITAIN = 40


# Development types
BARREN_DEVELOPMENT = 1.0
ROCKY_DEVELOPMENT = 1.5
COOL_DEVELOPMENT = 2.0
HILLY_DEVELOPMENT = 3.0
ARABLE_DEVELOPMENT = 4.0
IDYLLIC_DEVELOPMENT = 5.0

DEFAULT_DEVELOPMENT = HILLY_DEVELOPMENT


descriptions = {
    BARREN_DEVELOPMENT: "Barren, Desolate",
    ROCKY_DEVELOPMENT: "Rocky, Chilly",
    COOL_DEVELOPMENT: "Cool, Dry; Swampy",
    HILLY_DEVELOPMENT: "Hilly, Temperate",
    ARABLE_DEVELOPMENT: "Abundant Arable Land",
    IDYLLIC_DEVELOPMENT: "Fertile, Warm, Idyllic",
}


def generate_density(development=DEFAULT_DEVELOPMENT):
    """
    The average population density for a fully-developed medieval country is from 30 per square mile (for countries
    with lots of rocks, lots of rain, and lots of ice-or a slave-driving Mad King) to a limit of about 120 per square
    mile, for a land with rich soil, favorable seasons and maybe a touch of magical help. No land is wasted if it can
    be settled and farmed. There are many factors that determine the population density of a land, but none as
    important as arability and climate. If food will grow, so will peasants. If desired, exact density can be rolled
    randomly, and land arability reverse-engineered from the result. A roll of 6d4x5 will do the trick nicely. Reduce
    the x5 multiple by any amount down to x1 to represent a much less developed land, or to represent countries
    depopulated by invasions, plagues or other calamities. Nations hit by such troubles can stay depopulated for
    centuries, too, barring an influx of immigrants: natural population growth is usually glacial in pre-industrial
    worlds.

    :param development: development of land from 5 (highly populated) to 1 (depopulated)
    :return:
    """
    return d(6, 4) * development
