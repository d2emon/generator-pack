from models.tree_model import TreeModel as Model
from .venom import Venom
from .jelly import Jelly
from .hair import Hair, Fur, Whiskers
from .blood import BloodVessels, Blood, BloodCell
from .skeleton import BoneCell, Bone, Bones, MuscleCell, Muscles, Fat, Skeleton
from .skin import SkinCell, DeadSkin, Pores, Scar, Skin, Scales, Exoskeleton
from .body_parts import BodyPart, Flesh, SoftFlesh, WeirdOrgan
from models.v5.life.animal_body.head.eye import EyeFlesh, SimpleEye
from .limb import Limb, Wing, Tail, Tentacle
from .insect import InsectLeg, InsectClaw, Stinger, Antenna, InsectWing
from .fish import FishFin, FishTail, FishSkin
from .reptile import ReptileWing, ReptileHead, ReptileLeg, ReptileBody, ReptileBodyPart
from .bird import BirdLimb, BirdWing, BirdLeg, BirdTail, Beak, BirdHead, BirdBody
from .mammal import MammalLeg, MammalHead, MammalBody
from .cetacean import CetaceanFin, CetaceanFlipper
from .head import *


# TODO: Remove it


class AnimalBody(Model):
    pass


class CrustaceanLeg(Model):
    pass


class CrustaceanClaw(Model):
    pass


class CrustaceanShell(Model):
    pass


class WeirdSoftOrgan(Model):
    pass


class WeirdHardOrgan(Model):
    pass

