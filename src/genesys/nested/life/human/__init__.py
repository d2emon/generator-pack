from .hair import HairFactory
from .head.brain import BrainFactory
from .head.skull import SkullFactory
from .head.ear import EarFactory
from .head.eye import EyeFactory, EyeFleshFactory, EyelashesFactory, TearFactory
from .head.mouth import MouthFactory, TeethFactory, TongueFactory
from .head.nose import BoogersFactory, NoseFactory, NostrilFactory, NostrilHairFactory
from .head import HeadFactory, HeadHairFactory
from .torso import BellybuttonFactory, ButtFactory, ChestFactory, NaughtyBitsFactory, NippleFactory, PelvisFactory, TorsoFactory
from .arm import ArmFactory, ArmpitFactory, ArmpitHairFactory, ElbowFactory, FingerFactory, FingernailFactory, HandFactory
from .leg import FootFactory, KneeFactory, LegFactory, ToeFactory, ToenailFactory
from .body import BodyFactory
from .person import CorpseFactory, ManFactory, PersonFactory, WomanFactory

from ...unsorted_cloth import ClothingSetFactory

# from ..animal_body.body_parts import BodyPartFactory, SoftBodyPartFactory, SkinlessBodyPartFactory, \
#     SkinlessSoftBodyPartFactory
# from ..animal_body.hair import HairFactory
# from ..animal_body.skin import SkinCellFactory, DeadSkinFactory, PoresFactory, ScarFactory, SkinFactory
# from ..animal_body.skeleton import BoneCellFactory, BonesFactory, BoneFactory, MuscleCellFactory, MuscleFactory, \
#     FatFactory
# from ..animal_body.head import EyeFleshFactory, TeethFactory, BrainCellFactory, EyeFactory, EyelashesFactory, \
#     TearFactory, EarFactory, BrainFactory, NoseFactory, NostrilFactory, NostrilHairFactory, BoogersFactory, \
#     MouthFactory, TongueFactory, SkullFactory
# from ..animal_body.blood import BloodCellFactory, BloodFactory, BloodVesselsFactory


FACTORIES = {
    'clothing set': ClothingSetFactory,
    'man': ManFactory,
    'woman': WomanFactory,
    'person': PersonFactory,
    'corpse': CorpseFactory,
    'body': BodyFactory,
    'torso': TorsoFactory,
    'chest': ChestFactory,
    'bellybutton': BellybuttonFactory,
    'nipple': NippleFactory,
    'pelvis': PelvisFactory,
    'naughty bits': NaughtyBitsFactory,
    'butt': ButtFactory,
    'arm': ArmFactory,
    'hand': HandFactory,
    'finger': FingerFactory,
    'fingernail': FingernailFactory,
    'elbow': ElbowFactory,
    'armpit': ArmpitFactory,
    'armpit hair': ArmpitHairFactory,
    'leg': LegFactory,
    'foot': FootFactory,
    'toe': ToeFactory,
    'toenail': ToenailFactory,
    'knee': KneeFactory,
    'head': HeadFactory,
    'eye': EyeFactory,
    'eye flesh': EyeFleshFactory,
    'eyelashes': EyelashesFactory,
    'tear': TearFactory,
    'ear': EarFactory,
    'brain': BrainFactory,
    'skull': SkullFactory,
    'head hair': HeadHairFactory,
    'hair': HairFactory,
    'nose': NoseFactory,
    'nostril': NostrilFactory,
    'nostril hair': NostrilHairFactory,
    'boogers': BoogersFactory,
    'mouth': MouthFactory,
    'teeth': TeethFactory,
    'tongue': TongueFactory,
}
