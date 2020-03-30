from models import dndspeak
from models.data_manager import DataManager
from providers.data_item import DataItemProvider
from sample_data.dndspeak import groups


class EncounterManager(DataManager):
    class DataProvider(DataManager.DataProvider):
        def __init__(self):
            self.__desert_encounters = DataItemProvider(groups.DESERT_ENCOUNTERS)
            self.__sailing_conditions = DataItemProvider(groups.DESERT_ENCOUNTERS)

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
