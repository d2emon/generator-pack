import sample_data
from models.and_why import Doll as DollModel, genders
from models.data_item import DataItem


class Doll(DollModel):
    class Genders:
        MALE = genders.MALE
        FEMALE = genders.FEMALE

    @classmethod
    def get_clothing(cls, gender):
        return [item.value for item in DataItem.get_by_group(gender)]

    def fill(self, items=None):
        if items is None:
            items = self.get_clothing(self.gender)
        super().fill(items)
