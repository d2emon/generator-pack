import random
from database.data_block import fill_data


class Database:
    def __init__(self, group_id, data):
        self.data = fill_data(group_id=group_id)(data)

    def __block(self, block_id):
        return [item for item in self.data if item.block_id == block_id]

    @classmethod
    def __get_value(cls, f):
        def wrapped(*args, **kwargs):
            item = f(*args, **kwargs)

            if item is None:
                return None

            return item.get('value')

        return wrapped

    def find(self, block_id):
        items = self.__block(block_id)

        def f(*args, item_id=None, **kwargs):
            if item_id is not None:
                return next(item for item in items if item.item_id == item_id)

            return random.choice(items)

        return f
