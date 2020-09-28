from generated import life
from ....factory import Factory
from ..person import PersonFactory
from ..body import BodyFactory
from ..torso import TorsoFactory, ChestFactory, PelvisFactory
from ..head import HeadFactory, MouthFactory, NoseFactory, EarFactory, EyeFactory, SkullFactory, HeadHairFactory
from ..arm import ArmFactory
from ..leg import LegFactory


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
        # yield WeirdSoftOrganFactory().probable(20)
        # yield WeirdHardOrganFactory().probable(20)
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
        yield HeadHairFactory().probable(65)

    def children(self):
        # yield WeirdSoftOrganFactory().probable(20)
        # yield WeirdHardOrganFactory().probable(20)
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
        # yield CrustaceanClawFactory().probable(2)
        # yield StingerFactory().probable(2)
        # yield WeirdSoftOrganFactory().probable(10)
        # yield WeirdSoftOrganFactory().probable(10)
        # yield WeirdHardOrganFactory().probable(10)
        # yield WeirdHardOrganFactory().probable(10)


class AbominationThoughtFactory(Factory):
    default_model = life.AbominationThought
    thoughts = [
        "P-please...", "Don't look at me...", "Please... kill me...", "Kill... me...",
        "Why would I ever ask for this...", "I only wish for death.", "I only long for death now.",
        "I only demand... death...", "End my misery... I beg you...", "This is a mockery of existence...",
        "I miss her so much...", "I miss him so much...", "I miss my family...", "Why would they do that to me...",
        "How could they do this to me...", "What have I become...", "I feel... different...",
        "I can't feel... anything...", "I can't... see anything...",
    ]

    def generate_name(self):
        return self.select_item(self.thoughts)


class AbominationThoughtsFactory(Factory):
    default_model = life.AbominationThoughts

    def children(self):
        from ....universe import BlackHoleFactory

        yield BlackHoleFactory().probable(0.01)
        yield AbominationThoughtFactory()


class AbominationPsycheFactory(Factory):
    default_model = life.AbominationPsyche

    def children(self):
        yield AbominationThoughtsFactory()
        # yield MemoriesFactory()


class AbominationFactory(PersonFactory):
    default_model = life.Abomination

    def children(self):
        yield AbominationBodyFactory()
        yield AbominationPsycheFactory()
