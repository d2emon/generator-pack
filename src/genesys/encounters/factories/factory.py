from factories.factory import Factory
from models.encounters.encounter import Encounter
from models.item import Item


class EncounterFactory(Factory):
    model = Encounter


class ItemFactory(Factory):
    model = Item
