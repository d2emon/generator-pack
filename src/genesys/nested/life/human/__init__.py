from ...cloth.clothing_set import ClothingSetFactory
from .torso import BellybuttonFactory, ButtFactory, ChestFactory, NaughtyBitsFactory, NippleFactory, PelvisFactory, TorsoFactory
from .arm import ArmFactory, ArmpitFactory, ArmpitHairFactory, ElbowFactory, FingerFactory, FingernailFactory, HandFactory
from .leg import FootFactory, KneeFactory, LegFactory, ToeFactory, ToenailFactory
from .body import BodyFactory
from .person import CorpseFactory, ManFactory, PersonFactory, WomanFactory

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
# from ..abomination import AbominationFactory, AbominationPsycheFactory, AbominationThoughtsFactory, \
#     AbominationThoughtFactory, AbominationBodyFactory, AbominationTorsoFactory, AbominationHeadFactory


"""
new Thing("head",["mouth", "nose", "eye,99%", "eye,99%", "ear,2", "skull", "head hair,85%",
    (BodyPatFactory)
    ],"head");
new Thing("eye",["eyelashes", "eye flesh", "tear,2%"],"eye");
new Thing("eye flesh",[
    WaterFactory.one(),
    BloodVesselsFactory.one(),
    FatFactory.one(),
    ],"eyeball");
new Thing("eyelashes",[".hair"],"eyelashes");
new Thing("tear",[
    WaterFactory.one(),
    SaltFactory.one(),
]);
new Thing("ear",[
    (SoftBodyPartFactory)
    ],"ear");
new Thing("brain",["bacteria,20%",
    BrainCellFactory.one(),
    ],"brain");
new Thing("skull",["brain",
    (BonesFactory),
    ]);
new Thing("head hair",[".hair",
    DandruffFactory.probable(10),
    ],[["brown", "black", "gray", "light", "blonde", "red", "dark"], [" hair"]]);
new Thing("hair",["bacteria,30%", "keratin"],"hair");
new Thing("nose",["nostril,2",
    (BodyPatFactory)
    ],"nose");
new Thing("nostril",["nostril hair", "boogers,0-1",
    (SoftBodyPartFactory)
    ],"nostril");
new Thing("nostril hair",[".hair"],"nostril hair");
new Thing("boogers",[
    OrganicFactory.one(),
]);
new Thing("mouth",["teeth", "tongue"],"mouth");
new Thing("teeth",[
    ELEMENTS['Ca'].one(),
    ELEMENTS['P'].one(),
],"teeth");
new Thing("tongue",[
    MusclesFactory.one(),
    ],"tongue");
"""


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
    # 'head': HeadFactory(),
    # 'eye': EyeFactory(),
    # 'eye flesh': EyeFleshFactory(),
    # 'eyelashes': EyelashesFactory(),
    # 'tear': TearFactory(),
    # 'ear': EarFactory(),
    # 'brain': BrainFactory(),
    # 'skull': SkullFactory(),
    # 'head hair': HeadHairFactory(),
    # 'hair': HairFactory(),
    # 'nose': NoseFactory(),
    # 'nostril': NostrilFactory(),
    # 'nostril hair': NostrilHairFactory(),
    # 'boogers': BoogersFactory(),
    # 'mouth': MouthFactory(),
    # 'teeth': TeethFactory(),
    # 'tongue': TongueFactory(),

    # 'abomination': AbominationFactory(),
    # 'abomination psyche': AbominationPsycheFactory(),
    # 'abomination thoughts': AbominationThoughtsFactory(),
    # 'abomination thought': AbominationThoughtFactory(),
    # 'abomination body': AbominationBodyFactory(),
    # 'abomination head': AbominationHeadFactory(),
    # 'abomination torso': AbominationTorsoFactory(),
}
