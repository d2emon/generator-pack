import random
from database.models.data_block import NameItem
from .model import Model


class NameBlock(Model):
    """
    Block of items
    """

    def __init__(self, values=()):
        """
        :param values: Values for NameItems
        """
        super().__init__()
        self.values = [
            *self.values,
            *values,
        ]

    def fill(self, *values, **kwargs):
        """
        :param values: Values for NameItems
        :param kwargs: Additional data for NameItems
        """
        for item_id, value in enumerate(values):
            self.values.append(NameItem(item_id, value, **kwargs))
        return self

    def get_random_id(self):
        return random.choice([item.item_id for item in self.values])

    def search(self, query=lambda item: True):
        return filter(query, self.values)

    def search_values(self, **kwargs):
        return self.search(lambda item: all(item.values.get(key) == value for key, value in kwargs.items()))

    def filtered(self, **kwargs):
        return NameBlock(self.search_values(**kwargs))

    def __iter__(self):
        return self

    def __next__(self) -> NameItem:
        """
        Get random item

        :return: Random NameItem from block
        """
        return random.choice(self.values) if len(self.values) > 0 else None

    def __getitem__(self, item_id) -> NameItem:
        """
        Get item by item_id

        :param item_id: Id of item to get
        :return: NameItem from block
        """
        return next(self.search(lambda item: item.item_id == item_id), None)

    @classmethod
    def filled(cls, *values, **kwargs):
        return cls().fill(*values, **kwargs)


def load_data(data) -> dict:
    """
    Load data into dict

    :param data: Dict with data to load
    :return: Dict with NameBlocks
    """
    return {item_id: NameBlock.filled(*values) for item_id, values in data.items()}


def fill_data(**values):
    def f(blocks):
        return NameBlock(
            NameItem(
                item_id=item_id,
                block_id=block_id,
                value=value,
                **values,
            )
            for block_id, items in blocks.items()
            for item_id, value in enumerate(items)
        )
    return f
