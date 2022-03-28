from factories.model_factory import ModelFactory
from models.world.shape import WorldShape
from .data import DEFAULT_DATA_PROVIDER


class ShapeFactory(ModelFactory):
    def __init__(self, provider=DEFAULT_DATA_PROVIDER):
        super().__init__()
        self.provider = provider

    @property
    def model(self):
        return WorldShape

    def get_data(self, *args, **kwargs):
        return self.provider.shape_factory(*args, **kwargs)
