from factories.factory import Factory
from models.encounters.encounter_model import Encounter, Item


class EncounterFactory(Factory):
    model = Encounter


class ItemFactory(Factory):
    model = Item
