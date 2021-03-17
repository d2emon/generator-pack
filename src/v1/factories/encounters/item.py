from v1.fixtures.encounters.items import items
from v1.models.encounters import Item
from .factory import EncounterFactory


class ItemFactory(EncounterFactory):
    model_class = Item


class ClericItemFactory(ItemFactory):
    default_data = items.get('cleric', [])
