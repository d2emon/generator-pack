from data.storm import worlds
from factories.db_factory import DbFactory
from models.world.shape import WorldShape


class ShapeFactory(DbFactory):
    def __init__(self):
        super().__init__(WorldShape, worlds.shapes)
