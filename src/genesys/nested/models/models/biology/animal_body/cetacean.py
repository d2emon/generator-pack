from ..body import BodyPart, Muscles, Skin


class CetaceanFlipper(BodyPart):
    default_name = 'flipper'

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Muscles
                yield Skin


class CetaceanFin(BodyPart):
    default_name = 'fin'

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield Muscles
                yield Skin
