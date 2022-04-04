import math
from models.scales import Sized as Scalable, ScalableSize as Size


class Country(Scalable):
    def __init__(self, name, size, scale=9):
        scale = (scale - 1) / 2
        size = math.sqrt(size * 10)
        super().__init__(name, Size(size, scale))


COUNTRIES = [
    Country("Vatican", 0.44, 0),
    Country("Tuvalu", .026),
    Country("Grenada", .344),
    Country("Puerto Rico", 9.104),
    Country("Israel", 28.292),
    Country("Sri Lanka", 65.610),
    Country("Nepal", 147.181),
    Country("New Zealand", 270.467),
    Country("Ecuador", 276.841),
    Country("Japan", 377.930),
    Country("Turkey", 783.562),
    Country("Colombia", 1141.748),
    Country("South Africa", 1221.037),
    Country("Niger", 1267.0),
    Country("Peru", 1285.216),
    Country("Iran", 1648.195),
    Country("Mexico", 1964.375),
    Country("Saudi Arabia", 2149.690),
    Country("Greenland", 2166.086),
    Country("Kazakhstan", 2724.9090),
    Country("Argentina", 2785.216),
    Country("India", 3287.263),
    Country("European Union", 4376.780),
    Country("Brazil", 8515.767),
    Country("Australia", 7692.024),
    Country("United States", 9525.067),
    Country("People's Republic of China", 9596.216),
    Country("Canada", 9984.670),
    Country("Antarctica", 14000),
    Country("Russia", 17098.242),
]
