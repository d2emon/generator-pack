from factories.factory import Factory


class MarkovFactory(Factory):
    """
    Generate value from markov chain
    """

    def __init__(self, provider=None, max_length=32):
        super().__init__(provider)
        self.max_length = max_length

    def model(self, *args, **kwargs):
        """
        Get Markov chain

        :param args: Chain args
        :param kwargs: Chain kwargs
        :return: Markov chain
        """
        chain = self.model_class(self.provider)
        chain.reset()
        while len(chain) < self.max_length:
            unit = self.provider[str(chain.last)]
            if unit is None:
                return chain
            chain.append(unit)
        return chain
