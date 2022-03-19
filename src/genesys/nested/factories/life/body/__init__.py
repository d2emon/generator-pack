from ...cloth import ClothingSetFactory
from ..animal_body.body_parts import BodyPartFactory, SoftBodyPartFactory, SkinlessBodyPartFactory, \
    SkinlessSoftBodyPartFactory
from ..animal_body.hair import HairFactory
from ..animal_body.skin import SkinCellFactory, DeadSkinFactory, PoresFactory, ScarFactory, SkinFactory
from ..animal_body.skeleton import BoneCellFactory, BonesFactory, BoneFactory, MuscleCellFactory, MuscleFactory, \
    FatFactory
from ..animal_body.head import EyeFleshFactory, TeethFactory, BrainCellFactory, EyeFactory, EyelashesFactory, \
    TearFactory, EarFactory, BrainFactory, NoseFactory, NostrilFactory, NostrilHairFactory, BoogersFactory, \
    MouthFactory, TongueFactory, SkullFactory
from ..animal_body.blood import BloodCellFactory, BloodFactory, BloodVesselsFactory
from .head import *
from .person import *
from .body import BodyFactory
from .torso import TorsoFactory, ChestFactory, BellybuttonFactory, NippleFactory, PelvisFactory, NaughtyBitsFactory, \
    ButtFactory
from .arm import ArmFactory, HandFactory, FingerFactory, FingernailFactory, ElbowFactory, ArmpitFactory, \
    ArmpitHairFactory
from .leg import LegFactory, FootFactory, ToeFactory, ToenailFactory, KneeFactory
from ..abomination import AbominationFactory, AbominationPsycheFactory, AbominationThoughtsFactory, \
    AbominationThoughtFactory, AbominationBodyFactory, AbominationTorsoFactory, AbominationHeadFactory


FACTORIES = {
    'body part': BodyPartFactory(),
    'soft body part': SoftBodyPartFactory(),
    'skinless body part': SkinlessBodyPartFactory(),
    'skinless soft body part': SkinlessSoftBodyPartFactory(),
    'blood vessels': BloodVesselsFactory(),
    'blood': BloodFactory(),
    'blood cell': BloodCellFactory(),
    'skin': SkinFactory(),
    'scar': ScarFactory(),
    'pores': PoresFactory(),
    'skin cell': SkinCellFactory(),
    'dead skin': DeadSkinFactory(),
    'bone': BoneFactory(),
    'bones': BonesFactory(),
    'bone cell': BoneCellFactory(),
    'muscles': MuscleFactory(),
    'muscle cell': MuscleCellFactory(),
    'fat': FatFactory(),
    'brain cell': BrainCellFactory(),
    'dandruff': DandruffFactory(),

    'clothing set': ClothingSetFactory(),
    'man': ManFactory(),
    'woman': WomanFactory(),
    'person': PersonFactory(),
    'corpse': CorpseFactory(),
    'body': BodyFactory(),
    'torso': TorsoFactory(),
    'chest': ChestFactory(),
    'bellybutton': BellybuttonFactory(),
    'nipple': NippleFactory(),
    'pelvis': PelvisFactory(),
    'naughty bits': NaughtyBitsFactory(),
    'butt': ButtFactory(),
    'arm': ArmFactory(),
    'hand': HandFactory(),
    'finger': FingerFactory(),
    'fingernail': FingernailFactory(),
    'elbow': ElbowFactory(),
    'armpit': ArmpitFactory(),
    'armpit hair': ArmpitHairFactory(),
    'leg': LegFactory(),
    'foot': FootFactory(),
    'toe': ToeFactory(),
    'toenail': ToenailFactory(),
    'knee': KneeFactory(),
    'head': HeadFactory(),
    'eye': EyeFactory(),
    'eye flesh': EyeFleshFactory(),
    'eyelashes': EyelashesFactory(),
    'tear': TearFactory(),
    'ear': EarFactory(),
    'brain': BrainFactory(),
    'skull': SkullFactory(),
    'head hair': HeadHairFactory(),
    'hair': HairFactory(),
    'nose': NoseFactory(),
    'nostril': NostrilFactory(),
    'nostril hair': NostrilHairFactory(),
    'boogers': BoogersFactory(),
    'mouth': MouthFactory(),
    'teeth': TeethFactory(),
    'tongue': TongueFactory(),

    'abomination': AbominationFactory(),
    'abomination psyche': AbominationPsycheFactory(),
    'abomination thoughts': AbominationThoughtsFactory(),
    'abomination thought': AbominationThoughtFactory(),
    'abomination body': AbominationBodyFactory(),
    'abomination head': AbominationHeadFactory(),
    'abomination torso': AbominationTorsoFactory(),
}
