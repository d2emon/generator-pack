from genesys.nested.factories.nested_factory import NestedFactory
from models.v5 import life
from utils.nested import select_item
from .blood import BloodVesselsFactory
from .skeleton import BonesFactory, MuscleFactory, FatFactory
from .skin import SkinFactory

# ??? 
from ..single_celled import BacteriaFactory


class BodyPartFactory(NestedFactory):
    model = life.BodyPart

    has_bones = True
    has_skin = True

    def bacterii(self):
        yield BacteriaFactory.probable(30)
        yield BacteriaFactory.probable(10)

    def blood(self):
        yield BloodVesselsFactory.one()

    def bones(self):
        if self.has_bones:
            yield BonesFactory.one()

    def fat(self):
        yield FatFactory.one()

    def muscles(self):
        yield MuscleFactory.one()

    def skin(self):
        if self.has_skin:
            yield SkinFactory.one()

    def children(self):
        yield from self.bacterii()
        yield from self.skin()
        yield from self.blood()
        yield from self.bones()
        yield from self.fat()
        yield from self.muscles()


class SoftBodyPartFactory(BodyPartFactory):
    has_bones = False
    has_skin = True


class SkinlessBodyPartFactory(BodyPartFactory):
    has_bones = True
    has_skin = False


class SkinlessSoftBodyPartFactory(BodyPartFactory):
    has_bones = False
    has_skin = False


class FleshFactory(SkinlessBodyPartFactory):
    # TODO: Refactor it
    default_model = life.Flesh
    has_bones = True


class SoftFleshFactory(FleshFactory):
    # TODO: Refactor it
    default_model = life.Flesh
    has_bones = False


class WeirdSoftOrganFactory(SkinlessSoftBodyPartFactory):
    # TODO: Refactor it
    default_model = life.WeirdOrgan

    descriptions = [
        "fleshy", "thick", "slimy", "scaly", "furry", "fuzzy", "feathery", "sharp", "pointy", "thorny", "bulbous",
        "leathery", "hidden", "soft", "bubbling", "distorted", "shapeless", "porous", "spongiform", "liquid-filled",
        "foamy", "smoking", "oozing", "drooling", "shivering", "quivering", "pulsing",
    ]
    names = [
        "grasper", "tendril", "stinger", "claw", "tentacle", "sac", "egg sac", "pouch", "organ", "specialized organ",
        "bulb", "brain bulb", "gland", "epiderm", "sucker", "pod", "pseudolimb", "nervous bulb", "external muscle",
        "structure", "orifice", "proboscis", "tail",
    ]

    def generate_name(self):
        return f'{select_item(*self.descriptions)} {select_item(*self.names)}'


class WeirdHardOrganFactory(SkinlessBodyPartFactory):
    # TODO: Refactor it
    default_model = life.WeirdOrgan

    descriptions = [
        "fleshy", "thick", "slimy", "scaly", "furry", "fuzzy", "sharp", "pointy", "thorny", "bulbous", "hidden",
        "flexible", "plated", "armored", "metallic", "distorted", "shapeless", "porous", "spongiform", "liquid-filled",
        "foamy", "smoking", "oozing", "drooling",
    ]
    names = [
        "carapace", "shell", "bone structure", "skull", "grasper", "stinger", "claw", "organ", "specialized organ",
        "sucker", "pod", "pseudolimb", "structure",
    ]

    def generate_name(self):
        return f'{select_item(*self.descriptions)} {select_item(*self.names)}'
