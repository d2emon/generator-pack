from genesys.fng.factories.name_factory import ComplexFactory
from factories.list_factory import ListFactory
from factories.model_factory import ModelFactory
from models.world import World
from .providers import DEFAULT_DATA_PROVIDER


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
        def create_name_factory():
            factory = ListFactory(self.data.names)

            def __factory():
                item = factory()
                if item is None:
                    return None
                return item.get("value")

            return __factory

        if self.__name_factory is None:
            self.__name_factory = create_name_factory()

        return self.__name_factory
