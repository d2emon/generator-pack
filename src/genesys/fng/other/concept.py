from data.fixtures.fixtures import beings, places, characters, events
from factories.providers.list_provider import ComplexFactory
from models.fng.names.name import Name


class BaseConcept(Name):
    pass


class ArtConceptPlace(BaseConcept):
    provider = ComplexFactory.from_lists(places)


class ArtConceptBeing(BaseConcept):
    provider = ComplexFactory.from_lists(beings)


class StoryConceptCharacter(BaseConcept):
    provider = ComplexFactory.from_lists(characters)


class StoryConceptEvent(BaseConcept):
    provider = ComplexFactory.from_lists(events)


class ArtConcept(ComplexFactory):
    generators = {
        50: ArtConceptBeing,
        100: ArtConceptPlace,
    }


class StoryConcept(ComplexFactory):
    generators = {
        50: StoryConceptCharacter,
        100: StoryConceptEvent,
    }
