import random
from .database import BaseDatabase


class ArrayDatabase(BaseDatabase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

    @property
    def data(self):
        raise NotImplementedError()

    def insert(self, fields):
        """
        Save data for data file

        :return:
        """
        self.data.append(fields)

    def replace(self, item_id, fields):
        """
        Save data for data file

        :return:
        """
        for item in self.find(lambda i: self.get_item_id(i) == item_id):
            item.update(fields)

    def find(self, query):
        """
        Get all data from db

        :param query: Db query
        :return: Filtered data
        """
        return filter(query, self.data)

    def first(self, query):
        """
        Get first data from db

        :param query: Db query
        :return: Data
        """
        return next(self.find(query), None)

    def get(self, item_id):
        """
        Get item by uuid

        :param item_id: uuid
        :return: Data
        """
        return self.first(lambda item: self.get_item_id(item) == item_id)

    def random(self):
        """
        Get random data from db

        :return: Data
        """
        items = list(self.all())
        return random.choice(items) if len(items) > 0 else None
