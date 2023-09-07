import random
from factories.model_factory import ModelFactory


class ProbableFactory(ModelFactory):
    """
    Generate probable item
    """

    def __init__(
        self,
        probability=100,
    ):
        """
        Probable factory constructor

        :param probability: Item probability
        """
        super().__init__()
        self.probability = probability

    def probable(self, probability=None):
        """
        Have chance to generate

        :param probability: Probability of model
        :return: If generation is needed
        """
        if self.probability <= 0:
            return False
        if self.probability >= 100:
            return True
        if probability is None:
            probability = random.uniform(0, 100)
        return probability <= self.probability

    def build(self, probability=None, *args, **kwargs):
        """
        Get model if needed

        :param probability: Probability of model
        :param args: Model args
        :param kwargs: Model kwargs
        :return: Model
        """
        return next(super()) if self.probable(probability) else None
