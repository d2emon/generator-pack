import random
from data.storm import worlds
from factories.db_factory import DbFactory
from models.world.size import WorldSize


class SizeFactory(DbFactory):
    def __init__(self, size_class=None):
        super().__init__(WorldSize, worlds.sizes)
        self.size_class = size_class

    def by_class(self, size_class):
        return self.first(lambda item: item.get('size_class') == size_class)

    def set_size_class(self, size_class):
        if size_class is None:
            return
        self.size_class = self.by_class(size_class)

    def __call__(self, *args, **kwargs):
        if self.size_class is None:
            return 0

        if self.size_class.min_size >= self.size_class.max_size:
            return self.size_class.min_size

        return random.randrange(self.size_class.min_size, self.size_class.max_size)