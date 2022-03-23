from uuid import uuid4
from database.base_database import BaseDatabase
from .data_item import DataItem


class Database(BaseDatabase):
    def __init__(self, *data):
        self.__data = [Database.output(value) for value in data]

    @property
    def data(self):
        """
        :return: Data from db
        """
        return self.__data

    def load(self):
        """
        Reload data from data file

        :return:
        """
        raise NotImplementedError()

    def save(self):
        """
        Save data for data file

        :return:
        """
        raise NotImplementedError()

    def update(self, fields):
        """
        Update record by uuid or create new record

        :param fields: Fields to update
        :return:
        """
        raise NotImplementedError()

    def find(self, condition):
        return (
            item
            for item in self.data
            if condition(item.get("value"))
        )

    def first(self, query=lambda item: True):
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
        raise self.first(lambda item: item["id"] == item_id)

    def random(self):
        """
        Get random data from db

        :return: Data
        """
        raise NotImplementedError()

    # New methods

    def values(self):
        return [ item.get("value") for item in self.data ]

    @classmethod
    def add_to_group(cls, group_id, values):
        DataItem.add_values(group_id, values)

    @classmethod
    def get_from_group(cls, group_id):
        return DataItem.values_by_group_id(group_id)

    # Transform data

    @classmethod
    def output(cls, record):
        """
        Prepare loaded record

        :param record: Record
        :return: Prepared record
        """
        return {
            "id": uuid4(),
            "value": record,
        }
