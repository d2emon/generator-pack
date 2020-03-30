import random
from .factory import Factory


class ListFactory(Factory):
    default_data = []

    def __init__(self, provider=None, data=None):
        super().__init__(provider)
        self.data = data

    def value(self):
        return random.choice(self.data)

    def unique(self, count=1):
        data = [*self.data]
        random.shuffle(data)
        return (item for item in data[:count])

    def __len__(self):
        return len(self.data)
