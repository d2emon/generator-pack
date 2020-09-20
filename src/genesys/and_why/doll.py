from .models import DollModel
from .managers.clothing import ClothingManager


class Doll(DollModel):
    def fill(self, items=None):
        super().fill(items or ClothingManager.by_gender(self.gender))
