from utils import genders
from .dict_data_provider import DictDataProvider


class GenderDataProvider(DictDataProvider):
    # default = {}
    data = {}

    def query(self, gender_id=genders.NEUTRAL, *args, **kwargs):
        """
        Query data

        :param gender_id: Gender id
        :param args: Query args
        :param kwargs: Query kwargs
        :return: Selected data
        """
        return self.data.get(gender_id, None)
