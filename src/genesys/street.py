import random
from factories import MarkovFactory
from orm.models import Model, MarkovChain
from providers.markov import MarkovDataProvider
# from providers.markov import MarkovChain
from sample_data.fixtures.streets import streets


class Street(Model):
    def __init__(self, name, **fields):
        super().__init__(**fields)
        self.name = name

    def __repr__(self):
        return "ул. {}".format(self.name)


class StreetChain(MarkovChain):
    def __init__(self, data=None, length=3):
        super().__init__(data or streets, length)

    # def generate(self, length=32, *args, **kwargs):
    #     # raise NotImplementedError()


class StreetFactory(MarkovFactory):
    def __init__(self, provider=None):
        super().__init__(provider or StreetChain())

    def model_class(self):
        return Street

    def model(self, *args, **kwargs):
        """
        Get street from markov chain

        :param args: Chain args
        :param kwargs: Chain kwargs
        :return: Street
        """
        # return self.model_class(super().model(*args, **kwargs))
        return super().model(*args, **kwargs)
