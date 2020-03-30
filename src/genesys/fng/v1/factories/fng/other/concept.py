from factories.providers import ComplexProvider, ListProvider
from factories.generator import ListGenerated, ComplexGenerated

from sample_data.fixtures import beings, places
from sample_data.fixtures import characters, events


class BaseConcept(ListGenerated):
    pass


class ArtConceptPlace(BaseConcept):
    provider = ComplexProvider(*[ListProvider(provider) for provider in places])


class ArtConceptBeing(BaseConcept):
    provider = ComplexProvider(*[ListProvider(provider) for provider in beings])


class StoryConceptCharacter(BaseConcept):
    provider = ComplexProvider(*[ListProvider(provider) for provider in characters])


class StoryConceptEvent(BaseConcept):
    provider = ComplexProvider(*[ListProvider(provider) for provider in events])


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
