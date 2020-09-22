from generated.nested_v2.models import Mind
from genesys.nested.factories.thing_builder import ListFactory
from ..animal_body import AnimalBody, SimpleEye, CrustaceanLeg, CrustaceanClaw, CrustaceanShell, Tentacle, FishFin, \
    Stinger, Exoskeleton, Fur, Scales, Mouth, Beak, Skull, WeirdSoftOrgan, WeirdHardOrgan
from ..body import Eye
from ..mind import SimpleThoughts, Thought
from ..organism import Organism


class MonsterBody(AnimalBody):
    liquid = AnimalBody.child_property(Mind)

    class Factory(AnimalBody.Factory):
        class ChildrenFactory(AnimalBody.Factory.ChildrenFactory):
            fins = property(lambda self: ListFactory([
                Tentacle.multiple(0, 6),
                FishFin.multiple(0, 4),
                [],
                [],
            ]))
            claws = property(lambda self: ListFactory([
                CrustaceanClaw.multiple(0, 4),
                [],
            ]))
            legs = property(lambda self: ListFactory([
                CrustaceanLeg.multiple(0, 8),
                [],
            ]))
            shells = property(lambda self: ListFactory([
                CrustaceanShell,
                Scales,
                Fur,
                Exoskeleton,
                None,
            ]))
            mouths = property(lambda self: ListFactory([
                Mouth.multiple(1, 2),
                Beak.multiple(1, 2),
            ]))
            eyes = property(lambda self: ListFactory([
                Eye.multiple(1, 8),
                SimpleEye.multiple(1, 8),
                [],
                [],
            ]))

            def builders(self):
                yield from next(self.fins)
                yield Stinger.probable(20)
                yield from next(self.claws)
                yield from next(self.legs)
                yield next(self.shells)
                yield from next(self.mouths)
                yield Skull.probable(80)
                yield from next(self.eyes)
                yield from WeirdSoftOrgan.multiple(0, 4)
                yield from WeirdHardOrgan.multiple(0, 4)


class MonsterThought(Thought):
    pass


class MonsterThoughts(SimpleThoughts):
    class Factory(SimpleThoughts.Factory):
        class ChildrenFactory(SimpleThoughts.Factory.ChildrenFactory):
            def builders(self):
                yield from MonsterThought.multiple(1, 2)


class Monster(Organism):
    class Factory(Organism.Factory):
        class ChildrenFactory(Organism.Factory.ChildrenFactory):
            body_class = MonsterBody
            mind_class = MonsterThoughts
