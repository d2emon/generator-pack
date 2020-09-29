from .water import OceanFactory, SeaFactory, SeaWaterFactory, IcebergFactory, BeachFactory, AbyssFactory, \
    RiverFactory, LakeFactory
from .soil import SoilFactory, MudFactory, SandFactory
from .land import PlainFactory, ForestFactory, JungleFactory, MountainFactory, CaveFactory
from .ancient import AncientPlainFactory, AncientForestFactory, AncientJungleFactory, AncientMountainFactory, \
    AncientCaveFactory
from .sky import SkyFactory, TerraformedSkyFactory, FutureSkyFactory, MeteoriteFactory, CloudFactory, \
    PrecipitationFactory
from ..universe.atmosphere import OzoneFactory


FACTORIES = {
    'ocean': OceanFactory(),
    'sea': SeaFactory(),
    'sea water': SeaWaterFactory(),
    'iceberg': IcebergFactory(),
    'beach': BeachFactory(),
    'abyss': AbyssFactory(),
    'sand': SandFactory(),
    'soil': SoilFactory(),
    'mud': MudFactory(),

    'river': RiverFactory(),
    'lake': LakeFactory(),
    'plain': PlainFactory(),
    'forest': ForestFactory(),
    'jungle': JungleFactory(),
    'mountain': MountainFactory(),
    'cave': CaveFactory(),

    'ancient plain': AncientPlainFactory(),
    'ancient forest': AncientForestFactory(),
    'ancient jungle': AncientJungleFactory(),
    'ancient mountain': AncientMountainFactory(),
    'ancient cave': AncientCaveFactory(),

    'future sky': FutureSkyFactory(),
    'terraformed sky': TerraformedSkyFactory(),
    'sky': SkyFactory(),
    'meteorite': MeteoriteFactory(),
    'ozone': OzoneFactory(),
    'cloud': CloudFactory(),
    'precipitation': PrecipitationFactory(),
}
