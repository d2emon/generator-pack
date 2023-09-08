from models.v5 import life
from factories.thing.nested_factory import NestedFactory as Factory
from ....materials import ChitinFactory
from ....mind import ThoughtFactory, ThoughtsFactory, PsycheFactory
from ...animal_body.head import SimpleEyeFactory, BrainFactory
from ...animal_body.skin import ExoskeletonFactory
from ...animal_body.body_parts import SoftFleshFactory
from ...animal_body.skeleton import MuscleFactory, FatFactory
from ..animal import AnimalFactory, AnimalBodyFactory


class CrustaceanLegFactory(Factory):
    default_model = life.CrustaceanLeg

    def children(self):
        yield ChitinFactory()
        yield MuscleFactory()
        yield FatFactory()


class CrustaceanClawFactory(CrustaceanLegFactory):
    default_model = life.CrustaceanClaw


class CrustaceanShellFactory(ExoskeletonFactory):
    default_model = life.CrustaceanShell


class CrustaceanBodyFactory(AnimalBodyFactory):
    default_model = life.CrustaceanBody

    @classmethod
    def eyes(cls):
        yield from SimpleEyeFactory().multiple(2, 6)

    @classmethod
    def mouth(cls):
        yield from CrustaceanClawFactory().multiple(2)

    @classmethod
    def skin(cls):
        yield CrustaceanShellFactory()

    @classmethod
    def flesh(cls):
        yield BrainFactory()
        yield from CrustaceanLegFactory().multiple(6, 8)
        yield SoftFleshFactory()


class CrustaceanThoughtFactory(ThoughtFactory):
    thoughts = [
        "skitter skitter", "crawl crawl", "dig dig", "grab grab", "gotta eat", "gotta skitter", "gotta catch food",
        "gotta hide", "gotta breed", "breed breed", "under the sea",
    ]


class CrustaceanThoughtsFactory(ThoughtsFactory):
    black_hole_probability = 0

    @classmethod
    def thoughts(cls):
        yield CrustaceanThoughtFactory().multiple(2, 3)


class CrustaceanPsycheFactory(PsycheFactory):
    @property
    def thoughts_factory(self):
        return CrustaceanThoughtsFactory()

    @property
    def memories_factory(self):
        return None


class CrustaceanFactory(AnimalFactory):
    default_model = life.Crustacean
    names = [
        "shrimp", "prawn", "langoustine", "lobster", "rock lobster", "crab", "spider crab", "crayfish", "krill",
        "triops", "copepod",
    ]

    @property
    def body_factory(self):
        return CrustaceanBodyFactory()

    @property
    def psyche_factory(self):
        return CrustaceanPsycheFactory()
