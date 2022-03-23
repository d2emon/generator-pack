from v3.models.model import Model
# TODO: Resolve circular and uncomment this
# from factories.model import ModelFactory


class MarkovChain(Model):
    pass


# TODO: Resolve circular and remove this
class ModelFactory:
    pass


class MarkovFactory(ModelFactory):
    """
    Generate value from markov chain
    """

    def __init__(self, provider, max_length=32):
        super().__init__()
        self.__data = provider
        self.max_length = max_length

    @property
    def data(self):
        return self.__data

    @property
    def model_class(self):
        return MarkovChain

    def fill(self, chain):
        while len(chain) < self.max_length:
            unit = self.data[str(chain.last)]
            if unit is None:
                return
            chain.append(unit)

    def build(self, *args, **kwargs):
        """
        Get Markov chain

        :param args: Chain args
        :param kwargs: Chain kwargs
        :return: Markov chain
        """
        chain = self.model_class(*args, **kwargs)
        chain.reset()
        self.fill(chain)
        return chain
