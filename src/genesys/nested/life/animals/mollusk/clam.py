from models.v5 import life
from factories.nested_factory import NestedFactory as Factory
from ....materials import MoleculeFactory
from ....mind import ThoughtFactory, ThoughtsFactory, PsycheFactory
from ...animal_body.head import BrainFactory
from ...animal_body.body_parts import SoftFleshFactory
from ..animal import AnimalFactory, AnimalBodyFactory


class ClamShellFactory(Factory):
    default_model = life.ClamShell

    def children(self):
        yield MoleculeFactory.from_elements('Ca')


class ClamBodyFactory(AnimalBodyFactory):
    default_model = life.ClamBody

    @classmethod
    def eyes(cls):
        yield None

    @classmethod
    def mouth(cls):
        yield None

    @classmethod
    def skin(cls):
        yield ClamShellFactory()
        yield ClamShellFactory()

    @classmethod
    def flesh(cls):
        yield BrainFactory()
        yield SoftFleshFactory()


class ClamThoughtFactory(ThoughtFactory):
    thoughts = [
        "what", "wait", "hold on", "wait why", "i don't", "stay clam and carry on", "oh no", "why this", "that's",
        "no", "yes", "wait no", "but", "haha what", "please explain", "that's not", "i'm confused", "please why",
        "slurp", "okay", "okay what", "what is this", "what's that",
    ]


class ClamThoughtsFactory(ThoughtsFactory):
    black_hole_probability = 0

    @classmethod
    def thoughts(cls):
        yield ClamThoughtFactory().multiple(1, 3)


class ClamPsycheFactory(PsycheFactory):
    @property
    def thoughts_factory(self):
        return ClamThoughtsFactory()

    @property
    def memories_factory(self):
        return None


class ClamFactory(AnimalFactory):
    default_model = life.Clam
    names = ["oyster", "mussel", "scallop"]

    @property
    def body_factory(self):
        return ClamBodyFactory()

    @property
    def psyche_factory(self):
        return ClamPsycheFactory()
