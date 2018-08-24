from generator.generator import ListGenerator, PercentedGenerator
from generator.generator.generated import Generated
from generator.generator.generator_data import FileData


class ArtConcept(Generated):
    title = "ArtConcept"


class StoryConcept(Generated):
    title = "StoryConcept"


class BaseArtConceptGenerator(ListGenerator):
    generated_class = ArtConcept
    template = "{first} {last}"


class ArtConceptPlaceGenerator(BaseArtConceptGenerator):
    data = {
        'first': FileData("data/art-concept/place1.txt"),
        'last': FileData("data/art-concept/place2.txt"),
    }


class ArtConceptBeingGenerator(BaseArtConceptGenerator):
    data = {
        'first': FileData("data/art-concept/being1.txt"),
        'last': FileData("data/art-concept/being2.txt"),
    }


class ArtConceptGenerator(PercentedGenerator):
    subgenerators = {
        50: ArtConceptBeingGenerator,
        100: ArtConceptPlaceGenerator,
    }


class BaseStoryConceptGenerator(ListGenerator):
    generated_class = StoryConcept
    template = "{first} {last}"


class StoryConceptCharacterGenerator(BaseStoryConceptGenerator):
    data = {
        'first': FileData("data/story-concept/character1.txt"),
        'last': FileData("data/story-concept/character2.txt"),
    }


class StoryConceptEventGenerator(BaseStoryConceptGenerator):
    data = {
        'first': FileData("data/story-concept/event1.txt"),
        'last': FileData("data/story-concept/event2.txt"),
    }


class StoryConceptGenerator(PercentedGenerator):
    subgenerators = {
        50: StoryConceptCharacterGenerator,
        100: StoryConceptEventGenerator,
    }
