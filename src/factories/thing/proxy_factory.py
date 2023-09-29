from .delegator_factory import DelegatorFactory
from .multiple import MultipleFactory
from .probable import ProbableFactory


class ProxyFactory(DelegatorFactory):
    @classmethod
    def nested(cls, factory):
        return cls(
            DelegatorFactory(factory)
        )

    def probable(self, probability=100):
        """Create child factory with probability

        Args:
            probability (int, optional): Chance to build child. Defaults to 100.

        Returns:
            Factory: Child factory
        """
        self.logger.debug('Create probable (%s%%) proxy for instance of %s', probability, self.factory)
        return self.__class__(
            ProbableFactory(self, probability=probability),
        ) 

    def multiple(self, min_items=1, max_items=None):
        """Create child factory with multiple items

        Args:
            min_count (int, optional): Minimal children count. Defaults to 1.
            max_count (int, optional): Maximal children count. Defaults to None.

        Returns:
            Factory: Child factory
        """
        self.logger.debug('Create proxy for %s-%s instances of %s', min_items, max_items, self.factory)
        return self.__class__(
            MultipleFactory(self, min_count=min_items, max_count=max_items),
        ) 

    def __call__(self, *args, **kwargs):
        self.logger.debug('Redirect call to %s', self.factory)
        self.logger.debug('\tValues %s', args)
        self.logger.debug('\tData %s', kwargs)
        yield from self.factory(
            *args,
            **kwargs,
        )
