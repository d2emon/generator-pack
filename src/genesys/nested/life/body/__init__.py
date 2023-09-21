"""
Body stuff
"""
from .blood import BloodFactory, BloodCellFactory, BloodVesselsFactory
from .skin import DeadSkinFactory, PoresFactory, ScarFactory, SkinFactory, SkinCellFactory, \
    ScalesFactory, ExoskeletonFactory
from .skeleton import BoneFactory, BoneCellFactory, BonesFactory, FatFactory, MuscleFactory, MuscleCellFactory, \
    SkeletonFactory
from .body_parts import BodyPartFactory, SkinlessBodyPartFactory, SkinlessSoftBodyPartFactory, SoftBodyPartFactory, \
    FleshFactory, SoftFleshFactory, WeirdSoftOrganFactory, WeirdHardOrganFactory
from .head.brain import BrainCellFactory
from .hair import DandruffFactory, \
    HairFactory, FurFactory, WhiskersFactory

# ???
from ..animals.mollusk.clam import ClamShellFactory
# ???
from ..animals.crustacean import CrustaceanLegFactory, CrustaceanClawFactory, CrustaceanShellFactory

# ???
from .head import *
# ???
from ..animals.bird import BirdLimbFactory, BirdWingFactory, BirdLegFactory, BirdTailFactory, BeakFactory, BirdHeadFactory, \
    BirdBodyFactory
# ???
from ..animals.cetacean import CetaceanFinFactory, CetaceanFlipperFactory
# ???
from ..animals.fish import FishFinFactory, FishTailFactory, FishSkinFactory
# ???
from ..animals.insect import InsectLegFactory, InsectClawFactory, StingerFactory, AntennaFactory, InsectWingFactory
# ???
from ..animals.jelly import JellyFactory
# ???
from ..animals.limb import WingFactory, TentacleFactory, TailFactory
# ???
from ..animals.mammal import MammalLegFactory, MammalHeadFactory, MammalBodyFactory
# ???
from ..animals.reptile import ReptileWingFactory, ReptileHeadFactory, ReptileLegFactory, ReptileBodyFactory, SnakeBodyFactory
# ???
from ..animals.venom import VenomFactory


FACTORIES = {
    'body part': BodyPartFactory,
    'soft body part': SoftBodyPartFactory,
    'skinless body part': SkinlessBodyPartFactory,
    'skinless soft body part': SkinlessSoftBodyPartFactory,
    'blood vessels': BloodVesselsFactory,
    'blood': BloodFactory,
    'blood cell': BloodCellFactory,
    'skin': SkinFactory,
    'scar': ScarFactory,
    'pores': PoresFactory,
    'skin cell': SkinCellFactory,
    'dead skin': DeadSkinFactory,
    'bone': BoneFactory,
    'bones': BonesFactory,
    'bone cell': BoneCellFactory,
    'muscles': MuscleFactory,
    'muscle cell': MuscleCellFactory,
    'fat': FatFactory,
    'brain cell': BrainCellFactory,
    'dandruff': DandruffFactory,

    # 'skeleton': SkeletonFactory(),
    # 'flesh': FleshFactory(),
    # 'soft flesh': SoftFleshFactory(),
    # 'scales': ScalesFactory(),
    # 'fish fin': FishFinFactory(),
    # 'fish tail': FishTailFactory(),
    # 'fish skin': FishSkinFactory(),
    # 'cetacean flipper': CetaceanFlipperFactory(),
    # 'cetacean fin': CetaceanFinFactory(),
    # 'crustacean claw': CrustaceanClawFactory(),
    # 'crustacean leg': CrustaceanLegFactory(),
    # 'crustacean shell': CrustaceanShellFactory(),
    # 'clam shell': ClamShellFactory(),
    # 'simple eye': SimpleEyeFactory(),
    # 'exoskeleton': ExoskeletonFactory(),
    # 'insect leg': InsectLegFactory(),
    # 'insect claw': InsectClawFactory(),
    # 'stinger': StingerFactory(),
    # 'antenna': AntennaFactory(),
    # 'insect wing': InsectWingFactory(),
    # 'wing': WingFactory(),
    # 'reptile wing': ReptileWingFactory(),
    # 'bird wing': BirdWingFactory(),
    # 'bird leg': BirdLegFactory(),
    # 'bird tail': BirdTailFactory(),
    # 'venom': VenomFactory(),
    # 'jelly': JellyFactory(),

    # 'weird soft organ': WeirdSoftOrganFactory(),
    # 'weird hard organ': WeirdHardOrganFactory(),

    # 'tentacle': TentacleFactory(),
    # 'simple mouth': SimpleMouthFactory(),

    # 'beak': BeakFactory(),

    # 'reptile head': ReptileHeadFactory(),
    # 'reptile leg': ReptileLegFactory(),

    # 'fur': FurFactory(),
    # 'snout': SnoutFactory(),
    # 'whiskers': WhiskersFactory(),
    # 'mammal leg': MammalLegFactory(),
    # 'tail': TailFactory(),
    # 'mammal head': MammalHeadFactory(),
    # 'mammal body': MammalBodyFactory(),
    # 'bird body': BirdBodyFactory(),
    # 'bird head': BirdHeadFactory(),
    # 'reptile body': ReptileBodyFactory(),
    # 'snake body': SnakeBodyFactory(),
}
