from factories.model_factory import ModelFactory
from models.world.shape import WorldShape
from .data import DEFAULT_DATA_PROVIDER


class ShapeFactory(ModelFactory):
    default_data = DEFAULT_DATA_PROVIDER

    @property
    def model(self):
        return WorldShape

    def get_data(self, *args, **kwargs):
        return self.data.shape_factory(*args, **kwargs)
