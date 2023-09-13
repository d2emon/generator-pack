from ..factory import Factory
from .multiple import MultipleFactory
from .probable import ProbableFactory


class ProxyFactory(Factory):
    def __init__(self, factory):
        super().__init__()
        self.factory = factory

    @classmethod
    def nested(cls, factory):
        def yielder(*args, **kwargs):
            yield factory(*args, **kwargs)
        
        return cls(yielder)

    def probable(self, probability=100):
        """Create child factory with probability

        Args:
            probability (int, optional): Chance to build child. Defaults to 100.

        Returns:
            Factory: Child factory
        """
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
        return self.__class__(
            MultipleFactory(self, min_count=min_items, max_count=max_items),
        ) 

    def __call__(self, *args, **kwargs):
        return self.factory(
            *args,
            **kwargs,
        )
