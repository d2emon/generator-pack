from .provider import ProviderFactory


class StaticProvider(ProviderFactory):
    def __init__(self, value=None):
        self.value = value

    def __call__(self):
        return self.value
