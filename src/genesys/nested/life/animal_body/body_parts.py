from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from ..single_celled import BacteriaFactory
from .blood import BloodVesselsFactory
from .skeleton import BonesFactory, MuscleFactory, FatFactory
from .skin import SkinFactory


class BodyPartFactory(Factory):
    default_model = life.BodyPart

    has_bones = True
    has_skin = True

    def children(self):
        yield BacteriaFactory().probable(30)
        yield BacteriaFactory().probable(10)
        if self.has_skin:
            yield SkinFactory()
        yield BloodVesselsFactory()
        if self.has_bones:
            yield BonesFactory()
        yield FatFactory()
        yield MuscleFactory()


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
    default_model = life.Flesh
    has_bones = True


class SoftFleshFactory(FleshFactory):
    default_model = life.Flesh
    has_bones = False


class WeirdSoftOrganFactory(SkinlessSoftBodyPartFactory):
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
        return f'{self.select_item(*self.descriptions)} {self.select_item(*self.names)}'


class WeirdHardOrganFactory(SkinlessBodyPartFactory):
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
        return f'{self.select_item(*self.descriptions)} {self.select_item(*self.names)}'
