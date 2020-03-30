from factories import DictFactory
from models.generator_models.world import World
from providers.file_provider import FileProvider


class WorldFactory(DictFactory):
    generated_class = World
    data = {
        'name': FileProvider('data/world.txt'),
    }
