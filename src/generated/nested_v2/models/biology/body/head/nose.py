from genesys.nested.factories.thing_builder import ThingBuilder
from genesys.nested.models import Model
from generated.chemistry import OrganicMatter
from ..body_parts import BodyPart, SoftBodyPart
from .hair import Hair


class Boogers(Model):
    matter = Model.child_property(OrganicMatter)

    class Factory(ThingBuilder):
        class ChildrenFactory(ThingBuilder.ChildrenFactory):
            def builders(self):
                yield OrganicMatter


class NostrilHair(Hair):
    pass


class Nostril(SoftBodyPart):
    hair = SoftBodyPart.child_property(Hair)
    boogers = SoftBodyPart.children_property(Boogers)

    class Factory(SoftBodyPart.Factory):
        class ChildrenFactory(SoftBodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield NostrilHair
                yield from Boogers.multiple(0, 1)
                yield from super().builders()


class Nose(BodyPart):
    nostrils = BodyPart.children_property(Nostril)

    class Factory(BodyPart.Factory):
        class ChildrenFactory(BodyPart.Factory.ChildrenFactory):
            def builders(self):
                yield from Nostril.multiple(2)
                yield from super().builders()
