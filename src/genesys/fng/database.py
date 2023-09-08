import random
from models.name_block import fill_data


class Database:
    def __init__(self, group_id, data):
        self.data = fill_data(group_id=group_id)(data)

    def find(self, block_id):
        items = [*self.data.search(lambda item: item.block_id == block_id)]

        def f(*args, item_id=None, **kwargs):
            if item_id is not None:
                return next((item for item in items if item.item_id == item_id), None)

            if len(items) < 1:
                return None

            return random.choice(items)

        return f
