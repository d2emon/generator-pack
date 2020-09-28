"""
- Abomination
- Abomination Psyche
- Abomination Thoughts
- Abomination Thought
- Abomination Body
- Abomination Head
- Abomination Torso
"""
from genesys.nested.factories.v2.thing_builder import ThingBuilder
from ..body import Body, Head, Mouth, Nose, Eye, Ear, Skull, HeadHair, Torso, Chest, Pelvis, Arm, Leg
from ..animal_body import WeirdHardOrgan, WeirdSoftOrgan, CrustaceanClaw, Stinger
from ..mind import Psyche, Thoughts, Thought, Memories
from generated.nested_v2.models.person import Person
from genesys.nested.data import lookups


class AbominationHead(Head):
    soft_organs = Body.children_property(WeirdSoftOrgan)
    hard_organs = Body.children_property(WeirdHardOrgan)

    default_name = 'misshapen head'

    class Factory(Head.Factory):
        class ChildrenFactory(Head.Factory.ChildrenFactory):
            @classmethod
            def fill_head(cls):
                yield from Mouth.multiple(0, 2)
                yield from Nose.multiple(0, 2)
                yield from Eye.multiple(0, 8)
                yield from Ear.multiple(0, 4)
                yield Skull.probable(90)
                yield WeirdSoftOrgan.probable(20)
                yield WeirdHardOrgan.probable(20)
                yield HeadHair.probable(65)


class AbominationTorso(Torso):
    soft_organs = Torso.children_property(WeirdSoftOrgan)
    hard_organs = Torso.children_property(WeirdHardOrgan)

    default_name = 'misshapen torso'

    class Factory(Torso.Factory):
        class ChildrenFactory(Torso.Factory.ChildrenFactory):
            def builders(self):
                yield Chest
                yield Chest.probable(10)
                yield Pelvis
                yield Pelvis.probable(10)
                yield WeirdSoftOrgan.probable(20)
                yield WeirdHardOrgan.probable(20)
                yield from super().builders()


class AbominationBody(Body):
    claws = Body.children_property(CrustaceanClaw)
    stingers = Body.children_property(Stinger)
    soft_organs = Body.children_property(WeirdSoftOrgan)
    hard_organs = Body.children_property(WeirdHardOrgan)

    default_name = 'misshapen body'

    class Factory(Body.Factory):
        class ChildrenFactory(Body.Factory.ChildrenFactory):
            arms = [
                Arm.multiple(0, 8),
                Arm.multiple(0, 4),
            ]
            legs = [
                Leg.multiple(0, 8),
                Leg.multiple(0, 4),
            ]

            def builders(self):
                yield AbominationHead
                yield AbominationHead.probable(5)
                yield AbominationTorso
                for arm in self.arms:
                    yield from Body.BaseFactory(arm).next()
                for leg in self.legs:
                    yield from Body.BaseFactory(leg).next()
                yield CrustaceanClaw.probable(2)
                yield Stinger.probable(2)
                yield WeirdSoftOrgan.probable(10)
                yield WeirdSoftOrgan.probable(10)
                yield WeirdHardOrgan.probable(10)
                yield WeirdHardOrgan.probable(10)


class AbominationThought(Thought):
    class Factory(Thought.Factory):
        class DataProvider:
            abomination_thought = lookups.abomination_thoughts

        class BaseFactory(ThingBuilder.BaseFactory):
            data = property(lambda self: self.provider.abomination_thought)


class AbominationThoughts(Thoughts):
    default_name = 'thoughts'

    class Factory(Thoughts.Factory):
        class ChildrenFactory(Thoughts.Factory.ChildrenFactory):
            @classmethod
            def fill_thoughts(cls):
                yield AbominationThought


class AbominationPsyche(Psyche):
    default_name = 'psyche'

    class Factory(Psyche.Factory):
        class ChildrenFactory(Psyche.Factory.ChildrenFactory):
            def builders(self):
                yield AbominationThoughts
                yield Memories


class Abomination(Person):
    default_name = '*PERSON*| (abomination)'

    class Factory(Person.Factory):
        class ChildrenFactory(Person.Factory.ChildrenFactory):
            def builders(self):
                yield AbominationBody
                yield AbominationPsyche
