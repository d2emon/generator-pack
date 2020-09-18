from factories.factory import Factory


class MarkovChain:
    def generate(self, length=32, *args, **kwargs):
        raise NotImplementedError()


class MarkovFactory(Factory):
    def __init__(self, provider=None, chain=None):
        super().__init__(provider)
        self.chain = chain or MarkovChain()

    def model(self, *args, **kwargs):
        """
        Get value from markov chain

        :param args: Chain args
        :param kwargs: Chain kwargs
        :return: Values from markov chain
        """
        return self.chain.generate(*args, **kwargs)
