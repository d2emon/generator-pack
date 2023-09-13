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
        return [*args]

    def data_factory(self, **kwargs):
        """Generates data for model

        Args:
            **kwargs: Data kwargs.

        Returns:
            dict: Data for model
        """
        return {**kwargs}

    def build(self, *args, **kwargs):
        """Create model

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Returns:
            Model: Resulting model
        """
        return self.model(*args, **kwargs)

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
        return factory(
            *self.args_factory(*args),
            **self.data_factory(**kwargs),
        )
