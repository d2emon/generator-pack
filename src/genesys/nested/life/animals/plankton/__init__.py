from models.v5 import life
from ....mind import ThoughtFactory, ThoughtsFactory, PsycheFactory
from ...body.head import SimpleEyeFactory, SimpleMouthFactory
from ...body.skin import ExoskeletonFactory
from ...body.jelly import JellyFactory
from ...body.body_parts import SoftFleshFactory
from ..animal import AnimalFactory, AnimalBodyFactory


class PlanktonBodyFactory(AnimalBodyFactory):
    default_model = life.PlanktonBody

    @classmethod
    def eyes(cls):
        yield from SimpleEyeFactory().multiple(0, 3)

    @classmethod
    def mouth(cls):
        yield SimpleMouthFactory()

    @classmethod
    def skin(cls):
        yield ExoskeletonFactory()

    @classmethod
    def flesh(cls):
        yield JellyFactory()
        yield SoftFleshFactory()


class PlanktonThoughtFactory(ThoughtFactory):
    thoughts = [
        "hello :)", "yes hi :)", "how are you :)", "it's sunny today :)", "what a nice day :)",
        "aaah I could just float away :)", "I am fine thank you :)", "yes I think so :)", "how fun :)",
        "do you catch my drift :)", "so many cousins :)", "I'm a little lost :)", "no pressure :)", "that's okay :)",
        "what a nice thing to say :)", "you should stay over :)", "my place or your place :)",
        "why are you still here :)", "there's a big world to explore :)", "I don't even know where I'm going :)",
        "here I go! :)", "am I really going where I decide to go, or am I just being pushed around by the current? :)",
        "oh no :(", "can't you feel them coming? :(", "they're slowly rising from deep below :(",
        "it's slowly coming this way :(", "I'm different :(", "ravioli, ravioli :)", "give me the formuoli :)",
        "oh,...",
    ]


class PlanktonThoughtsFactory(ThoughtsFactory):
    black_hole_probability = 0

    @classmethod
    def thoughts(cls):
        yield PlanktonThoughtFactory().multiple(1)


class PlanktonPsycheFactory(PsycheFactory):
    @property
    def thoughts_factory(self):
        return PlanktonThoughtsFactory()

    @property
    def memories_factory(self):
        return None


class PlanktonFactory(AnimalFactory):
    default_model = life.Plankton
    names = [
        "jellyfish larva", "coral polyp", "diatom", "urchin larva", "starfish larva", "salp", "rotifer", "pteropod",
        "clione",
    ]

    @property
    def body_factory(self):
        return PlanktonBodyFactory()

    @property
    def psyche_factory(self):
        return PlanktonPsycheFactory()
