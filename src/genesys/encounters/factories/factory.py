from factories.factory import Factory
from models.encounters import Encounter
from models.item import Item


class EncounterFactory(Factory):
    model = Encounter


class ItemFactory(Factory):
    model = Item
