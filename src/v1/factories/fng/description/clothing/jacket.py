from factories import ListFactory
from v1.factories.fng import Tie, Jacket
from v1.factories.fng import Material
from .sleeves import SleevesFactory


class TieFactory(ListFactory):
    def __init__(self, provider):
        self.provider = provider

    def __next__(self):
        model = Tie()
        model.description = next(self.provider.descriptions)
        model.position = next(self.provider.positions)
        return model


class JacketFactory(ListFactory):
    def __init__(self, provider):
        self.provider = provider
        self.tie_factory = TieFactory(provider.TieDataProvider)
        self.materials = map(Material, provider.materials)
        self.covers = provider.materials
        self.necklines = provider.necklines

    def __next__(self):
        model = Jacket()
        model.sleeves = next(SleevesFactory(self.provider))
        model.material = next(self.materials)
        model.cover = next(self.covers)
        model.tie = next(self.tie_factory)
        model.neckline = next(self.necklines)
        return model
