from ...unknown import Lint, Pasta, Sweat
from .body_parts import BodyPart, SoftBodyPart
from .skin import Skin


class Butt(BodyPart):
    pasta = BodyPart.children_property(Pasta)
    sweat = BodyPart.children_property(Sweat)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield Pasta.probable(0.01)
            yield Sweat.probable(50)
            yield from super().children_classes()


class NaughtyBits(SoftBodyPart):
    pass


class Pelvis(BodyPart):
    naughty_bits = BodyPart.children_property(NaughtyBits)
    butt = BodyPart.child_property(Butt)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield NaughtyBits
            yield Butt
            yield from super().children_classes()


class Nipple(BodyPart):
    skin = BodyPart.children_property(Skin)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield Skin


class Bellybutton(BodyPart):
    skin = BodyPart.children_property(Skin)
    lint = BodyPart.child_property(Lint)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield Skin
            yield from Lint.multiple(0, 1)


class Chest(BodyPart):
    nipples = BodyPart.children_property(Nipple)
    bellybutton = BodyPart.child_property(Bellybutton)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield from Nipple.multiple(2)
            yield Bellybutton
            yield from super().children_classes()


class Torso(BodyPart):
    chest = BodyPart.children_property(Chest)
    pelvis = BodyPart.children_property(Pelvis)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        @classmethod
        def fill_torso(cls):
            yield Chest
            yield Pelvis

        def children_classes(self):
            yield from self.fill_torso()
            yield from super().children_classes()
