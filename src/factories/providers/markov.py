from .provider import DataProvider


class MarkovChain(DataProvider):
    def generate(self, length=32, *args, **kwargs):
        raise NotImplementedError()
