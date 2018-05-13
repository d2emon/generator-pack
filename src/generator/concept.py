from .generator import DataGenerator, PercentedGenerator
from .generator.template import GeneratorTemplate
from .generator.generated import Generated


class ArtConcept(Generated):
    title = "ArtConcept"


class StoryConcept(Generated):
    title = "StoryConcept"

class BaseArtConceptGenerator(DataGenerator):
    generated_class = ArtConcept


class ArtConceptPlaceGenerator(BaseArtConceptGenerator):
    @classmethod
    def generate_value(cls, *args, **kwargs):
        return GeneratorTemplate.generate([
            "data/art-concept/place1.txt",
            "data/art-concept/place2.txt",
        ])


class ArtConceptBeingGenerator(BaseArtConceptGenerator):
    @classmethod
    def generate_value(cls, *args, **kwargs):
        return GeneratorTemplate.generate([
            "data/art-concept/being1.txt",
            "data/art-concept/being2.txt",
        ])


class ArtConceptGenerator(PercentedGenerator):
    subgenerators = {
        50: ArtConceptBeingGenerator,
        100: ArtConceptPlaceGenerator,
    }


class BaseStoryConceptGenerator(DataGenerator):
    generated_class = StoryConcept


class StoryConceptCharacterGenerator(BaseStoryConceptGenerator):
    @classmethod
    def generate_value(cls, *args, **kwargs):
        return GeneratorTemplate.generate([
            "data/story-concept/character1.txt",
            "data/story-concept/character2.txt",
        ])


class StoryConceptEventGenerator(BaseStoryConceptGenerator):
    @classmethod
    def generate_value(cls, *args, **kwargs):
        return GeneratorTemplate.generate([
            "data/story-concept/event1.txt",
            "data/story-concept/event2.txt",
        ])


class StoryConceptGenerator(PercentedGenerator):
    subgenerators = {
        50: StoryConceptCharacterGenerator,
        100: StoryConceptEventGenerator,
    }
