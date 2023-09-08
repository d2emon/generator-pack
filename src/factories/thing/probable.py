import random
from factories.model_factory import ModelFactory


class ProbableFactory(ModelFactory):
    """
    Generate probable item
    """

    def __init__(
        self,
        factory,
        probability=100,
    ):
        """Constructor for ChildFactory.

        Args:
            factory (Factory): Factory to build child
            probability (int, optional): Chance to build child. Defaults to 100.
        """
        super().__init__()
        self.factory = factory
        self.probability = probability

    def probable(self, probability=None):
        """Check if need to build model

        Args:
            probability (int, optional): Pregenersted chance to build model. Defaults to None.

        Returns:
            bool: Need to build model
        """
        if self.probability <= 0:
            return False

        if self.probability >= 100:
            return True

        if probability is None:
            probability = random.uniform(0, 100)

        return probability <= self.probability

    def __call__(
        self,
        *args,
        probability=None,
        **kwargs,
    ):
        """Build model with chance

        Args:
            probability (int, optional): Pregenerated chance to build model. Defaults to None.

        Yields:
            Model: Generated model
        """
        if not self.probable(probability):
            return

        yield self.factory(
            *args,
            **kwargs,
        )
