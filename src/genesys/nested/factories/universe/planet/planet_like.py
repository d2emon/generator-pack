# from generated import universe
from ...factory import Factory


class PlanetLikeFactory(Factory):
    def atmosphere(self):
        yield None

    def biosphere(self):
        yield None

    def core(self):
        # yield PlanetCore
        yield None

    def plates(self):
        # yield from Plate.multiple(2, 7)
        # yield from Plate.multiple(1, 7)
        yield None

    def sky(self):
        yield None

    def visited(self):
        yield None

    def children(self):
        yield from self.core()
        yield from self.atmosphere()
        yield from self.biosphere()
        yield from self.plates()
        yield from self.sky()
        yield from self.visited()
