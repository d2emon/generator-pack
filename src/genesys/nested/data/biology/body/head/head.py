from ..body_parts import BodyPart
from .eye import Eye
from .ear import Ear
from .skull import Skull
from .hair import Hair, HeadHair
from .nose import Nose
from .mouth import Mouth


class Head(BodyPart):
    mouths = BodyPart.children_property(Mouth)
    noses = BodyPart.children_property(Nose)
    eyes = BodyPart.children_property(Eye)
    ears = BodyPart.children_property(Ear)
    skull = BodyPart.child_property(Skull)
    hair = BodyPart.child_property(Hair)

    class ChildrenFactory(BodyPart.ChildrenFactory):
        @classmethod
        def fill_head(cls):
            yield Mouth
            yield Nose
            yield Eye.probable(99)
            yield Eye.probable(99)
            yield from Ear.multiple(2)
            yield Skull
            yield HeadHair.probable(85)

        def children_classes(self):
            yield from self.fill_head()
            yield from super().children_classes()
