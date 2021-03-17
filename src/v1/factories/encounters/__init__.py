from v1.fixtures.encounters import encounters
from .factory import EncounterFactory


class CaveEncounterFactory(EncounterFactory):
    default_data = encounters.get('cave', [])
