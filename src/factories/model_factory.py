from models.model import Model
from .factory import Factory


class ModelFactory(Factory):
    """
    Generate model
    """
    @property
    def model(self):
        return Model

    def get_data(self, *args, **kwargs):
        return {}

    def __call__(self, *args, **kwargs):
        """
        Generate model

        :param args: Model args
        :param kwargs: Model kwargs
        :return: Generated model
        """
        return self.model(**self.get_data(*args, **kwargs))
