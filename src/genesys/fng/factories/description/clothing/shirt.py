from factories.factories.list_factory import ListFactory
from genesys.fng.models.description.clothing.shirt import Shirt
from .sleeves import SleevesFactory


class ShirtFactory(ListFactory):
    def __init__(self, provider):
        self.provider = provider

    def __next__(self):
        model = Shirt()
        model.style = next(self.provider.styles)
        model.sleeves = next(SleevesFactory(self.provider))
        return model
