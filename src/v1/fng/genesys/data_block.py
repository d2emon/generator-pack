import random


class NameItem:
    def __init__(self, item_id, value):
        self.item_id = item_id
        self.value = value

    def __str__(self):
        return str(self.value)


class NameBlock:
    def __init__(self, *values):
        self.values = [NameItem(item_id, value) for item_id, value in enumerate(values)]

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.values)

    def __getitem__(self, item):
        return self.values[item]


def load_data(data):
    return {item_id: NameBlock(*values) for item_id, values in data.items()}
