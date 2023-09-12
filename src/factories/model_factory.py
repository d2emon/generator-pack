from models.model import Model
from .factory import Factory
from .dict_factory import DictFactory


class ModelFactory(Factory):
    """Generate model"""

    def __init__(self, data=None):
        """
        Construct factory with data from database.

        Args:
            data (Database, optional): Database for factory. Defaults to None.
        """
        super().__init__(data)
        self.data_factory = DictFactory()

    @property
    def model(self):
        """Model to build.

        Returns:
            Model: Model class
        """
        return Model

    def get_args(self, *args):
        """Generates args for model

        Args:
            *args: Data args.

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
        return self.data_factory(*args, **kwargs)

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

        model_args = [*self.get_args(*args)]
        model_kwargs = {**self.get_data(**kwargs)}

        return factory(
            *model_args,
            **model_kwargs,
        )
