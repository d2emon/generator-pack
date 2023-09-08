from utils import genders
from factories.list_factory import ListFactory
from .name_data_provider import NameDataProvider


class DictDataProvider(NameDataProvider):
    # default = []
    data = ListFactory()

    def query(self, *args, **kwargs):
        """
        Query data

        :param args: Query args
        :param kwargs: Query kwargs
        :return: Selected data
        """
        return self.data

    def parts(self, gender_id=genders.NEUTRAL, *args, **kwargs):
        """
        Next items from factories

        :param gender_id: Gender id
        :param args: Item args
        :param kwargs: Item kwargs
        :return: Generated items
        """
        data = self.query(gender_id=gender_id, *args, **kwargs)
        return next(data) if data is not None else []
