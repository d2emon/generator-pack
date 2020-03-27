class DataProvider:
    def __iter__(self):
        return self

    def __next__(self):
        raise NotImplementedError()

    def __add__(self, other):
        return ComplexProvider(self, other)


class ComplexProvider(DataProvider):
    def __init__(self, *providers):
        self.providers = list(providers)

    def __next__(self):
        return [next(provider.items) for provider in self.providers]

    def __add__(self, other):
        return ComplexProvider(*self.providers, other)
