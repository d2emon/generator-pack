from genesys.model.models.name import Name
from utils import genders
from factories.model import ModelFactory


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


class NameFactory(TextFactory):
    """
    Generate name by race
    """

    gender = genders.NEUTRAL

    def build(self, race_id=None, *args, **kwargs):
        """
        Get name

        :param race_id: Race id
        :param args: Name args
        :param kwargs: Name kwargs
        :return: Name
        """
        return self.model(race_id=race_id, **kwargs)


class ListNameFactory(NameFactory):
    """
    Generate name by gender
    """

    def build(self, gender=genders.NEUTRAL, *args, **kwargs):
        """
        Get name

        :param gender: Gender id
        :param args: Name args
        :param kwargs: Name kwargs
        :return: Name
        """
        return self.model(gender=gender, **kwargs)
