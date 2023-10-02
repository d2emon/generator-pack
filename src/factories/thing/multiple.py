import random
from .delegator_factory import DelegatorFactory


class MultipleFactory(DelegatorFactory):
    """
    Generate multiple items
    """

    @property
    def min_count(self):
        return self.options.get('min_count', 1)

    @property
    def max_count(self):
        return self.options.get('max_count', None)

    def count(self):
        """Get random items count

        Returns:
            int: Random items count
        """
        if self.max_count is None:
            return self.min_count

        return random.randint(self.min_count, self.max_count)

    def build(
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

        self.logger.debug('Create %s instances of %s', count, self.factory)

        for _ in range(count):
            self.logger.debug('Create from %s', self.factory)
            self.logger.debug('\tValues %s', args)
            self.logger.debug('\tData %s', kwargs)
            yield from self.factory(
                *args,
                **kwargs,
            )

    def __call__(
        self,
        *args,
        **kwargs,
    ):
        """Build some models

        Args:
            count (int, optional): Pregenerated models count. Defaults to None.

        Yields:
            Model: Generated model
        """
        return list(self.build(*args, **kwargs))

