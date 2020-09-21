from providers.data_manager import DataManager
from ..providers import ClothingDataProvider
from ..sample_data.genders import DEFAULT


class ClothingManager(DataManager):
    def __init__(self, provider=None):
        super().__init__(provider or ClothingDataProvider())

    @classmethod
    def by_gender(cls, gender=None):
        return cls.get_provider().by_gender(gender or DEFAULT).data
