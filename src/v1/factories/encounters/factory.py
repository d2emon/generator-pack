from v1.factories.factory import Factory
from v3.models.encounter_model import Encounter, Item


class EncounterFactory(Factory):
    model = Encounter


class ItemFactory(Factory):
    model = Item
