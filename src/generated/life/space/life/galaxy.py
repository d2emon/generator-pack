from .space import GalacticLife


class GalaxyCenterLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        probability = 0


class GalaxyArmLife(GalacticLife):
    class Factory(GalacticLife.Factory):
        probability = 5
