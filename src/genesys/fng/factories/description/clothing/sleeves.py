from factories.factories.list_factory import ListFactory
from genesys.fng.models.description.clothing.sleeves import Sleeves
from .belt import SleeveBandGenerator


class SleevesFactory(ListFactory):
    def __init__(self, provider):
        self.provider = provider

    def __next__(self):
        model = Sleeves()
        model.length = next(self.provider.lengths)
        model.width = next(self.provider.widths)
        model.reach = next(self.provider.reachs)
        model.decoration = next(self.provider.decorations)
        return model


class DressSleevesFactory(SleevesFactory):
    def __next__(self):
        model = Sleeves()
        model.length = next(self.provider.lengths)
        model.width = next(self.provider.widths)
        model.reach = next(self.provider.reachs)
        model.decoration = next(self.provider.decorations)
        model.change_position = next(self.provider.change_positions)
        model.change_type = next(self.provider.change_types)
        model.bands = next(SleeveBandGenerator())
        return model
