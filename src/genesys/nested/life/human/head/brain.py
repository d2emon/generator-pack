from models.v5 import life
from ...body.body_parts import SoftBodyPartFactory
from ...body.brain import BrainCellFactory

# ???
from ...single_celled import BacteriaFactory


class BrainFactory(SoftBodyPartFactory):
    model = life.Brain

    def children(self):
        yield BacteriaFactory.probable(20)
        yield BrainCellFactory.one()
