"""
- Teeth
- SimpleMouth ???
- Tongue
- Mouth
"""
from ....materials import Molecule
from ..body_parts import BodyPart


class Teeth(BodyPart):
    elements = BodyPart.children_property(Molecule)


class SimpleMouth(BodyPart):
    default_name = 'mouth'

    teeth = BodyPart.children_property(Teeth)


class Tongue(BodyPart):
    pass


class Mouth(SimpleMouth):
    tongue = BodyPart.child_property(Tongue)
