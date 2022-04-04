from models.scales import Sized as Scalable, ScalableSize as Size


class Starship(Scalable):
    def __init__(self, name, size, universe="", scale=0):
        Scalable.__init__(self, name, Size(size, scale))
        self.universe = universe
