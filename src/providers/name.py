from genesys.fng.providers.list_item import ListItemProvider
from sample_data import genders
from .provider import DataProvider


class TextDataProvider(DataProvider):
    # default = generator_data
    block_id = ''
    groups = ListItemProvider([])
    data = {}

    def __next__(self):
        return self.parts()

    @property
    def block(self):
        """
        Get all data from current block

        :return: Block data
        """
        return self.data.get(self.block_id, {})

    def factory(self, group_id=None):
        """
        Get factory from current block by group

        :param group_id: Factory group id
        :return: Factory
        """
        return self.block.get(group_id or next(self.groups))

    def parts(self, group_id=None, *args, **kwargs):
        """
        Next items from factories

        :param group_id: Factory group id
        :param args: Item args
        :param kwargs: Item kwargs
        :return: Generated items
        """
        return next(self.factory(group_id))


class NameDataProvider(TextDataProvider):
    block_id = 'names'
    name_group_id = 'aliens'

    @property
    def block(self):
        """
        Get all data from current block with current group id

        :return: Block data
        """
        return self.data.get(self.block_id, {}).get(self.name_group_id)

    def parts(self, race_id=None, *args, **kwargs):
        """
        Next items from factories

        :param race_id: Race id
        :param args: Item args
        :param kwargs: Item kwargs
        :return: Generated items
        """
        return [next(part) for part in self.factory(race_id)]


class DictDataProvider(NameDataProvider):
    # default = []
    data = ListItemProvider([])

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
