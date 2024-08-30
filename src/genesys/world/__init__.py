from typing import Any
from genesys.fng.factories.name_factory import ComplexFactory
from factories.list_factory import ListFactory
from factories.model_factory import ModelFactory
from models.world import World
from .providers import DEFAULT_DATA_PROVIDER


class WorldNameFactory(ListFactory):
    def __call__(self, *args, **kwds):
        item = super().__call__(*args, **kwds)

        if item is None:
            return None

        return item.get("value")


class WorldFactory(ModelFactory):
    default_data = DEFAULT_DATA_PROVIDER
    model = World

    def __init__(self, data=None):
        super().__init__(data)

        self.__data_factory = None
        self.__name_factory = None

    @property
    def data_factory(self):
        if self.__data_factory is None:
            self.__data_factory = ComplexFactory.from_factories(
                name=self.name_factory,
            )

        return self.__data_factory

    @property
    def name_factory(self):
        if self.__name_factory is None:
            self.__name_factory = WorldNameFactory(self.data.names)

        return self.__name_factory
