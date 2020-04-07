from .body_part import Scales
from ..body import BodyPart, Muscles, Skin


class FishFin(BodyPart):
    scales = BodyPart.child_property(Scales)

    default_name = 'fin'

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Muscles
                yield Scales


class FishTail(BodyPart):
    scales = BodyPart.child_property(Scales)

    default_name = 'tail'

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Muscles
                yield Scales


class FishSkin(Skin):
    scales = Skin.child_property(Scales)

    default_name = 'skin'

    class Factory(Skin.Factory):
        class ChildrenFactory(Skin.Factory.ChildrenFactory):
            def builders(self):
                yield Scales
