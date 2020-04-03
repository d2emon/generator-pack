from genesys.nested.models import Model
from genesys.nested.models.models.chemistry import OrganicMatter
from ..body_parts import BodyPart, SoftBodyPart
from .hair import Hair


class Boogers(Model):
    matter = Model.child_property(OrganicMatter)

    class ChildrenFactory(Model.ChildrenFactory):
        def children_classes(self):
            yield OrganicMatter


class NostrilHair(Hair):
    pass


class Nostril(SoftBodyPart):
    hair = SoftBodyPart.child_property(Hair)
    boogers = SoftBodyPart.children_property(Boogers)

    class ChildrenFactory(SoftBodyPart.ChildrenFactory):
        def children_classes(self):
            yield NostrilHair
            yield from Boogers.multiple(0, 1)
            yield from super().children_classes()


class Nose(BodyPart):
    nostrils = BodyPart.children_property(Nostril)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        def children_classes(self):
            yield from Nostril.multiple(2)
            yield from super().children_classes()
