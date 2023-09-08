from database.data_item_database import DataItemDatabase
from .list_factory import ListFactory


class DataItemFactory(ListFactory):
    def __init__(self, group_id):
        super().__init__()
        self.group_id = group_id

    @property
    def data(self):
        return DataItemDatabase.get_from_group(self.group_id)
