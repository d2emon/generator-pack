from generated import life
from genesys.nested.factories.life.cell import CellFactory
from genesys.nested.factories.life.animal_body.body_parts import SoftBodyPartFactory


class BrainCellFactory(CellFactory):
    default_model = life.BrainCell


class BrainFactory(SoftBodyPartFactory):
    default_model = life.Brain

    def children(self):
        # yield Bacteria.probable(20)
        yield BrainCellFactory()
