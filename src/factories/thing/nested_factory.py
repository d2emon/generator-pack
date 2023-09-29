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
        self.logger.debug('Get children factories')
        for group in self.children():
            if group is None:
                continue

            self.logger.debug('Add factories from %s', group)
            self.logger.debug('.'*8)
            factory = group()
            for children in factory:
                self.logger.debug('Add children %s', children)
                self.logger.debug('.'*4)
                for child in children:
                    self.logger.debug('Add child %s', child)
                    yield child
                self.logger.debug('.'*4)
            self.logger.debug('.'*8)

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
            self.logger.debug('Use values %s', args)
            return super().args_factory(*args)

        return self.children_factories()

    def data_factory(self, **kwargs):
        """Generates data for model

        Args:
            **kwargs: Data kwargs.

        Returns:
            dict: Data for model
        """
        data = {
            'name': self.name_factory(data=self.data),
            **kwargs,
        }
        self.logger.debug('Create data %s', data)
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
        return cls\
            .one()\
            .multiple(min_items, max_items)

    @classmethod
    def probable(cls, probability=100):
        """Create child factory with probability

        Args:
            probability (int, optional): Chance to build child. Defaults to 100.

        Returns:
            Factory: Child factory
        """
        return cls\
            .one()\
            .probable(probability)
