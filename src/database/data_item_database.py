from .database_loader import DatabaseLoader
from models.data_item import DataItem


class DataItemSource:
    def __init__(self, data):
        self.__data = data

    def load(self):
        for value in self.__data:
            yield {"value": value}

    def save(self, data):
        self.__data = data


class DataItemDatabase(DatabaseLoader):
    def __init__(self, *data, **config):
        super().__init__(**config)

        self.__data_items = data

    def open(self):
        """Open data source"""
        return DataItemSource(self.__data_items)

    def find(self, query):
        return (
            item
            for item in self.data
            if query(item.get("value"))
        )

    # New methods

    def values(self):
        return [ item.get("value") for item in self.data ]

    @classmethod
    def add_to_group(cls, group_id, values):
        DataItem.add_values(group_id, values)

    @classmethod
    def get_from_group(cls, group_id):
        return DataItem.values_by_group_id(group_id)
