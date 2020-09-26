from factories.factory import ListFactory
from factories.generator import ListGenerated, ComplexGenerated

from genesys.fixtures.fixtures.place.amusement_park import first1, second2
from genesys.fixtures.fixtures.place.amusement_park import second1, first2


class BaseAmusementPark(ListGenerated):
    def __init__(self, first="", last=""):
        super().__init__()
        self.first = first
        self.last = last

    def __str__(self):
        return "{} {}".format(self.first, self.last)


class AmusementPark1(BaseAmusementPark):
    data = {
        'first': ListFactory(first1),
        'last': ListFactory(second1),
    }

    def __str__(self):
        return "{}{}".format(self.first, self.last)


class AmusementPark2(BaseAmusementPark):
    data = {
        'first': ListFactory(first2),
        'last': ListFactory(second2),
    }


class AmusementPark(ComplexGenerated):
    generators = {
        50: AmusementPark1,
        100: AmusementPark2,
    }
