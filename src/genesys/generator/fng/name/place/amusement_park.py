from genesys.generator import ListGenerated, ComplexGenerated
from genesys.generator import ListData

from fixtures.place.amusement_park.first1 import first1
from fixtures.place.amusement_park import first2, second1, second2


class BaseAmusementPark(ListGenerated):
    def __init__(self, first="", last=""):
        super().__init__()
        self.first = first
        self.last = last

    def __str__(self):
        return "{} {}".format(self.first, self.last)


class AmusementPark1(BaseAmusementPark):
    data = {
        'first': ListData(first1),
        'last': ListData(second1),
    }

    def __str__(self):
        return "{}{}".format(self.first, self.last)


class AmusementPark2(BaseAmusementPark):
    data = {
        'first': ListData(first2),
        'last': ListData(second2),
    }


class AmusementPark(ComplexGenerated):
    generators = {
        50: AmusementPark1,
        100: AmusementPark2,
    }
