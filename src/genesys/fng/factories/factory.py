class Factory:
    class DataProvider:
        pass

    def __init__(self, provider=None):
        self.provider = provider or self.DataProvider()

    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError()
