from factories.factory import Factory


class MarkovFactory(Factory):
    """
    Generate value from markov chain
    """

    def model(self, *args, **kwargs):
        """
        Get value from markov chain

        :param args: Chain args
        :param kwargs: Chain kwargs
        :return: Values from markov chain
        """
        return self.provider.generate(*args, **kwargs)
