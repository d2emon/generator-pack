import random
from models.data_item import DataItem


class DataItemProvider:
    def __init__(self, group_id):
        self.group_id = group_id
        self.data = DataItem.get_values_by_group(self.group_id)

    def __iter__(self):
        return self

    def __next__(self):
        if not len(self.data):
            return None
        # random.shuffle(self.__data)
        return random.choice(self.data)
