from ..animals.mollusk.clam import ClamShellFactory
from ..animals.crustacean import CrustaceanLegFactory, CrustaceanClawFactory, CrustaceanShellFactory
from .body_parts import BodyPartFactory, SoftBodyPartFactory, SkinlessBodyPartFactory, SkinlessSoftBodyPartFactory, \
    FleshFactory, SoftFleshFactory, WeirdSoftOrganFactory, WeirdHardOrganFactory
from .hair import HairFactory, FurFactory, WhiskersFactory
from .skeleton import BoneCellFactory, BoneFactory, BonesFactory, MuscleCellFactory, MuscleFactory, FatFactory, \
    SkeletonFactory
from .skin import SkinCellFactory, DeadSkinFactory, ScarFactory, PoresFactory, SkinFactory, ScalesFactory, \
    ExoskeletonFactory
from .fish import FishFinFactory, FishTailFactory, FishSkinFactory
from .cetacean import CetaceanFinFactory, CetaceanFlipperFactory
from .insect import InsectLegFactory, InsectClawFactory, StingerFactory, AntennaFactory, InsectWingFactory
from .limb import WingFactory, TentacleFactory, TailFactory
from .reptile import ReptileWingFactory, ReptileHeadFactory, ReptileLegFactory, ReptileBodyFactory, SnakeBodyFactory
from .bird import BirdLimbFactory, BirdWingFactory, BirdLegFactory, BirdTailFactory, BeakFactory, BirdHeadFactory, \
    BirdBodyFactory
from .mammal import MammalLegFactory, MammalHeadFactory, MammalBodyFactory
from .blood import BloodCellFactory, BloodFactory, BloodVesselsFactory
from .venom import VenomFactory
from .jelly import JellyFactory
from .head import *


FACTORIES = {
    'skeleton': SkeletonFactory(),
    'flesh': FleshFactory(),
    'soft flesh': SoftFleshFactory(),
    'scales': ScalesFactory(),
    'fish fin': FishFinFactory(),
    'fish tail': FishTailFactory(),
    'fish skin': FishSkinFactory(),
    'cetacean flipper': CetaceanFlipperFactory(),
    'cetacean fin': CetaceanFinFactory(),
    'crustacean claw': CrustaceanClawFactory(),
    'crustacean leg': CrustaceanLegFactory(),
    'crustacean shell': CrustaceanShellFactory(),
    'clam shell': ClamShellFactory(),
    'simple eye': SimpleEyeFactory(),
    'exoskeleton': ExoskeletonFactory(),
    'insect leg': InsectLegFactory(),
    'insect claw': InsectClawFactory(),
    'stinger': StingerFactory(),
    'antenna': AntennaFactory(),
    'insect wing': InsectWingFactory(),
    'wing': WingFactory(),
    'reptile wing': ReptileWingFactory(),
    'bird wing': BirdWingFactory(),
    'bird leg': BirdLegFactory(),
    'bird tail': BirdTailFactory(),
    'venom': VenomFactory(),
    'jelly': JellyFactory(),

    'weird soft organ': WeirdSoftOrganFactory(),
    'weird hard organ': WeirdHardOrganFactory(),

    'tentacle': TentacleFactory(),
    'simple mouth': SimpleMouthFactory(),

    'beak': BeakFactory(),

    'reptile head': ReptileHeadFactory(),
    'reptile leg': ReptileLegFactory(),

    'fur': FurFactory(),
    'snout': SnoutFactory(),
    'whiskers': WhiskersFactory(),
    'mammal leg': MammalLegFactory(),
    'tail': TailFactory(),
    'mammal head': MammalHeadFactory(),
    'mammal body': MammalBodyFactory(),
    'bird body': BirdBodyFactory(),
    'bird head': BirdHeadFactory(),
    'reptile body': ReptileBodyFactory(),
    'snake body': SnakeBodyFactory(),
}
