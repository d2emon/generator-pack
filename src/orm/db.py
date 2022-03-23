from uuid import uuid4
from .data_item import DataItem


class Database:
    def __init__(self, *data):
        self.data = [{ "id": uuid4(), "value": value } for value in data]

    def find(self, condition):
        return (
            item
            for item in self.data
            if condition(item.get("value"))
        )

    def values(self):
        return [ item.get("value") for item in self.data ]

    @classmethod
    def add_to_group(cls, group_id, values):
        DataItem.add_values(group_id, values)

    @classmethod
    def get_from_group(cls, group_id):
        return DataItem.values_by_group_id(group_id)

    @classmethod
    def get_items(cls):
        return DataItem.items
