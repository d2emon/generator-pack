"""
- Boogers
- NostrilHair
- Nostril
- Nose
"""
from genesys.model.model import Model
from ....materials import OrganicMatter
from ...animal_body.body_parts import BodyPart
from ...animal_body.hair import Hair


class Boogers(Model):
    matter = Model.child_property(OrganicMatter)


class NostrilHair(Hair):
    pass


class Nostril(BodyPart):
    hair = BodyPart.child_property(Hair)
    boogers = BodyPart.children_property(Boogers)


class Nose(BodyPart):
    nostrils = BodyPart.children_property(Nostril)
