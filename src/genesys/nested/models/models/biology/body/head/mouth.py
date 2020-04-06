from genesys.nested.models.models.chemistry import elements, Atom
from ..body_parts import SoftBodyPart, BodyPart
from ..skeleton import Muscles


class Tongue(SoftBodyPart):
    class Factory(SoftBodyPart.Factory):
        class ChildrenFactory(SoftBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Muscles


class Teeth(BodyPart):
    elements = BodyPart.children_property(Atom)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield elements['Ca']
                yield elements['P']


class Mouth(SoftBodyPart):
    teeth = SoftBodyPart.child_property(Teeth)
    tongue = SoftBodyPart.child_property(Tongue)

    class Factory(SoftBodyPart.Factory):
        class ChildrenFactory(SoftBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Teeth
                yield Tongue
