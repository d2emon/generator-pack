import os
from config import BASE_ROOT
from factories.list_factory import ListFactory
from utils.loaders import load_lines


class WorldDataProvider:
    def __init__(self, names):
        self.__names = list(names)

    @property
    def names(self):
        return self.__names

    def names_factory(self):
        return ListFactory(self.names)


DEFAULT_DATA_PROVIDER = WorldDataProvider(
    names=load_lines(os.path.join(BASE_ROOT, 'data', 'world.txt')),
)
