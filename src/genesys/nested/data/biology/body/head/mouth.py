from ....chemistry import elements, Atom
from ..body_parts import SoftBodyPart, BodyPart
from ..skeleton import Muscles


class Tongue(SoftBodyPart):
    class ChildrenFactory(SoftBodyPart.ChildrenFactory):
        def children_classes(self):
            yield Muscles


class Teeth(BodyPart):
    elements = SoftBodyPart.children_property(Atom)

    class ChildrenFactory(SoftBodyPart.ChildrenFactory):
        def children_classes(self):
            yield elements['Ca']
            yield elements['P']


class Mouth(SoftBodyPart):
    teeth = SoftBodyPart.child_property(Teeth)
    tongue = SoftBodyPart.child_property(Tongue)

    class ChildrenFactory(SoftBodyPart.ChildrenFactory):
        def children_classes(self):
            yield Teeth
            yield Tongue
