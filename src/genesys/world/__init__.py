from factories.dict_factory import DictFactory
from factories.model_factory import ModelFactory
from models.world import World
from .data import DEFAULT_DATA_PROVIDER, WorldDataProvider


class WorldFactory(ModelFactory):
    def __init__(self, provider=DEFAULT_DATA_PROVIDER):
        super().__init__()

        self.factory = DictFactory(
            name=provider.names_factory(),
        )

        self.provider = provider

    @property
    def model(self):
        return World

    def get_data(self, *args, **kwargs):
        return self.factory(*args, **kwargs)
