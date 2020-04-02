"""
- Abomination
- Abomination Psyche
- Abomination Thoughts
- Abomination Thought
- Abomination Body
- Abomination Head
- Abomination Torso
"""
from ...unknown import Psyche, Memories, Thoughts, Thought, CrustaceanClaw, Stinger, WeirdHardOrgan, WeirdSoftOrgan
from ...space import BlackHole
from ..body import Person, Body, Head, Mouth, Nose, Eye, Ear, Skull, HeadHair, Torso, Chest, Pelvis, Arm, Leg
from ... import lookups


class AbominationHead(Head):
    class NameFactory(Head.NameFactory):
        default = 'misshapen head'

    class ChildrenFactory(Head.ChildrenFactory):
        soft_organs = Body.children_property(WeirdSoftOrgan)
        hard_organs = Body.children_property(WeirdHardOrgan)

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

    class NameFactory(Torso.NameFactory):
        default = 'misshapen torso'

    class ChildrenFactory(Torso.ChildrenFactory):
        def children_classes(self):
            yield Chest
            yield Chest.probable(10)
            yield Pelvis
            yield Pelvis.probable(10)
            yield WeirdSoftOrgan.probable(20)
            yield WeirdHardOrgan.probable(20)
            yield from super().children_classes()


class AbominationBody(Body):
    class NameFactory(Body.NameFactory):
        default = 'misshapen body'

    class ChildrenFactory(Body.ChildrenFactory):
        claws = Body.children_property(CrustaceanClaw)
        stingers = Body.children_property(Stinger)
        soft_organs = Body.children_property(WeirdSoftOrgan)
        hard_organs = Body.children_property(WeirdHardOrgan)

        arms = [
            Arm.multiple(0, 8),
            Arm.multiple(0, 4),
        ]
        legs = [
            Leg.multiple(0, 8),
            Leg.multiple(0, 4),
        ]

        def children_classes(self):
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
    class BaseFactory(Thought.BaseFactory):
        default = lookups.abomination_thoughts


class AbominationThoughts(Thoughts):
    class NameFactory(Thoughts.NameFactory):
        default = 'thoughts'

    class ChildrenFactory(Thoughts.ChildrenFactory):
        def children_classes(self):
            yield BlackHole.probable(0.01)
            yield AbominationThought


class AbominationPsyche(Psyche):
    class NameFactory(Psyche.NameFactory):
        default = 'psyche'

    class ChildrenFactory(Psyche.ChildrenFactory):
        def children_classes(self):
            yield AbominationThoughts
            yield Memories


class Abomination(Person):
    class NameFactory(Person.NameFactory):
        default = '*PERSON*| (abomination)'

    class ChildrenFactory(Person.ChildrenFactory):
        def children_classes(self):
            yield AbominationBody
            yield AbominationPsyche
