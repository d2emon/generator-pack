import random
from data.storm import worlds
from models.world import World
from .db import DbFactory
from .size import SizeFactory
from .world_type import WorldTypeFactory


class WorldFactory(DbFactory):
    def __init__(self):
        super().__init__(World, worlds.worlds)
        self.world_type_factory = WorldTypeFactory()

    @classmethod
    def get_size_class(cls, world_type):
        return random.choice(world_type.sizes) if world_type.sizes and len(world_type.sizes) > 0 else None

    def get_data(self, **kwargs):
        size_factory = SizeFactory()

        world_type = kwargs.get('world_type') or self.world_type_factory()
        size_factory.set_size_class(kwargs.get('size_class') or self.get_size_class(world_type))
        world_size = kwargs.get('world_size') or size_factory()

        data = {}
        data.update({
            'world_type': world_type,
            'size_class': size_factory.size_class,
            'world_size': world_size,
        })
        data.update(kwargs)
        print(data)
        return data

    def __call__(self, *args, **kwargs):
        data = self.get_data(**kwargs)
        return World(*args, **data)
