from factories.factory import Factory
from models.encounters import Encounter
from models.model import Model


class EncounterFactory(Factory):
    model = Encounter


class ItemFactory(Factory):
    model = Model
