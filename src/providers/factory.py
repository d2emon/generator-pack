from .provider import DataProvider


class FactoryProvider(DataProvider):
    def __init__(self, factory=None):
        self.factory = factory

    def __next__(self):
        return next(self.factory)
