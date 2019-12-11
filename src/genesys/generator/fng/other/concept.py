from genesys.generator import ListGenerated, ComplexGenerated
from genesys.generator import ListProvider, ProvidersList


from fixtures.other import beings, places
from fixtures.other import characters, events


class BaseConcept(ListGenerated):
    pass


class ArtConceptPlace(BaseConcept):
    provider = ProvidersList(*[ListProvider(provider) for provider in places])


class ArtConceptBeing(BaseConcept):
    provider = ProvidersList(*[ListProvider(provider) for provider in beings])


class StoryConceptCharacter(BaseConcept):
    provider = ProvidersList(*[ListProvider(provider) for provider in characters])


class StoryConceptEvent(BaseConcept):
    provider = ProvidersList(*[ListProvider(provider) for provider in events])


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
