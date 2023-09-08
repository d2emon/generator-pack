import random
from factories.factory import Factory
from factories.model_factory import ModelFactory
from models.model import Model
from .multiple import MultipleFactory
from .probable import ProbableFactory


class ProxyFactory(Factory):
    def __init__(self, factory):
        super().__init__()
        self.factory = factory

    def probable(self, probability=100):
        """Create child factory with probability

        Args:
            probability (int, optional): Chance to build child. Defaults to 100.

        Returns:
            Factory: Child factory
        """
        return ProbableFactory(self, probability=probability)

    def multiple(self, min_items=1, max_items=None):
        """Create child factory with multiple items

        Args:
            min_count (int, optional): Minimal children count. Defaults to 1.
            max_count (int, optional): Maximal children count. Defaults to None.

        Returns:
            Factory: Child factory
        """
        return MultipleFactory(self, min_count=min_items, max_count=max_items)

    def __call__(self, *args, **kwargs):
        return self.factory(*args, **kwargs)


class NestedFactory(ModelFactory):
    """
    Nested model Factory.

    Attributes:
        default_model (Model): Default model class.
        default_name (str): Default model name.
        default_children (list[Factory]): Default model children factories.

    """

    default_model = Model
    default_name = None
    default_children = []

    def __init__(self, provider=None, *args, **kwargs):
        """Creates nested factory

        Args:
            provider (Provider, optional): Data provider for factory. Defaults to None.
        """
        self.provider = provider

    def children(self):
        """Children to build

        Yields:
            Factory: Child factory
        """
        yield from self.default_children

    # Factory methods

    def children_factories(self, *args, **kwargs):
        """Create children factories

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Yields:
            Factory: Child factory
        """
        for child_factory in self.children():
            if child_factory is not None:
                yield from child_factory()

    def model_factory(self, *children, **kwargs):
        """Create model

        Args:
            *children: Data args.
            **kwargs: Data kwargs.

        Returns:
            Model: Resulting model
        """
        return self.model(*children, **kwargs)

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

    @property
    def model(self):
        """Model to build.

        Returns:
            Model: Model class
        """
        return self.default_model

    def get_args(self, *args, **kwargs):
        """Generates args for model

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Returns:
            list: Args for model
        """
        if len(args) > 0:
            return [*args]

        return self.children_factories()

    def get_data(
        self,
        **kwargs,
    ):
        """Generates data for model

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Returns:
            dict: Data for model
        """
        return {
            'name': self.name_factory(provider=self.provider),
            **kwargs,
        }

    # Helper methods

    @classmethod
    def proxy(cls):
        """Create child factory

        Returns:
            Factory: Child factory
        """
        return ProxyFactory(cls)

    @classmethod
    def probable(cls, probability=100):
        """Create child factory with probability

        Args:
            probability (int, optional): Chance to build child. Defaults to 100.

        Returns:
            Factory: Child factory
        """
        return cls.proxy().probable(probability)

    @classmethod
    def multiple(cls, min_items=1, max_items=None):
        """Create child factory with multiple items

        Args:
            min_count (int, optional): Minimal children count. Defaults to 1.
            max_count (int, optional): Maximal children count. Defaults to None.

        Returns:
            Factory: Child factory
        """
        return cls.proxy().multiple(min_items, max_items)

    @classmethod
    def as_child(cls, min_count=1, max_count=None, probability=100):
        """Create child factory

        Args:
            min_count (int, optional): Minimal children count. Defaults to 1.
            max_count (int, optional): Maximal children count. Defaults to None.
            probability (int, optional): Chance to build child. Defaults to 100.

        Returns:
            Factory: Child factory
        """
        # TODO: Remove it
        return cls.proxy()\
            .probable(probability)\
            .multiple(min_count, max_count)

    @classmethod
    def select_item(cls, *items):
        """Get random item from list

        Args:
            *items: Data items.

        Returns:
            _type_: _description_
        """
        # TODO: Remove it
        return random.choice(items) if len(items) else None
