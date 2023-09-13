from factories.model_factory import ModelFactory
from .proxy_factory import ProxyFactory


class NestedFactory(ModelFactory):
    """
    Nested model Factory.

    Attributes:
        default_model (Model): Default model class.
        default_name (str): Default model name.
        default_children (list[Factory]): Default model children factories.

    """

    default_name = None
    default_children = []

    def children(self):
        """Children to build

        Yields:
            Factory: Child factory
        """
        yield from self.default_children

    # Factory methods

    def children_factories(self):
        """Create children factories

        Yields:
            Factory: Child factory
        """
        for factory in self.children():
            if factory is not None:
                yield from factory()

    def name_factory(self, *args, **kwargs):
        """Generate name

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Returns:
            str: Resulting name
        """
        return self.default_name

    # Inherited methods

    def args_factory(self, *args):
        """Generates args for model

        Args:
            *args: Data args.

        Returns:
            list: Args for model
        """
        if len(args) > 0:
            return super().args_factory(*args)

        return self.children_factories()

    def data_factory(self, **kwargs):
        """Generates data for model

        Args:
            **kwargs: Data kwargs.

        Returns:
            dict: Data for model
        """
        return {
            'name': self.name_factory(data=self.data),
            **kwargs,
        }

    # List generators

    @classmethod
    def one(cls):
        """Create child factory

        Returns:
            Factory: Child factory
        """
        return ProxyFactory\
            .nested(cls)

    @classmethod
    def multiple(cls, min_items=1, max_items=None):
        """Create child factory with multiple items

        Args:
            min_count (int, optional): Minimal children count. Defaults to 1.
            max_count (int, optional): Maximal children count. Defaults to None.

        Returns:
            Factory: Child factory
        """
        return ProxyFactory\
            .nested(cls)\
            .multiple(min_items, max_items)

    @classmethod
    def probable(cls, probability=100):
        """Create child factory with probability

        Args:
            probability (int, optional): Chance to build child. Defaults to 100.

        Returns:
            Factory: Child factory
        """
        return ProxyFactory\
            .nested(cls)\
            .probable(probability)
