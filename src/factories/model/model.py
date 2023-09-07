# from orm.models import Model
from factories.factory import Factory


class ModelFactory(Factory):
    """
    Generate model
    """
    @property
    def model_class(self):
        # return Model
        raise NotImplementedError()

    def __call__(self, *args, **kwargs):
        """
        Generate model

        :param args: Model args
        :param kwargs: Model kwargs
        :return: Generated model
        """
        return self.model_class(**kwargs)
