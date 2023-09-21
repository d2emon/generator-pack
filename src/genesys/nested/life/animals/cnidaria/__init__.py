from models.v5 import life
from utils.nested import select_item
from ....mind import ThoughtFactory, ThoughtsFactory, PsycheFactory
from ...body.head import SimpleMouthFactory
from ...body.jelly import JellyFactory
from ...body.body_parts import SoftFleshFactory
from ..animal import AnimalFactory, AnimalBodyFactory


class CnidariaBodyFactory(AnimalBodyFactory):
    default_model = life.CnidariaBody

    @classmethod
    def eyes(cls):
        yield None

    @classmethod
    def mouth(cls):
        yield SimpleMouthFactory()

    @classmethod
    def skin(cls):
        yield None

    @classmethod
    def flesh(cls):
        yield JellyFactory()
        yield SoftFleshFactory()


class CnidariaThoughtFactory(ThoughtFactory):
    part1 = ["shhhhl", "shhl", "schllll", "gl", "schgl", "gbl", "swwwl"]
    part2 = ["urp", "orp", "arp", "urps", "orpsss"]

    def generate_name(self):
        return f'{select_item(*self.part1)}{select_item(*self.part2)}'


class CnidariaThoughtsFactory(ThoughtsFactory):
    black_hole_probability = 0

    @classmethod
    def thoughts(cls):
        yield CnidariaThoughtFactory().multiple(1)


class CnidariaPsycheFactory(PsycheFactory):
    @property
    def thoughts_factory(self):
        return CnidariaThoughtsFactory()

    @property
    def memories_factory(self):
        return None


class CnidariaFactory(AnimalFactory):
    default_model = life.Cnidaria
    names = [
        "urchin", "starfish", "sea cucumber", "sea anemon", "coral", "box jelly", "jellyfish", "hydra", "man'o'war",
        "sponge", "sea nettle", "siphonophore", "ctenophore", "tunicate", "trichordate",
    ]
    # urchins and starfish and sponges are unrelated to cnidarians but I don't really care

    @property
    def body_factory(self):
        return CnidariaBodyFactory()

    @property
    def psyche_factory(self):
        return CnidariaPsycheFactory()
