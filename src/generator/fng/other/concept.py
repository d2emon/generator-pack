from generator.generator.generated import ListGenerated, ComplexGenerated
from generator.generator.generator_data import FileData


class BaseConcept(ListGenerated):
    def __init__(self, first="", last=""):
        super().__init__()
        self.first = first
        self.last = last

    def __str__(self):
        return "{} {}".format(self.first, self.last)


class BaseArtConcept(BaseConcept):
    pass


class BaseStoryConcept(BaseConcept):
    pass


class ArtConceptPlace(BaseArtConcept):
    data = {
        'first': FileData("data/concept/art/place1.txt"),
        'last': FileData("data/concept/art/place2.txt"),
    }


class ArtConceptBeing(BaseArtConcept):
    data = {
        'first': FileData("data/concept/art/being1.txt"),
        'last': FileData("data/concept/art/being2.txt"),
    }


class StoryConceptCharacter(BaseStoryConcept):
    data = {
        'first': FileData("data/concept/story/character1.txt"),
        'last': FileData("data/concept/story/character2.txt"),
    }


class StoryConceptEvent(BaseStoryConcept):
    data = {
        'first': FileData("data/concept/story/event1.txt"),
        'last': FileData("data/concept/story/event2.txt"),
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
