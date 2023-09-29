from models.model import Model
from .factory import Factory
from .dict_factory import DictFactory


class ModelFactory(Factory):
    """Generate model"""

    default_model = Model

    @property
    def model(self):
        """Model to build.

        Returns:
            Model: Model class
        """
        return self.default_model

    def args_factory(self, *args):
        """Generates args for model

        Args:
            *args: Data args.

        Returns:
            list: Args for model
        """
        self.logger.debug('Use values %s', args)

        return [*args]

    def data_factory(self, **kwargs):
        """Generates data for model

        Args:
            **kwargs: Data kwargs.

        Returns:
            dict: Data for model
        """
        self.logger.debug('Use data %s', kwargs)

        return {**kwargs}

    def build(self, *args, **kwargs):
        """Create model

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Returns:
            Model: Resulting model
        """
        self.logger.debug('-'*20)
        self.logger.debug('Build model %s', self.model)
        self.logger.debug('\tFactory: %s', self)
        self.logger.debug('\tValues: %s', args)
        self.logger.debug('\tData: %s', kwargs)

        result = self.model(*args, **kwargs)
        self.logger.debug('Result: %s', result)
        self.logger.debug('-'*20)

        return result

    def __call__(
        self,
        *args,
        model=None,
        **kwargs,
    ):
        """Generate model

        Args:
            *args: Model args.
            model (Model): Model factory. Defaults to None.
            **kwargs: Model kwargs.

        Returns:
            Model: Generated model
        """
        factory = model or self.build

        self.logger.debug('='*20)
        self.logger.debug('With %s', self)
        self.logger.debug('Build %s', factory)
        self.logger.debug('-'*20)

        result = factory(
            *self.args_factory(*args),
            **self.data_factory(**kwargs),
        )

        self.logger.debug('Result: %s', result)
        self.logger.debug('='*20)

        return result
