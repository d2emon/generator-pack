from genesys.nested.models import models
# from genesys.nested.factories.thing_builder import ThingBuilder
from ..cell import Cell


class PlantCell(Cell):
    model = models.PlantCell
