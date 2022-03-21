from data.db.storm import worlds
from genesys.storm.models.world import WorldType
from .db import DbFactory


class WorldTypeFactory(DbFactory):
    def __init__(self):
        super().__init__(WorldType, worlds.types)

    def __call__(self, *args, **kwargs):
        return self.random()