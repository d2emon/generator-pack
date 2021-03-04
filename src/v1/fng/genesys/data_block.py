import random


class NameItem:
    """
    Name generator item
    """

    def __init__(self, item_id, value):
        """
        :param item_id: Id of item
        :param value: Item value
        """
        self.item_id = item_id
        self.value = value

    def __str__(self):
        return str(self.value)


class NameBlock:
    """
    Block of items
    """

    def __init__(self, *values):
        """
        :param values: Values for NameItems
        """
        self.values = [NameItem(item_id, value) for item_id, value in enumerate(values)]

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
        return self.values[item_id]


def load_data(data) -> dict:
    """
    Load data into dict

    :param data: Dict with data to load
    :return: Dict with NameBlocks
    """
    return {item_id: NameBlock(*values) for item_id, values in data.items()}
