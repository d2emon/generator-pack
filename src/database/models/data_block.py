import random


class NameItem:
    """
    Name generator item
    """

    def __init__(self, item_id, value, block_id=None, **kwargs):
        """
        :param item_id: Id of item
        :param value: Item value
        """
        self.item_id = item_id
        self.block_id = block_id
        self.value = value
        self.values = kwargs

    def __str__(self):
        return str(self.value)

    def __len__(self):
        return len(str(self))
