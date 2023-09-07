from models.model import Model
from .factory import Factory


class ModelFactory(Factory):
    """Generate model"""

    @property
    def model(self):
        """Model to build.

        Returns:
            Model: Model class
        """
        return Model

    def get_args(self, *args, **kwargs):
        """Generates args for model

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Returns:
            list: Args for model
        """
        return [*args]

    def get_data(self, *args, **kwargs):
        """Generates data for model

        Args:
            *args: Data args.
            **kwargs: Data kwargs.

        Returns:
            dict: Data for model
        """
        return {**kwargs}

    def model_factory(self, *args, **kwargs):
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
        model_factory = model or self.model_factory

        model_args = self.get_args(*args)
        model_kwargs = self.get_data(**kwargs)

        return model_factory(
            *list(model_args),
            **model_kwargs,
        )
