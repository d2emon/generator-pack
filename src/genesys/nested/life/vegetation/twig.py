from models.v5 import life
from factories.nested_factory import NestedFactory as Factory
from ..cell import CellFactory


class PlantCellFactory(CellFactory):
    default_model = life.PlantCell


class TwigFactory(Factory):
    default_model = life.Twig

    def children(self):
        yield PlantCellFactory()
