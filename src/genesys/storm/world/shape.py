from data.storm import worlds
from models.world.shape import WorldShape
from .db import DbFactory


class ShapeFactory(DbFactory):
    def __init__(self):
        super().__init__(WorldShape, worlds.shapes)
