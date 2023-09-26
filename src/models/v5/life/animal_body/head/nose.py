"""
- Boogers
- NostrilHair
- Nostril
- Nose
- Snout ?
"""
from models.tree_model import TreeModel as Model
from ....materials import OrganicMatter
from ..body_parts import BodyPart
from ..hair import Hair


class Boogers(Model):
    matter = Model.child_property(OrganicMatter)


class NostrilHair(Hair):
    pass


class Nostril(BodyPart):
    hair = BodyPart.child_property(Hair)
    boogers = BodyPart.children_property(Boogers)


class Nose(BodyPart):
    nostrils = BodyPart.children_property(Nostril)


class Snout(Nose):
    pass
