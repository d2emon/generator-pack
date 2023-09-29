import random
from .delegator_factory import DelegatorFactory


class ProbableFactory(DelegatorFactory):
    """
    Generate probable item
    """

    @property
    def probability(self):
        return self.options.get('probability', 100)

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
