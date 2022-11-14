from factories.list_factory import ListFactory
from genesys.fixtures.fixtures import adjective
from genesys.fixtures.fixtures.place.world import noun
from models.fng.names.name import Name


class World(Name):
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
