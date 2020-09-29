from .body_parts import BodyPartFactory, SoftBodyPartFactory, SkinlessBodyPartFactory, SkinlessSoftBodyPartFactory, \
    FleshFactory, SoftFleshFactory
from .hair import HairFactory
from .skeleton import BoneCellFactory, BoneFactory, BonesFactory, MuscleCellFactory, MuscleFactory, FatFactory, \
    SkeletonFactory
from .skin import SkinCellFactory, DeadSkinFactory, ScarFactory, PoresFactory, SkinFactory, ScalesFactory, \
    ExoskeletonFactory
from .fish import FishFinFactory, FishTailFactory, FishSkinFactory
from .cetacean import CetaceanFinFactory, CetaceanFlipperFactory
from .crustacean import CrustaceanLegFactory, CrustaceanClawFactory, CrustaceanShellFactory
from .mollusk import ClamShellFactory
from .eye import EyeFleshFactory, SimpleEyeFactory
from .insect import InsectLegFactory, InsectClawFactory, StingerFactory, AntennaFactory, InsectWingFactory
from .limb import WingFactory
from .reptile import ReptileWingFactory
from .bird import BirdLimbFactory, BirdWingFactory, BirdLegFactory, BirdTailFactory
from .venom import VenomFactory


"""
# new Thing("skeleton",["Bones"],"skeleton");
# new Thing("flesh",[".SkinlessBodyPart"],"flesh");
# new Thing("soft flesh",[".SkinlessSoftBodyPart"],"flesh");
# new Thing("scales",["Keratin"]);
# new Thing("fish fin",["Muscles","scales"],"fin");
# new Thing("fish tail",["Muscles","scales"],"tail");
# new Thing("fish skin",["scales"],"skin");
# new Thing("cetacean flipper",["Muscles","Skin"],"flipper");
# new Thing("cetacean fin",["Muscles","Skin"],"fin");
# new Thing("crustacean claw",["Chitin","Muscles","Fat"],"claw");
# new Thing("crustacean leg",["Chitin","Muscles","Fat"],"leg");
# new Thing("crustacean shell",["Chitin"],"shell");
# new Thing("clam shell",["Calcium"],"shell");
# new Thing("simple eye",[".EyeFlesh"],"eye");
# new Thing("exoskeleton",["Chitin"],"exoskeleton");
# new Thing("insect leg",["Chitin","Muscles","Fat"],"leg");
# new Thing("insect claw",["Chitin","Muscles","Fat"],"claw");
# new Thing("stinger",["Chitin","venom"],"stinger");
# new Thing("antenna",["Chitin"],"antenna");
# new Thing("insect wing",[["Chitin","scales"],"Dew,2%"],"wing");
# new Thing("wing",["feathers",".BodyPart"],"wing");
# new Thing("reptile wing",["scales",".BodyPart"],"wing");
# new Thing("bird wing",["feathers",".BodyPart"],"wing");
# new Thing("bird leg",["feathers",".BodyPart"],"leg");
# new Thing("bird tail",["feathers",".BodyPart"],"tail");
# new Thing("venom",["Proteins","Lipids,40%","Nitrogen,40%","Sodium,40%","Chlorine,40%"],"venom");
# new Thing("jelly",["Water"]);
"""
