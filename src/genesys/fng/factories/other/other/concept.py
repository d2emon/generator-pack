from factories.providers.list_provider import ComplexFactory
from factories.generator import ListGenerated, ComplexGenerated

from genesys.fixtures.fixtures import beings, places, characters, events


class BaseConcept(ListGenerated):
    pass


class ArtConceptPlace(BaseConcept):
    provider = ComplexFactory.from_lists(places)


class ArtConceptBeing(BaseConcept):
    provider = ComplexFactory.from_lists(beings)


class StoryConceptCharacter(BaseConcept):
    provider = ComplexFactory.from_lists(characters)


class StoryConceptEvent(BaseConcept):
    provider = ComplexFactory.from_lists(events)


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
