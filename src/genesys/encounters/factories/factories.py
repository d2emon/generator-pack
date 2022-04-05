from factories.model_factory import ModelFactory
from ..encounters.environmental import encounters
from ..encounters.items import items
from ..models import Encounter, Item


class EncounterFactory(ModelFactory):
    model = Encounter


class ItemFactory(ModelFactory):
    model = Item


class ClericItemFactory(ItemFactory):
    def __init__(self, data=None):
        super().__init__(data or items.get('cleric', []))


class ArmorFactory(ItemFactory):
    def __init__(self, data=None):
        super().__init__(data or items.get('armor', []))


class CaveEncounterFactory(EncounterFactory):
    def __init__(self, data=None):
        super().__init__(data or encounters.get('cave', []))


class ForestEncounterFactory(EncounterFactory):
    def __init__(self, data=None):
        super().__init__(data or encounters.get('forest', []))
