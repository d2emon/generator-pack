from factories.factory import ListFactory
from factories.generator import ListGenerated

from genesys.fixtures.fixtures import adjective
from genesys.fixtures.fixtures.place.world import noun


class World(ListGenerated):
    data = {
        'adjective': ListFactory(adjective),
        'noun': ListFactory(noun),
    }

    def __init__(self, adjective="", noun=""):
        super().__init__()
        self.adjective = adjective
        self.noun = noun

    def __str__(self):
        return "{} {}".format(self.adjective, self.noun)
