from models.v5 import life
from ...cell import CellFactory
from ...single_celled import BacteriaFactory
from ..body_parts import SoftBodyPartFactory


class BrainCellFactory(CellFactory):
    default_model = life.BrainCell


class BrainFactory(SoftBodyPartFactory):
    default_model = life.Brain

    def children(self):
        yield BacteriaFactory().probable(20)
        yield BrainCellFactory()
