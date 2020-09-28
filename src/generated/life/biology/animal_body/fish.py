from .body_part import Scales, Limb, Tail
from generated.life.body.body import Muscles, Skin


class FishFin(Limb):
    scales = Limb.child_property(Scales)

    default_name = 'fin'

    class Factory(Limb.Factory):
        class ChildrenFactory(Limb.Factory.ChildrenFactory):
            def builders(self):
                yield Muscles
                yield Scales


class FishTail(Tail):
    scales = Tail.child_property(Scales)

    default_name = 'tail'

    class Factory(Tail.Factory):
        class ChildrenFactory(Tail.Factory.ChildrenFactory):
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
