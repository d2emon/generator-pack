import os
from factories import DictFactory
from models.world import World
from factories.list_factory import ListFactory


class WorldDataProvider:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


DEFAULT_WORLD_DATA_PROVIDER = WorldDataProvider(
    ListFactory.from_text_file(os.path.join('data', 'world.txt'))
)


"""
class WorldFactory(DictFactory):
    def __init__(self, provider=DEFAULT_WORLD_DATA_PROVIDER):
        super().__init__(provider)

        self.data = {
            'name': self.provider.name,
        }

    @property
    def model_class(self):
        return World
"""
