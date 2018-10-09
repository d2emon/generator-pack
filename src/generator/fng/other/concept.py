from generator.generator.generated import ListGenerated, ComplexGenerated
from generator.generator.data_provider import FileProvider


class BaseConcept(ListGenerated):
    providers = dict()

    def __init__(self, first="", last=""):
        super().__init__()
        self.first = first
        self.last = last

    def __str__(self):
        return "{} {}".format(self.first, self.last)

    @classmethod
    def generate(cls):
        next_data = {key: next(d) for key, d in cls.providers.items()}
        return cls(**next_data)


class BaseArtConcept(BaseConcept):
    pass


class BaseStoryConcept(BaseConcept):
    pass


class ArtConceptPlace(BaseArtConcept):
    providers = {
        'first': FileProvider("data/concept/art/place1.txt"),
        'last': FileProvider("data/concept/art/place2.txt"),
    }


class ArtConceptBeing(BaseArtConcept):
    providers = {
        'first': FileProvider("data/concept/art/being1.txt"),
        'last': FileProvider("data/concept/art/being2.txt"),
    }


class StoryConceptCharacter(BaseStoryConcept):
    providers = {
        'first': FileProvider("data/concept/story/character1.txt"),
        'last': FileProvider("data/concept/story/character2.txt"),
    }


class StoryConceptEvent(BaseStoryConcept):
    providers = {
        'first': FileProvider("data/concept/story/event1.txt"),
        'last': FileProvider("data/concept/story/event2.txt"),
    }


class ArtConcept(ComplexGenerated):
    generators = {
        50: ArtConceptBeing,
        100: ArtConceptPlace,
    }


class StoryConcept(ComplexGenerated):
    generators = {
        50: StoryConceptCharacter,
        100: StoryConceptEvent,
    }
