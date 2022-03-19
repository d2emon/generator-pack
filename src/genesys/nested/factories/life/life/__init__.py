from .life import LifeFactory, SeaLifeFactory, AbyssLifeFactory, BeachLifeFactory, RiverLifeFactory, \
    LakeLifeFactory, LandLifeFactory, ForestLifeFactory, JungleLifeFactory, MountainLifeFactory, CaveLifeFactory, \
    UrbanLifeFactory, SkyLifeFactory, GalacticLifeFactory, GalaxyArmLifeFactory, GalaxyCenterLifeFactory, \
    NebulaLifeFactory, BlackHoleLifeFactory, StarLifeFactory, AsteroidBeltLifeFactory, GasGiantLifeFactory, \
    AsteroidLifeFactory, MoonLifeFactory, PlanetCoreLifeFactory, BarrenPlanetLifeFactory, VisitorPlanetLifeFactory
from .ancient import AncientLandLifeFactory, AncientForestLifeFactory, AncientJungleLifeFactory, \
    AncientMountainLifeFactory


FACTORIES = {
    'life': LifeFactory(),
    'sea life': SeaLifeFactory(),
    'abyss life': AbyssLifeFactory(),
    'beach life': BeachLifeFactory(),
    'river life': RiverLifeFactory(),
    'lake life': LakeLifeFactory(),
    'land life': LandLifeFactory(),
    'forest life': ForestLifeFactory(),
    'jungle life': JungleLifeFactory(),
    'mountain life': MountainLifeFactory(),
    'cave life': CaveLifeFactory(),
    'ancient land life': AncientLandLifeFactory(),
    'ancient forest life': AncientForestLifeFactory(),
    'ancient jungle life': AncientJungleLifeFactory(),
    'ancient mountain life': AncientMountainLifeFactory(),
    'urban life': UrbanLifeFactory(),
    'sky life': SkyLifeFactory(),
    'galactic life': GalacticLifeFactory(),
}
