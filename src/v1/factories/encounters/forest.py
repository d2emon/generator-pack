from v1.fixtures.encounters import encounters
from .factory import EncounterFactory


class ForestEncounterFactory(EncounterFactory):
    default_data = encounters.get('forest', [])
