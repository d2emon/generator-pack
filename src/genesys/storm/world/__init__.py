from factories.dict_factory import DictFactory
from factories.model_factory import ModelFactory
from genesys.storm.world.shape import ShapeFactory
from models.world import World
from .size import SizeFactory, SizeClassFactory
from .world_type import WorldTypeFactory
from .data import DEFAULT_DATA_PROVIDER, WorldDataProvider


class WorldFactory(ModelFactory):
    def __init__(self, provider=DEFAULT_DATA_PROVIDER):
        super().__init__()

        self.provider = provider
        self.factory = DictFactory(
            # name=provider.names_factory(),
            world_type=WorldTypeFactory(),
            shape=ShapeFactory(),
            # world_size=SizeFactory(),
        )
        self.size_class_factory = SizeClassFactory(provider)
        self.world_size_factory = SizeFactory

    @property
    def model(self):
        return World

    def get_data(self, *args, **kwargs):
        data = self.factory(*args, **kwargs)

        world_type = data.get('world_type')
        size_class = data.get('size_class')
        world_size = data.get('world_size')

        if size_class is None:
            size_class = self.size_class_factory.by_world_type(world_type)

        if world_size is None:
            world_size_factory = self.world_size_factory(size_class=size_class)
            world_size = world_size_factory()

        data['size_class'] = size_class
        data['world_size'] = world_size

        return data
