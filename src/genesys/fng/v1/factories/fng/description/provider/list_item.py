import random


class ListItemProvider:
    def __init__(self, values=()):
        self.values = values

    def __iter__(self):
        return self

    def __next__(self):
        return random.choice(self.values)
