from models.v5 import life
from ...cell import CellFactory
from ..body_parts import SoftBodyPartFactory
# ???
from ...single_celled import BacteriaFactory


class BrainCellFactory(CellFactory):
    model = life.BrainCell


class BrainFactory(SoftBodyPartFactory):
    # TODO: Refactor it
    default_model = life.Brain

    def children(self):
        yield BacteriaFactory().probable(20)
        yield BrainCellFactory()
