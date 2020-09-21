from orm.models import Model
from .factory import Factory


class ModelFactory(Factory):
    """
    Generate model
    """
    @property
    def data(self):
        raise NotImplementedError()

    @property
    def model_class(self):
        return Model

    def build(self, *args, **kwargs):
        """
        Generate model

        :param args: Model args
        :param kwargs: Model kwargs
        :return: Generated model
        """
        return self.model_class(**kwargs)
