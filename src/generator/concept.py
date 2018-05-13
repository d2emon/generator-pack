from .generator import DataGenerator, PercentedGenerator
from .generator.template import GeneratorTemplate
from .generator.generated import Generated
from .generator.generator_data import FileData


class ArtConcept(Generated):
    title = "ArtConcept"


class StoryConcept(Generated):
    title = "StoryConcept"

class BaseConceptGenerator(DataGenerator):
    @classmethod
    def generate_value(cls, *args, **kwargs):
        return GeneratorTemplate.glue(cls.data_files, glue=" ")


class BaseArtConceptGenerator(BaseConceptGenerator):
    generated_class = ArtConcept


class ArtConceptPlaceGenerator(BaseArtConceptGenerator):
    data_files = [
        FileData("data/art-concept/place1.txt"),
        FileData("data/art-concept/place2.txt"),
    ]


class ArtConceptBeingGenerator(BaseArtConceptGenerator):
    data_files = [
        FileData("data/art-concept/being1.txt"),
        FileData("data/art-concept/being2.txt"),
    ]


class ArtConceptGenerator(PercentedGenerator):
    subgenerators = {
        50: ArtConceptBeingGenerator,
        100: ArtConceptPlaceGenerator,
    }


class BaseStoryConceptGenerator(BaseConceptGenerator):
    generated_class = StoryConcept


class StoryConceptCharacterGenerator(BaseStoryConceptGenerator):
    data_files = [
        FileData("data/story-concept/character1.txt"),
        FileData("data/story-concept/character2.txt"),
    ]


class StoryConceptEventGenerator(BaseStoryConceptGenerator):
    data_files = [
        FileData("data/story-concept/event1.txt"),
        FileData("data/story-concept/event2.txt"),
    ]


class StoryConceptGenerator(PercentedGenerator):
    subgenerators = {
        50: StoryConceptCharacterGenerator,
        100: StoryConceptEventGenerator,
    }
