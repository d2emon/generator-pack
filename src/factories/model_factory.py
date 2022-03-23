from models.model import Model
from .factory import Factory


class ModelFactory(Factory):
    """
    Generate model
    """
    def __init__(self, data=()):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @property
    def model_class(self):
        return Model

    def __call__(self, *args, **kwargs):
        """
        Generate model

        :param args: Model args
        :param kwargs: Model kwargs
        :return: Generated model
        """
        return self.model_class(**kwargs)
