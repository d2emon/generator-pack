from providers.data_manager import DataManager
from .provider import DataProvider
from .model import TimelineModel


class TimelineManager(DataManager):
    def __init__(self, provider=None):
        super().__init__(provider or DataProvider)

    @classmethod
    def timeline(cls):
        return TimelineModel(cls.get_provider().timeline)
