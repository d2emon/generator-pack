from models.models import Model
from .providers import DataProvider


class Factory:
    """
    Generate value
    """

    def __init__(self, provider=None):
        self.provider = provider or DataProvider()
        self.data = None

    @property
    def model_class(self):
        return Model

    def __iter__(self):
        """
        Factory iterator

        :return: Factory
        """
        return self

    def __next__(self):
        """
        Generate model with default params

        :return: Model
        """
        return self.model()

    def model(self, *args, **kwargs):
        """
        Generate model

        :param args: Model args
        :param kwargs: Model kwargs
        :return: Generated model
        """
        value = str(self.data)
        return value and self.model_class(
            value=value,
            # *args,
            **kwargs,
        )
