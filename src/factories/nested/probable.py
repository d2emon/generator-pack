import random
from .thing import ThingFactory


class ProbableFactory(ThingFactory):
    """
    Generate probable item
    """

    def __init__(
        self,
        provider=None,
        probability=100,
    ):
        """
        Probable factory constructor

        :param provider: Data providers
        :param probability: Item probability
        """
        super().__init__(provider)
        self.probability = probability

    def probable(self):
        """
        Have chance to generate

        :return: If generation is needed
        """
        if self.probability <= 0:
            return False
        if self.probability >= 100:
            return True
        return random.uniform(0, 100) <= self.probability

    def model(self, *args, **kwargs):
        """
        Get model if needed

        :param args: Model args
        :param kwargs: Model kwargs
        :return: Model
        """
        return next(super()) if self.probable() else None
