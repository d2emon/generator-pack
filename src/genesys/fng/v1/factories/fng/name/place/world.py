from factories.generator import ListGenerated
from factories.generator import ListData

from sample_data.fixtures import adjective
from sample_data.fixtures.place.world import noun


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
