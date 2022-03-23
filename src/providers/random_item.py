import random
from database.data_item_database import DataItemDatabase
from .provider import ProviderFactory


class RandomItemProvider(ProviderFactory):
    def __init__(self, group_id):
        self.group_id = group_id

    def __call__(self):
        data = list(self.data)
        # random.shuffle(data)
        return random.choice(self.data) if len(self.data) else None

    @property
    def data(self):
        return DataItemDatabase.get_from_group(self.group_id)
