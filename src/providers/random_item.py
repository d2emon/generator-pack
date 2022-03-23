import random
from orm.db import DataItem, Database
from .provider import DataProvider


class RandomItemProvider(DataProvider):
    def __init__(self, group_id):
        self.group_id = group_id

    def __next__(self):
        data = list(self.data)
        # random.shuffle(data)
        return random.choice(self.data) if len(self.data) else None

    @property
    def data(self):
        return Database.get_from_group(self.group_id)
