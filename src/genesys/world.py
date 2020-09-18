from factories import DictFactory
from models.generator_models.world import World
from providers.file_provider import FileProvider


class WorldFactory(DictFactory):
    def __init__(self, provider=None):
        super().__init__(provider)
        self.data = {
            'name': FileProvider('data/world.txt'),
        }

    @property
    def model_class(self):
        return World
