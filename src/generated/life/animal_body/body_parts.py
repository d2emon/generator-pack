"""
- BodyPart
"""
from genesys.model.model import Model
from ...materials import Sweat
from .blood import BloodVessels
from .skin import Skin
from .skeleton import Bones, Muscles, Fat


class BodyPart(Model):
    # bacterias = Model.children_property(Bacteria)
    skin = Model.child_property(Skin)
    blood_vessels = Model.child_property(BloodVessels)
    bones = Model.child_property(Bones)
    fat = Model.child_property(Fat)
    muscles = Model.child_property(Muscles)
    sweat = Model.child_property(Sweat)


class Flesh(BodyPart):
    default_name = 'flesh'


class SoftFlesh(Flesh):
    default_name = 'flesh'


class WeirdHardOrgan(SkinlessBodyPart):
    class Factory(SkinlessBodyPart.Factory):
        class DataProvider:
            organ_styles = [
                'fleshy', 'thick', 'slimy', 'scaly', 'furry', 'fuzzy', 'sharp', 'pointy', 'thorny', 'bulbous', 'hidden',
                'flexible', 'plated', 'armored', 'metallic', 'distorted', 'shapeless', 'porous', 'spongiform',
                'liquid-filled', 'foamy', 'smoking', 'oozing', 'drooling',
            ]
            organs = [
                'carapace', 'shell', 'bone structure', 'skull', 'grasper', 'stinger', 'claw', 'organ', 'specialized organ',
                'sucker', 'pod', 'pseudolimb', 'structure',
            ]

        class BaseFactory(SkinlessBodyPart.BaseFactory):
            def __next__(self):
                return "{} {}".format(
                    SkinlessBodyPart.BaseFactory(self.provider.organ_styles),
                    SkinlessBodyPart.BaseFactory(self.provider.organs),
                )


class WeirdSoftOrgan(SkinlessSoftBodyPart):
    class Factory(SkinlessSoftBodyPart.Factory):
        class DataProvider:
            organ_styles = [
                'fleshy', 'thick', 'slimy', 'scaly', 'furry', 'fuzzy', 'feathery', 'sharp', 'pointy', 'thorny', 'bulbous',
                'leathery', 'hidden', 'soft', 'bubbling', 'distorted', 'shapeless', 'porous', 'spongiform',
                'liquid-filled', 'foamy', 'smoking', 'oozing', 'drooling', 'shivering', 'quivering', 'pulsing',
            ]
            organs = [
                'grasper', 'tendril', 'stinger', 'claw', 'tentacle', 'sac', 'egg sac', 'pouch', 'organ',
                'specialized organ', 'bulb', 'mind bulb', 'gland', 'epiderm', 'sucker', 'pod', 'pseudolimb',
                'nervous bulb', 'external muscle', 'structure', 'orifice', 'proboscis', 'tail',
            ]

        class BaseFactory(SkinlessBodyPart.BaseFactory):
            def __next__(self):
                return "{} {}".format(
                    SkinlessBodyPart.BaseFactory(self.provider.organ_styles),
                    SkinlessBodyPart.BaseFactory(self.provider.organs),
                )
