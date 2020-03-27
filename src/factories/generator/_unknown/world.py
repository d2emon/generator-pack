from factories.generator_factories import ListFactory, FileFactory
from models.generator_models.world import World


class WorldFactory(ListFactory):
    generated_class = World
    data = {
        'name': FileFactory('data/world.txt'),
    }
