from utils import genders
from .name_factory import NameFactory


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