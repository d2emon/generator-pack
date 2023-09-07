import random
from .factory import Factory


class ChildFactory(Factory):
    """Generate nested value"""

    def __init__(
        self,
        factory_class,
        min_count=1,
        max_count=None,
        probability=100,
    ):
        """Constructor for ChildFactory.

        Args:
            factory_class (Factory): Factory to build child
            min_count (int, optional): Minimal children count. Defaults to 1.
            max_count (int, optional): Maximal children count. Defaults to None.
            probability (int, optional): Chance to build child. Defaults to 100.
        """
        self.factory_class = factory_class
        self.min_count = min_count
        self.max_count = max_count
        self.probability = probability

    @classmethod
    def get_probability(cls, probability=100):
        """Check if need to build child

        Args:
            probability (int, optional): Chance to build result. Defaults to 100.

        Returns:
            bool: If need to build child
        """
        if probability >= 100:
            return True

        return random.uniform(0, 100) < probability

    @classmethod
    def get_count(cls, min_count=1, max_count=None):
        """Get random children count

        Args:
            min_count (int, optional): Minimal children count. Defaults to 1.
            max_count (int, optional): Maximal children count. Defaults to None.

        Returns:
            int: Random children count
        """
        if max_count is None:
            return min_count
        
        return random.randint(min_count, max_count)

    def __call__(
        self,
        provider=None,
    ):
        """Generate child

        Args:
            provider (_type_, optional): Data provider for child. Defaults to None.

        Yields:
            Any: Generated child
        """
        if not self.get_probability(self.probability):
            return

        count = self.get_count(min_count=self.min_count, max_count=self.max_count)
        for _ in range(count):
            yield self.factory_class(
                provider=provider,
            )
