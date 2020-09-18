from models.generator_models.street import StreetChain
from factories import MarkovFactory


class Street:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "ул. {}".format(self.name)


class StreetFactory(MarkovFactory):
    def __init__(self):
        super().__init__(StreetChain)

    def model(self, *args, **kwargs):
        """
        Get street from markov chain

        :param args: Chain args
        :param kwargs: Chain kwargs
        :return: Street
        """
        return Street(super().model(*args, **kwargs))
