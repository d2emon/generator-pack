from .space import GalacticLife


class NebulaLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        probability = 15
