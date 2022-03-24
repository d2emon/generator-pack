from data.storm import worlds
from models.world import WorldType
from .db import DbFactory


class WorldTypeFactory(DbFactory):
    def __init__(self):
        super().__init__(WorldType, worlds.types)

    def __call__(self, *args, **kwargs):
        return self.random()
