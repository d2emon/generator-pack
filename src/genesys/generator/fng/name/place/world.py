from genesys.generator import ListGenerated
from genesys.generator import ListData

from fixtures.place.world.adjective import adjective
from fixtures.place.world import noun


class World(ListGenerated):
    data = {
        'adjective': ListData(adjective),
        'noun': ListData(noun),
    }

    def __init__(self, adjective="", noun=""):
        super().__init__()
        self.adjective = adjective
        self.noun = noun

    def __str__(self):
        return "{} {}".format(self.adjective, self.noun)
