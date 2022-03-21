import random


class ProviderQuery:
    def __init__(self, data):
        self.data = data
        self.__values = None

    @property
    def values(self):
        if self.__values is None:
            self.__values = list(self.data)

        return list(self.__values)

    def random_item(self):
        values = self.values
        return random.choice(values) if len(values) > 0 else None

    def filter(self, condition):
        return self.__class__(filter(condition, self.values))
