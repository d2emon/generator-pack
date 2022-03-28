import os
from config import BASE_ROOT
from factories.dict_factory import DictFactory
from factories.list_factory import ListFactory
from models.world import World
from utils.loaders import load_lines


class WorldDataProvider:
    def __init__(self, names):
        self.__names = list(names)

    @property
    def names(self):
        return self.__names

    def names_factory(self):
        return ListFactory(self.names)


DEFAULT_WORLD_DATA_PROVIDER = WorldDataProvider(
    names=load_lines(os.path.join(BASE_ROOT, 'data', 'world.txt')),
)


class WorldFactory(DictFactory):
    def __init__(self, provider=DEFAULT_WORLD_DATA_PROVIDER):
        super().__init__(
            name=provider.names_factory(),
        )
        self.provider = provider

    def __call__(self, *args, **kwargs):
        data = super().__call__(*args, **kwargs)
        return World(**data)
