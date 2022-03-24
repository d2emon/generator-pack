from data.storm import worlds
from factories.db_factory import DbFactory
from models.world import WorldType


class WorldTypeFactory(DbFactory):
    def __init__(self):
        super().__init__(WorldType, worlds.types)

    def __call__(self, *args, **kwargs):
        return self.random()
