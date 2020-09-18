from factories import DictFactory
from models.generator_models.world import World
from providers.file_provider import FileProvider


class WorldDataProvider:
    @classmethod
    def name(cls):
        return FileProvider('data/world.txt')


class WorldFactory(DictFactory):
    def __init__(self, provider=None):
        super().__init__(provider)
        self.data = {
            'name': self.provider.name,
        }

    @property
    def model_class(self):
        return World
