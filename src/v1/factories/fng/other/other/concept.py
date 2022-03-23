from providers.list_provider import ListProvider
from factories.generator import ListGenerated, ComplexGenerated

from genesys.fixtures.fixtures import beings, places, characters, events


class BaseConcept(ListGenerated):
    pass


class ArtConceptPlace(BaseConcept):
    provider = ListProvider.multiple(places)


class ArtConceptBeing(BaseConcept):
    provider = ListProvider.multiple(beings)


class StoryConceptCharacter(BaseConcept):
    provider = ListProvider.multiple(characters)


class StoryConceptEvent(BaseConcept):
    provider = ListProvider.multiple(events)


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
