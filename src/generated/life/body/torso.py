"""
- Butt
- NaughtyBits
- Pelvis
- Nipple
- Bellybutton
- Chest
- Torso
"""
from .body_parts import BodyPart


class Butt(BodyPart):
    # pasta = BodyPart.children_property(Pasta)
    pass


class NaughtyBits(BodyPart):
    pass


class Pelvis(BodyPart):
    naughty_bits = BodyPart.children_property(NaughtyBits)
    butt = BodyPart.child_property(Butt)


class Nipple(BodyPart):
    pass


class Bellybutton(BodyPart):
    # lint = BodyPart.child_property(Lint)
    pass


class Chest(BodyPart):
    nipples = BodyPart.children_property(Nipple)
    bellybutton = BodyPart.child_property(Bellybutton)


class Torso(BodyPart):
    chest = BodyPart.children_property(Chest)
    pelvis = BodyPart.children_property(Pelvis)
