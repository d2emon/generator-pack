from models.v5 import life
from ....mind import ThoughtFactory, ThoughtsFactory, PsycheFactory
from ...animal_body.head import SimpleEyeFactory, MouthFactory
from ...animal_body.limb import TentacleFactory
from ...animal_body.jelly import JellyFactory
from ...animal_body.body_parts import SoftFleshFactory
from ..animal import AnimalFactory, AnimalBodyFactory


class MolluskBodyFactory(AnimalBodyFactory):
    default_model = life.MolluskBody

    @classmethod
    def eyes(cls):
        yield from SimpleEyeFactory().multiple(2)

    @classmethod
    def mouth(cls):
        yield MouthFactory()
        yield from TentacleFactory().multiple(6, 8)

    @classmethod
    def skin(cls):
        yield None

    @classmethod
    def flesh(cls):
        yield JellyFactory()
        yield SoftFleshFactory()


class MolluskThoughtFactory(ThoughtFactory):
    thoughts = [
        "party time", "is it party time now", "party now ok", "party's over", "okay let's party", "ready to party",
        "are you party", "they don't look like they want to party", "is the party over",
        "this party's so hot it's stupid", "this party getting crazy", "partyyyyyyy", "chug chug chug", "we party now",
        "wanna join in", "we partyin", "okay too much party", "I have a secret for you", "that's a secret",
        "I kinda like partying", "party yes nice", "woooo party",
    ]


class MolluskThoughtsFactory(ThoughtsFactory):
    black_hole_probability = 0

    @classmethod
    def thoughts(cls):
        yield MolluskThoughtFactory().multiple(2)


class MolluskPsycheFactory(PsycheFactory):
    @property
    def thoughts_factory(self):
        return MolluskThoughtsFactory()

    @property
    def memories_factory(self):
        return None


class MolluskFactory(AnimalFactory):
    default_model = life.Mollusk
    names = [
        "sea slug", "sea snail", "squid", "octopus", "vampire squid", "clione", "sea angel", "cuttlefish", "nautilus",
        "giant squid", "colossal squid", "mimic octopus",
    ]

    @property
    def body_factory(self):
        return MolluskBodyFactory()

    @property
    def psyche_factory(self):
        return MolluskPsycheFactory()
