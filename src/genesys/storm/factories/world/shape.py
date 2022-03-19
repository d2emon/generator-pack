from data.db.storm import worlds
from genesys.storm.models.world.shape import WorldShape
from .db import DbFactory


class ShapeFactory(DbFactory):
    def __init__(self):
        super().__init__(WorldShape, worlds.shapes)
