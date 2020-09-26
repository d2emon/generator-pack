from ..scalable import Scalable


class Starship(Scalable):
    def __init__(self, name, size, universe="", scale=0):
        Scalable.__init__(self, name, size, scale)
        self.universe = universe
