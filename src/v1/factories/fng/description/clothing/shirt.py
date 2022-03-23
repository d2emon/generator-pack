from factories.list_factory import ListFactory
from v1.factories.fng import Shirt
from .sleeves import SleevesFactory


class ShirtFactory(ListFactory):
    def __init__(self, provider):
        self.provider = provider

    def __next__(self):
        model = Shirt()
        model.style = next(self.provider.styles)
        model.sleeves = next(SleevesFactory(self.provider))
        return model
