class DataProvider:
    pass


class OldStyleFactory:
    default_provider = DataProvider

    def __init__(self, provider=None):
        self.provider = provider or self.default_provider()

    def __call__(self, *args, **kwargs):
        raise NotImplementedError()
