from utils import genders
from .text_factory import TextFactory


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
