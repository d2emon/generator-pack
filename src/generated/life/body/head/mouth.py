"""
- Tongue
- Teeth
- Mouth
"""
from ....materials import Molecule
from ...animal_body.body_parts import BodyPart


class Tongue(BodyPart):
    pass


class Teeth(BodyPart):
    elements = BodyPart.children_property(Molecule)


class Mouth(BodyPart):
    teeth = BodyPart.child_property(Teeth)
    tongue = BodyPart.child_property(Tongue)
