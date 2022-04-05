from genesys.encounters.encounters.environmental import encounters
from genesys.encounters.encounters.items import items
from .factory import EncounterFactory, ItemFactory


class ClericItemFactory(ItemFactory):
    default_data = items.get('cleric', [])


class ArmorFactory(ItemFactory):
    default_data = items.get('armor', [])


class CaveEncounterFactory(EncounterFactory):
    default_data = encounters.get('cave', [])


class ForestEncounterFactory(EncounterFactory):
    default_data = encounters.get('forest', [])
