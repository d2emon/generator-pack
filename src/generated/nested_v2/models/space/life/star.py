from generated.nested_v2.models import Ghost
from .space import GalacticLife


class StarLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        def children(self):
            yield Ghost.probable(0.1)
            # yield SpaceMonster.probable(0.2)
