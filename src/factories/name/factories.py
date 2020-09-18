from models.models.name import Name
from sample_data import genders
from ..factory import Factory


class TextFactory(Factory):
    def model(self, group_id=None, *args, **kwargs):
        """
        Get name

        :param group_id: Name group id
        :param args: Name args
        :param kwargs: Name kwargs
        :return: Name
        """
        return Name(*self.provider.parts(group_id=group_id, **kwargs), generator=self)


class NameFactory(TextFactory):
    gender = genders.NEUTRAL

    def model(self, race_id=None, *args, **kwargs):
        """
        Get name

        :param race_id: Race id
        :param args: Name args
        :param kwargs: Name kwargs
        :return: Name
        """
        return Name(*self.provider.parts(race_id=race_id, **kwargs), generator=self)


class ListNameFactory(NameFactory):
    def model(self, gender=genders.NEUTRAL, *args, **kwargs):
        """
        Get name

        :param gender: Gender id
        :param args: Name args
        :param kwargs: Name kwargs
        :return: Name
        """
        return Name(*self.provider.get_parts(gender=gender, **kwargs), generator=self)
