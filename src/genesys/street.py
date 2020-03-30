from models.generator_models.street import StreetChain
from factories import MarkovFactory


class StreetFactory(MarkovFactory):
    chain_class = StreetChain

    def __repr__(self):
        return "ул. {}".format(self.name)
