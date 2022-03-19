from v1.factories.factory import Factory
from v1.models.encounters import Encounter, Item


class EncounterFactory(Factory):
    model = Encounter


class ItemFactory(Factory):
    model = Item
