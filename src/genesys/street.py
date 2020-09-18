from models.generator_models.street import StreetChain
from factories import MarkovFactory


class Street:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "ул. {}".format(self.name)


class StreetFactory(MarkovFactory):
    def __init__(self, provider=None):
        super().__init__(provider or StreetChain)

    def model_class(self):
        return Street

    def model(self, *args, **kwargs):
        """
        Get street from markov chain

        :param args: Chain args
        :param kwargs: Chain kwargs
        :return: Street
        """
        return self.model_class(super().model(*args, **kwargs))
