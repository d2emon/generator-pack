from generated import life
from ...mind import PsycheFactory, ThoughtsFactory, ThoughtFactory
from ..animal_body import WeirdSoftOrganFactory, WeirdHardOrganFactory, CrustaceanClawFactory, StingerFactory, \
    MouthFactory, NoseFactory, EarFactory, EyeFactory, SkullFactory
from ..body.person import PersonFactory
from ..body.body import BodyFactory
from ..body.torso import TorsoFactory, ChestFactory, PelvisFactory
from ..body.head import HeadFactory, HeadHairFactory
from ..body.arm import ArmFactory
from ..body.leg import LegFactory


class AbominationTorsoFactory(TorsoFactory):
    default_model = life.AbominationTorso

    @classmethod
    def chest(cls):
        yield ChestFactory()
        yield ChestFactory().probable(10)

    @classmethod
    def pelvis(cls):
        yield PelvisFactory()
        yield PelvisFactory().probable(10)

    def children(self):
        yield WeirdSoftOrganFactory().probable(20)
        yield WeirdHardOrganFactory().probable(20)
        yield super().children()


class AbominationHeadFactory(HeadFactory):
    default_model = life.AbominationHead

    @classmethod
    def mouth(cls):
        yield MouthFactory().multiple(0, 2)

    @classmethod
    def nose(cls):
        yield NoseFactory().multiple(0, 2)

    @classmethod
    def eyes(cls):
        yield EyeFactory().multiple(0, 8)

    @classmethod
    def ears(cls):
        yield EarFactory().multiple(0, 4)

    @classmethod
    def skull(cls):
        yield SkullFactory().probable(90)

    @classmethod
    def fur(cls):
        yield HeadHairFactory().probable(65)

    def children(self):
        yield WeirdSoftOrganFactory().probable(20)
        yield WeirdHardOrganFactory().probable(20)
        yield super().children()


class AbominationBodyFactory(BodyFactory):
    default_model = life.AbominationBody

    def children(self):
        yield AbominationHeadFactory()
        yield AbominationHeadFactory().probable(5)
        yield AbominationTorsoFactory()
        yield self.select_item(
            ArmFactory().multiple(0, 8),
            ArmFactory().multiple(0, 4),
        )
        yield self.select_item(
            LegFactory().multiple(0, 8),
            LegFactory().multiple(0, 4),
        )
        yield CrustaceanClawFactory().probable(2)
        yield StingerFactory().probable(2)
        yield WeirdSoftOrganFactory().probable(10)
        yield WeirdSoftOrganFactory().probable(10)
        yield WeirdHardOrganFactory().probable(10)
        yield WeirdHardOrganFactory().probable(10)


class AbominationThoughtFactory(ThoughtFactory):
    thoughts = [
        "P-please...", "Don't look at me...", "Please... kill me...", "Kill... me...",
        "Why would I ever ask for this...", "I only wish for death.", "I only long for death now.",
        "I only demand... death...", "End my misery... I beg you...", "This is a mockery of existence...",
        "I miss her so much...", "I miss him so much...", "I miss my family...", "Why would they do that to me...",
        "How could they do this to me...", "What have I become...", "I feel... different...",
        "I can't feel... anything...", "I can't... see anything...",
    ]


class AbominationThoughtsFactory(ThoughtsFactory):
    @classmethod
    def thoughts(cls):
        yield AbominationThoughtFactory()


class AbominationPsycheFactory(PsycheFactory):
    @property
    def thoughts_factory(self):
        return AbominationThoughtsFactory()


class AbominationFactory(PersonFactory):
    default_model = life.Abomination
    default_name = '*PERSON*| (abomination)'

    @property
    def body_factory(self):
        return AbominationBodyFactory()

    @property
    def psyche_factory(self):
        return AbominationPsycheFactory()

    @property
    def clothing_set_factory(self):
        return None
