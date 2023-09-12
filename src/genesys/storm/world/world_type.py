from factories.model_factory import ModelFactory
from models.world import WorldType
from .data import DEFAULT_DATA_PROVIDER


class WorldTypeFactory(ModelFactory):
    default_data = DEFAULT_DATA_PROVIDER

    @property
    def model(self):
        return WorldType

    def get_data(self, *args, **kwargs):
        return self.data.world_type_factory(*args, **kwargs)
