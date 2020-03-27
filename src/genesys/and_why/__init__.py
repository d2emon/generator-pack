from models.and_why import Doll as DollModel
from models.data_item import DataItem
from sample_data.and_why import groups
from . import genders


print(groups.MALE)


class ClothingItem(DataItem):
    GROUPS = {
        genders.MALE: groups.MALE,
        genders.FEMALE: groups.FEMALE,
    }

    @classmethod
    def by_gender(cls, gender):
        group_id = cls.GROUPS.get(gender)
        return [item.value for item in cls.get_by_group(group_id)]


class Doll(DollModel):
    def fill(self, items=None):
        if items is None:
            items = ClothingItem.by_gender(self.gender)
        super().fill(items)
