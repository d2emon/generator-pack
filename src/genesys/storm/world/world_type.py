from factories.model_factory import ModelFactory
from models.world import WorldType
from .data import DEFAULT_DATA_PROVIDER


class WorldTypeFactory(ModelFactory):
    def __init__(self, provider=DEFAULT_DATA_PROVIDER):
        super().__init__()

        self.provider = provider

    @property
    def model(self):
        return WorldType

    def get_data(self, *args, **kwargs):
        return self.provider.world_type_factory(*args, **kwargs)
