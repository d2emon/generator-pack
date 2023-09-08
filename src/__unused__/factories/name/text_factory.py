from factories.model_factory import ModelFactory
from models.name_model import Name


class TextFactory(ModelFactory):
    """
    Generate name from data
    """
    def __init__(self, provider):
        super().__init__()
        self.__data = provider

    @property
    def model_class(self):
        return Name

    @property
    def data(self):
        return self.__data

    def model(self, **kwargs):
        return self.model_class(*self.data.parts(**kwargs), generator=self)

    def build(self, group_id=None, *args, **kwargs):
        """
        Get name

        :param group_id: Name group id
        :param args: Name args
        :param kwargs: Name kwargs
        :return: Name
        """
        return self.model(group_id=group_id, **kwargs)