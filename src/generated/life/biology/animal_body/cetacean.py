from .body_part import Limb
from generated.life.body.body import BodyPart, Muscles, Skin


class CetaceanFlipper(Limb):
    default_name = 'flipper'

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Muscles
                yield Skin


class CetaceanFin(Limb):
    default_name = 'fin'

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Muscles
                yield Skin
