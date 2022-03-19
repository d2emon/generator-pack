from .life import LandLifeFactory, ForestLifeFactory, JungleLifeFactory, MountainLifeFactory


class AncientLandLifeFactory(LandLifeFactory):
    def children(self):
        # "dinosaur,0-8"
        yield from super().children()


class AncientForestLifeFactory(ForestLifeFactory):
    def children(self):
        # "dinosaur,0-5"
        yield from super().children()


class AncientJungleLifeFactory(JungleLifeFactory):
    def children(self):
        # "dinosaur,0-5"
        yield from super().children()


class AncientMountainLifeFactory(MountainLifeFactory):
    def children(self):
        # "dinosaur,0-3"
        yield from super().children()
