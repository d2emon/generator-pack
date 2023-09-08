import random
from factories.model_factory import ModelFactory


class MultipleFactory(ModelFactory):
    """
    Generate multiple items
    """

    def __init__(
        self,
        factory,
        min_count=1,
        max_count=None,
    ):
        """Constructor for ChildFactory.

        Args:
            factory (Factory): Factory to build child
            min_count (int, optional): Minimal count of items. Defaults to 1.
            max_count (int, optional): Maximal count of items. Defaults to None.
        """
        super().__init__()
        self.factory = factory
        self.min_count = min_count
        self.max_count = max_count

    def count(self):
        """Get random items count

        Returns:
            int: Random items count
        """
        if self.max_count is None:
            return self.min_count

        return random.randint(self.min_count, self.max_count)

    def __call__(
        self,
        *args,
        count=None,
        **kwargs,
    ):
        """Build some models

        Args:
            count (int, optional): Pregenerated models count. Defaults to None.

        Yields:
            Model: Generated model
        """
        if count is None:
            count = self.count()

        for _ in range(count):
            yield self.factory(
                *args,
                **kwargs,
            )
