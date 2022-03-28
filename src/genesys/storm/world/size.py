import random
from factories.factory import Factory
from factories.model_factory import ModelFactory
from models.world.size import WorldSize
from .data import DEFAULT_DATA_PROVIDER


class SizeFactory(Factory):
    def __init__(
        self,
        provider=DEFAULT_DATA_PROVIDER,
        size_class=None,
    ):
        super().__init__()

        self.provider = provider
        self.size_class = size_class

    def __call__(self, *args, **kwargs):
        if self.size_class is None:
            return 0

        if self.size_class.min_size >= self.size_class.max_size:
            return self.size_class.min_size

        return random.randrange(self.size_class.min_size, self.size_class.max_size)


class SizeClassFactory(ModelFactory):
    def __init__(self, provider=DEFAULT_DATA_PROVIDER):
        super().__init__()

        self.provider = provider

    @property
    def model(self):
        return WorldSize

    def get_data(self, size_class=None, *args, **kwargs):
        if size_class is None:
            return self.provider.size_factory()
        else:
            return self.provider.find_size_class(size_class, *args, **kwargs) or {}

    def by_world_type(self, world_type, *args, **kwargs):
        size_class = random.choice(world_type.sizes) if world_type.sizes and len(world_type.sizes) > 0 else None
        return self(size_class, *args, **kwargs)

    def size_factory(self, size_class):
        size_class_data = self(size_class=size_class) if size_class is not None else None

        return SizeFactory(
            provider=self.provider,
            size_class=size_class_data,
        )
