from generated.nested_v2.models import Lint, Pasta
from .body_parts import BodyPart, SoftBodyPart
from .skin import Skin
from generated.chemistry import Sweat


class Butt(BodyPart):
    pasta = BodyPart.children_property(Pasta)
    sweat = BodyPart.children_property(Sweat)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Pasta.probable(0.01)
                yield Sweat.probable(50)
                yield from super().builders()


class NaughtyBits(SoftBodyPart):
    pass


class Pelvis(BodyPart):
    naughty_bits = BodyPart.children_property(NaughtyBits)
    butt = BodyPart.child_property(Butt)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield NaughtyBits
                yield Butt
                yield from super().builders()


class Nipple(BodyPart):
    skin = BodyPart.children_property(Skin)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Skin


class Bellybutton(BodyPart):
    skin = BodyPart.children_property(Skin)
    lint = BodyPart.child_property(Lint)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Skin
                yield from Lint.multiple(0, 1)


class Chest(BodyPart):
    nipples = BodyPart.children_property(Nipple)
    bellybutton = BodyPart.child_property(Bellybutton)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield from Nipple.multiple(2)
                yield Bellybutton
                yield from super().builders()


class Torso(BodyPart):
    chest = BodyPart.children_property(Chest)
    pelvis = BodyPart.children_property(Pelvis)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            @classmethod
            def fill_torso(cls):
                yield Chest
                yield Pelvis

            def builders(self):
                yield from self.fill_torso()
                yield from super().builders()
