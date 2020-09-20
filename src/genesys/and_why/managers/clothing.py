from providers.data_manager import DataManager


class ClothingManager(DataManager):
    @classmethod
    def by_gender(cls, gender):
        return cls.get_provider().gender_factory(gender).data
