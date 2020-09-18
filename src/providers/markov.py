from .provider import DataProvider


class MarkovChain(DataProvider):
    def __next__(self):
        return self.generate()

    def generate(self, length=32, *args, **kwargs):
        raise NotImplementedError()
