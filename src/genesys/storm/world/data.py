from data.storm import worlds
# from factories.list_factory import ListFactory


class WorldDataProvider:
    def __init__(
        self,
        worlds=(),
        world_types=(),
        sizes=(),
        shapes=(),
    ):
        self.worlds = worlds
        self.world_types = world_types
        self.sizes = sizes
        self.shapes = shapes

    # def world_type_factory(self):
    #     return ListFactory(self.names)

    def world_type_factory(self, *args, **kwargs):
        return self.world_types.random()

    def size_factory(self, *args, **kwargs):
        return self.sizes.random()

    def shape_factory(self, *args, **kwargs):
        return self.shapes.random()

    def find_size_class(self, size_class, *args, **kwargs):
        return self.sizes.first(lambda item: item.get('size_class') == size_class)


DEFAULT_DATA_PROVIDER = WorldDataProvider(
    worlds=worlds.worlds,
    world_types=worlds.types,
    sizes=worlds.sizes,
    shapes=worlds.shapes,
)
