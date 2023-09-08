from genesys.dndspeak import dndspeak
from factories.data_item_factory import DataItemFactory
from data.dndspeak import groups
from .data_manager import DataManager


class EncounterManager(DataManager):
    class DataProvider:
        def __init__(self):
            self.__desert_encounters = DataItemFactory(groups.DESERT_ENCOUNTERS)
            self.__sailing_conditions = DataItemFactory(groups.DESERT_ENCOUNTERS)

        @property
        def desert_encounters(self):
            return self.__desert_encounters

        @property
        def sailing_conditions(self):
            return self.__sailing_conditions

    @classmethod
    def desert_encounter(cls):
        return dndspeak.DesertEncounter(next(cls.get_provider().desert_encounters))

    @classmethod
    def sailing_conditions(cls):
        return dndspeak.SailingConditions(next(cls.get_provider().sailing_conditions))
