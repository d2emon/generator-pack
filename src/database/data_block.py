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


class NameBlock:
    """
    Block of items
    """

    def __init__(self, *values):
        """
        :param values: Values for NameItems
        """
        self.values = list(values)

    def fill(self, *values, **kwargs):
        """
        :param values: Values for NameItems
        :param kwargs: Additional data for NameItems
        """
        for item_id, value in enumerate(values):
            self.values.append(NameItem(item_id, value, **kwargs))
        return self

    def get_random_id(self):
        return random.randrange(len(self.values))

    def search(self, query=lambda item: True):
        return filter(query, self.values)

    def search_values(self, **kwargs):
        return self.search(lambda item: all(item.values.get(key) == value for key, value in kwargs.items()))

    def filtered(self, **kwargs):
        return NameBlock(*self.search_values(**kwargs))

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


def load_data(data) -> dict:
    """
    Load data into dict

    :param data: Dict with data to load
    :return: Dict with NameBlocks
    """
    return {item_id: NameBlock().fill(*values) for item_id, values in data.items()}


def fill_data(**values):
    def f(blocks):
        return [
            NameItem(
                item_id=item_id,
                block_id=block_id,
                value=value,
                **values,
            )
            for block_id, items in blocks.items()
            for item_id, value in enumerate(items)
        ]
    return f
