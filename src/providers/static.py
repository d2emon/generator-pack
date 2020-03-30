from .provider import DataProvider


class StaticProvider(DataProvider):
    def __init__(self, value=None):
        self.value = value

    def __next__(self):
        return self.value
