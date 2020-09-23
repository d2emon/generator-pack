from generated.materials.chemistry import elements, Atom
from ..body_parts import SoftBodyPart, BodyPart
from ..skeleton import Muscles
from ...animal_body import SimpleMouth


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


class Mouth(SimpleMouth):
    teeth = SimpleMouth.child_property(Teeth)
    tongue = SimpleMouth.child_property(Tongue)

    class Factory(SimpleMouth.Factory):
        class ChildrenFactory(SimpleMouth.Factory.ChildrenFactory):
            def builders(self):
                yield Teeth
                yield Tongue
