from providers.data_manager import DataManager
from generated.history import Timeline
from .provider import DataProvider


class TimelineManager(DataManager):
    def __init__(self, provider=None):
        super().__init__(provider or DataProvider)

    @classmethod
    def timeline(cls):
        return Timeline(*cls.get_provider().timeline)
