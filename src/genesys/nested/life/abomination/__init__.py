from models.v5 import life
from utils.nested import select_item
from ..human.person import PersonFactory
from ..human.body import BodyFactory
from ..human.torso import TorsoFactory, ChestFactory, PelvisFactory
from ..human.head import HeadFactory, HeadHairFactory
from ..human.head.ear import EarFactory
from ..human.head.eye import EyeFactory
from ..human.head.mouth import MouthFactory
from ..human.head.nose import NoseFactory
from ..human.head.skull import SkullFactory
from ..human.arm import ArmFactory
from ..human.leg import LegFactory

# ???
from ..animals.insect import StingerFactory
# ???
from ..animals.crustacean import CrustaceanClawFactory
# ???
from ...mind import PsycheFactory, ThoughtsFactory, ThoughtFactory
# ???
from ..body.body_parts import WeirdSoftOrganFactory, WeirdHardOrganFactory


class AbominationTorsoFactory(TorsoFactory):
    model = life.AbominationTorso

    @classmethod
    def chest(cls):
        yield ChestFactory.one()
        yield ChestFactory.probable(10)

    @classmethod
    def pelvis(cls):
        yield PelvisFactory.one()
        yield PelvisFactory.probable(10)

    def children(self):
        yield WeirdSoftOrganFactory.probable(20)
        yield WeirdHardOrganFactory.probable(20)
        yield super().children()


class AbominationHeadFactory(HeadFactory):
    model = life.AbominationHead

    @classmethod
    def mouth(cls):
        yield MouthFactory.multiple(0, 2)

    @classmethod
    def nose(cls):
        yield NoseFactory.multiple(0, 2)

    @classmethod
    def eyes(cls):
        yield EyeFactory.multiple(0, 8)

    @classmethod
    def ears(cls):
        yield EarFactory.multiple(0, 4)

    @classmethod
    def skull(cls):
        yield SkullFactory.probable(90)

    @classmethod
    def fur(cls):
        yield HeadHairFactory.probable(65)

    def children(self):
        yield WeirdSoftOrganFactory.probable(20)
        yield WeirdHardOrganFactory.probable(20)
        yield super().children()


class AbominationBodyFactory(BodyFactory):
    model = life.AbominationBody

    def children(self):
        yield AbominationHeadFactory.one()
        yield AbominationHeadFactory.probable(5)
        yield AbominationTorsoFactory.one()
        yield select_item(
            ArmFactory.multiple(0, 8),
            ArmFactory.multiple(0, 4),
        )
        yield select_item(
            LegFactory.multiple(0, 8),
            LegFactory.multiple(0, 4),
        )
        yield CrustaceanClawFactory.probable(2)
        yield StingerFactory.probable(2)
        yield WeirdSoftOrganFactory.probable(10)
        yield WeirdSoftOrganFactory.probable(10)
        yield WeirdHardOrganFactory.probable(10)
        yield WeirdHardOrganFactory.probable(10)


class AbominationThoughtFactory(ThoughtFactory):
    def get_thoughts(self, data=None):
        data_source = data or self.data
        return data_source.abomination_thought


class AbominationThoughtsFactory(ThoughtsFactory):
    @classmethod
    def thoughts(cls):
        yield AbominationThoughtFactory.one()


class AbominationPsycheFactory(PsycheFactory):
    @property
    def thoughts_factory(self):
        return AbominationThoughtsFactory.one()


class AbominationFactory(PersonFactory):
    model = life.Abomination
    default_name = '*PERSON*| (abomination)'

    @property
    def body_factory(self):
        return AbominationBodyFactory.one()

    @property
    def psyche_factory(self):
        return AbominationPsycheFactory.one()

    @property
    def clothing_set_factory(self):
        return None


FACTORIES = {
    'abomination': AbominationFactory,
    # nonononononono
    'abomination psyche': AbominationPsycheFactory,
    'abomination thoughts': AbominationThoughtsFactory,
    'abomination thought': AbominationThoughtFactory,
    'abomination body': AbominationBodyFactory,
    'abomination head': AbominationHeadFactory,
    'abomination torso': AbominationTorsoFactory,
}
