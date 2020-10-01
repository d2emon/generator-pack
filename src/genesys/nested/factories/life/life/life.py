from generated import life
from ...factory import Factory
from ..body import PersonFactory
from ..vegetation import TreeFactory, GrassBladeFactory
from ..animals import PlanktonFactory, ClamFactory, CnidariaFactory, MolluskFactory


class LifeFactory(Factory):
    default_model = life.Life

    def children(self):
        yield self.select_item(
            # "bird"
            # "poultry"
            # "fish"
            # "shark"
            # "crustacean"
            CnidariaFactory(),
            # "worm"
            MolluskFactory(),
            ClamFactory(),
            PlanktonFactory(),
            # "reptile"
            # "amphibian"
            # "snake"
            # "small mammal"
            # "herbivorous mammal"
            # "predatory mammal"
            # "monkey"
            # "bear"
            # "horse"
            # "cat"
            # "dog"
            # "dinosaur"
            # "medieval person"
            # "caveman"
            # "dragon"
            PersonFactory(),
            # "space animal"
            # "insect"
            TreeFactory(),
            GrassBladeFactory(),
        )


class SeaLifeFactory(LifeFactory):
    def children(self):
        # "sea monster,0.5%"
        # "fish,5-10"
        # "cetacean,0-4"
        # "shark,0-4"
        # "crustacean,1-4"
        yield from CnidariaFactory().multiple(1, 4)
        yield from MolluskFactory().multiple(1, 4)
        yield from ClamFactory().multiple(1, 4)
        yield from PlanktonFactory().multiple(2, 8)


class AbyssLifeFactory(LifeFactory):
    def children(self):
        # "sea monster,2%"
        # "fish,3-6"
        # "cetacean,0-2"
        # "shark,0-2"
        # "crustacean,2-5"
        yield from CnidariaFactory().multiple(2, 5)
        yield from MolluskFactory().multiple(2, 5)
        yield from ClamFactory().multiple(2, 5)
        yield from PlanktonFactory().multiple(2, 8)


class BeachLifeFactory(LifeFactory):
    def children(self):
        # "bird,0-3"
        # "herbivorous mammal,5%"
        # "amphibian,2%"
        # "reptile,2%"
        # "snake,2%"
        # "predatory mammal,5%"
        # "small mammal,2-5"
        # "insect,3-10"
        yield from ClamFactory().multiple(3, 8)


class RiverLifeFactory(LifeFactory):
    def children(self):
        # "fish,5-15"
        # "crustacean,0-10"
        yield from PlanktonFactory().multiple(2, 8)
        # "bird,0-5"
        # "small mammal,0-2"
        # "amphibian,0-5"
        # "reptile,0-1"
        # "snake,0-1"
        # "insect,3-10"


class LakeLifeFactory(LifeFactory):
    def children(self):
        # "sea monster,1%"
        # "fish,5-15"
        # "amphibian,0-5"
        # "crustacean,0-10"
        # "bird,0-5"
        yield from PlanktonFactory().multiple(5, 15)
        # "small mammal,0-2"
        # "reptile,0-1"
        # "snake,0-1"
        # "insect,3-10"


class LandLifeFactory(LifeFactory):
    def children(self):
        # "herbivorous mammal,2-8"
        # "horse,5%"
        # "predatory mammal,0-4"
        # "small mammal,5-10"
        # "amphibian,0-2"
        # "reptile,0-2"
        # "snake,0-2"
        # "bird,0-5"
        # "anthill,30%"
        # "insect,5-10"
        yield None


class ForestLifeFactory(LifeFactory):
    def children(self):
        # "herbivorous mammal,2-8"
        # "predatory mammal,0-4"
        # "bear,0-5"
        # "small mammal,5-10"
        # "amphibian,0-3"
        # "reptile,0-3"
        # "snake,0-3"
        # "bird,2-10"
        # "beehive,30%"
        # "anthill,30%"
        # "insect,5-10"
        yield None


class JungleLifeFactory(LifeFactory):
    def children(self):
        # "herbivorous mammal,1-5"
        # "predatory mammal,0-4"
        # "monkey,1-5"
        # "small mammal,5-10"
        # "amphibian,0-3"
        # "reptile,0-3"
        # "snake,0-6"
        # "bird,2-10"
        # "beehive,30%"
        # "anthill,30%"
        # "insect,5-10"
        yield None


class MountainLifeFactory(LifeFactory):
    def children(self):
        # "herbivorous mammal,1-6"
        # "predatory mammal,0-4"
        # "bear,2-6"
        # "small mammal,5-10"
        # "amphibian,0-2"
        # "reptile,0-2"
        # "snake,0-2"
        # "bird,2-10"
        # "beehive,30%"
        # "anthill,30%"
        # "insect,5-10"
        yield None


class CaveLifeFactory(LifeFactory):
    def children(self):
        # "herbivorous mammal,10%"
        # "predatory mammal,10%"
        # "bear,20%"
        # "small mammal,20%"
        # "small mammal,20%"
        # "small mammal,20%"
        # "amphibian,20%"
        # "reptile,20%"
        # "snake,10%"
        # "bird,15%"
        # "bird,5%"
        # "insect,5-10"
        yield None


class UrbanLifeFactory(LifeFactory):
    def children(self):
        # "bird,0-8"
        # "small mammal,5-10"
        # "anthill,30%"
        # "insect,10-20"
        yield None


class SkyLifeFactory(LifeFactory):
    def children(self):
        # "shark,1%"
        # "bird,5-20"
        # "insect,0-2"
        yield None


class GalacticLifeFactory(LifeFactory):
    def children(self):
        # "space monster,1%"
        # "space animal,1-12"
        yield None


class GalaxyArmLifeFactory(LifeFactory):
    def children(self):
        yield GalacticLifeFactory().probable(5)


class GalaxyCenterLifeFactory(LifeFactory):
    def children(self):
        yield GalacticLifeFactory().probable(10)


class NebulaLifeFactory(LifeFactory):
    def children(self):
        yield GalacticLifeFactory().probable(15)


class BlackHoleLifeFactory(LifeFactory):
    def children(self):
        # "crustacean,0.2%"
        yield None


class StarLifeFactory(LifeFactory):
    def children(self):
        # "ghost,0.1%"
        # "space monster,0.2%"
        yield None


class PlanetCoreLifeFactory(LifeFactory):
    def children(self):
        # "space monster,0.5%"
        yield None


class BarrenPlanetLifeFactory(LifeFactory):
    def children(self):
        yield GalacticLifeFactory().probable(10)


class VisitorPlanetLifeFactory(GalacticLifeFactory):
    pass


class GasGiantLifeFactory(LifeFactory):
    def children(self):
        yield GalacticLifeFactory().probable(10)


class AsteroidLifeFactory(LifeFactory):
    def children(self):
        # "space animal,0.5%"
        yield None


class AsteroidBeltLifeFactory(LifeFactory):
    def children(self):
        yield GalacticLifeFactory().probable(20)


class MoonLifeFactory(LifeFactory):
    def children(self):
        # "ghost,0.1%"
        yield None
