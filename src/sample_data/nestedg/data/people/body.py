"""
Body stuff
"""
from nestedg.data import unknown, materials
from nestedg.data.materials import elements
from nestedg.model import Model
from nestedg.data.cells import Cell


class Keratin(NestedItem):
    @classmethod
    def get_children(cls):
        yield materials.Proteins


class Sweat(NestedItem):
    @classmethod
    def get_children(cls):
        yield materials.Water
        yield materials.Salt
        yield materials.Glucids


# ----


class Fat(NestedItem):
    @classmethod
    def get_children(cls):
        yield materials.Lipids


class MuscleCell(Cell):
    @classmethod
    def get_name(cls):
        return 'muscle cells'


class Muscles(NestedItem):
    @classmethod
    def get_children(cls):
        yield MuscleCell


class BoneCell(Cell):
    @classmethod
    def get_name(cls):
        return 'bone cells'


class Bones(NestedItem):
    @classmethod
    def get_children(cls):
        yield BoneCell
        yield elements.Calcium


class Bone(Bones):
    @classmethod
    def get_name(cls):
        return 'bone'


class SkinCell(Cell):
    @classmethod
    def get_name(cls):
        return 'skin cells'


class DeadSkin(SkinCell):
    pass


class Pores(NestedItem):
    @classmethod
    def get_children(cls):
        yield unknown.Bacteria.multiple(1, 3)
        yield SkinCell
        yield DeadSkin.probable(50)
        yield Sweat.probable(40)


class Scar(NestedItem):
    @classmethod
    def get_children(cls):
        yield DeadSkin


class Dandruff(NestedItem):
    @classmethod
    def get_children(cls):
        yield DeadSkin


class Skin(NestedItem):
    @classmethod
    def get_children(cls):
        yield unknown.Bacteria.multiple(1, 3)
        yield Scar.probable(0.5)
        yield Pores
        yield SkinCell
        yield DeadSkin
        yield unknown.Dust.probable(20)
        yield Sweat.probable(20)


class BloodCell(Cell):
    @classmethod
    def get_name(cls):
        return 'blood cells'


class Blood(NestedItem):
    @classmethod
    def get_children(cls):
        yield BloodCell


class BloodVessels(NestedItem):
    @classmethod
    def get_children(cls):
        yield unknown.Bacteria.probable(30)
        yield Blood


class BodyPart(NestedItem):
    has_bones = True
    has_skin = True

    @classmethod
    def get_children(cls):
        yield unknown.Bacteria.probable(30)
        yield unknown.Bacteria.probable(10)
        if cls.has_skin:
            yield Skin
        yield BloodVessels
        if cls.has_bones:
            yield Bones
        yield Fat
        yield Muscles

    @classmethod
    def get_name(cls):
        return 'body part'


class SoftBodyPart(BodyPart):
    has_bones = False
    has_skin = True


class SkinlessBodyPart(BodyPart):
    has_bones = True
    has_skin = False


class SkinlessSoftBodyPart(BodyPart):
    has_bones = False
    has_skin = False


# ----


class Tongue(SoftBodyPart):
    @classmethod
    def get_children(cls):
        yield Muscles


class Teeth(SoftBodyPart):
    @classmethod
    def get_children(cls):
        yield elements.Calcium
        yield elements.Phosphorus


class Mouth(SoftBodyPart):
    @classmethod
    def get_children(cls):
        yield Teeth
        yield Tongue


class Boogers(NestedItem):
    @classmethod
    def get_children(cls):
        yield unknown.OrganicMatter


class Hair(NestedItem):
    @classmethod
    def get_children(cls):
        yield unknown.Bacteria.probable(30)
        yield Keratin


class HeadHair(Hair):
    colors = ['brown', 'black', 'gray', 'light', 'blond', 'red', 'dark']

    @classmethod
    def get_children(cls):
        yield Dandruff
        yield from super().get_children()

    @classmethod
    def get_name(cls):
        return '{} hair'.format(cls.choice(cls.colors))


class NostrilHair(Hair):
    pass


class Nostril(SoftBodyPart):
    @classmethod
    def get_children(cls):
        yield NostrilHair
        yield from Boogers.multiple(0, 1)
        yield from super().get_children()


class Nose(BodyPart):
    @classmethod
    def get_children(cls):
        yield from Nostril.multiple(2)
        yield from super().get_children()


class BrainCell(Cell):
    @classmethod
    def get_name(cls):
        return 'brain cells'


class Brain(SoftBodyPart):
    @classmethod
    def get_children(cls):
        yield unknown.Bacteria.probable(20)
        yield BrainCell


class Skull(Bones):
    @classmethod
    def get_children(cls):
        yield Brain
        yield from super().get_children()


class Ear(SoftBodyPart):
    pass


class Tear(NestedItem):
    @classmethod
    def get_children(cls):
        yield materials.Water
        yield materials.Salt


class Eyelashes(Hair):
    pass


class EyeFlesh(BodyPart):
    @classmethod
    def get_children(cls):
        yield materials.Water
        yield BloodVessels
        yield Fat

    @classmethod
    def get_name(cls):
        return 'eyeball'


class Eye(BodyPart):
    @classmethod
    def get_children(cls):
        yield Eyelashes
        yield EyeFlesh
        yield Tear.probable(2)


class Head(BodyPart):
    @classmethod
    def get_children(cls):
        yield Mouth
        yield Nose
        yield Eye.probable(99)
        yield Eye.probable(99)
        yield from Ear.multiple(2)
        yield Skull
        yield HeadHair.probable(85)
        yield from super().get_children()


class Knee(BodyPart):
    pass


class Toenail(BodyPart):
    @classmethod
    def get_children(cls):
        yield unknown.Dust.probable(40)
        yield Keratin


class Toe(BodyPart):
    @classmethod
    def get_children(cls):
        yield Toenail
        yield from super().get_children


class Foot(BodyPart):
    @classmethod
    def get_children(cls):
        yield from Toe.multiple(5)
        yield Sweat.probable(30)
        yield from super().get_children


class Leg(BodyPart):
    @classmethod
    def get_children(cls):
        yield Foot
        yield Knee
        yield from super().get_children


class ArmpitHair(Hair):
    @classmethod
    def get_name(cls):
        return 'hair'


class Armpit(SoftBodyPart):
    @classmethod
    def get_children(cls):
        yield ArmpitHair
        yield Sweat.probable(80)
        yield from super().get_children


class Elbow(BodyPart):
    pass


class Fingernail(BodyPart):
    @classmethod
    def get_children(cls):
        yield unknown.Dust.probable(30)
        yield Keratin


class Finger(BodyPart):
    @classmethod
    def get_children(cls):
        yield Fingernail
        yield from super().get_children


class Hand(BodyPart):
    @classmethod
    def get_children(cls):
        yield from Finger.multiple(5)
        yield from super().get_children


class Arm(BodyPart):
    @classmethod
    def get_children(cls):
        yield Hand
        yield Elbow
        yield Armpit
        yield from super().get_children


class Butt(BodyPart):
    @classmethod
    def get_children(cls):
        yield unknown.Pasta.probable(0.01)
        yield Sweat.probable(50)
        yield from super().get_children


class NaughtyBits(SoftBodyPart):
    pass


class Pelvis(BodyPart):
    @classmethod
    def get_children(cls):
        yield NaughtyBits
        yield Butt
        yield from super().get_children()


class Nipple(BodyPart):
    @classmethod
    def get_children(cls):
        yield Skin


class Bellybutton(BodyPart):
    @classmethod
    def get_children(cls):
        yield Skin
        yield from unknown.Lint.multiple(0, 1)


class Chest(BodyPart):
    @classmethod
    def get_children(cls):
        yield from Nipple.multiple(2)
        yield Bellybutton
        yield from super().get_children()


class Torso(BodyPart):
    @classmethod
    def get_children(cls):
        yield Chest
        yield Pelvis
        yield from super().get_children()


class Body(NestedItem):
    @classmethod
    def get_children(cls):
        yield Head
        yield Torso
        yield Arm.probable(99)
        yield Arm.probable(99)
        yield Leg.probable(99)
        yield Leg.probable(99)
