from genesys.nested.models.models.unknown import Feathers
from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from ..body import Bones, BodyPart, SkinlessBodyPart, SkinlessSoftBodyPart, EyeFlesh, Teeth, Skin, Nose
from ...chemistry import Keratin


class Skeleton(Model):
    bones = Model.child_property(Bones)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield Bones


class Scales(Skin):
    keratin = Skin.child_property(Keratin)

    class Factory(Skin.Factory):
        class ChildrenFactory(Skin.Factory.ChildrenFactory):
            def builders(self):
                yield Keratin


class Flesh(SkinlessBodyPart):
    default_name = 'flesh'


class SoftFlesh(SkinlessSoftBodyPart):
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


class SimpleEye(EyeFlesh):
    default_name = 'eye'


class Wing(BodyPart):
    feathers = Model.child_property(Feathers)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            has_feathers = True

            def builders(self):
                if self.has_feathers:
                    yield Feathers
                yield from super().builders()


class Tentacle(SkinlessSoftBodyPart):
    pass


class SimpleMouth(SkinlessSoftBodyPart):
    default_name = 'Mouth'

    class Factory(SkinlessSoftBodyPart.Factory):
        class ChildrenFactory(SkinlessSoftBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Teeth
                yield from super().builders()


class Snout(Nose):
    pass


class Tail(BodyPart):
    pass