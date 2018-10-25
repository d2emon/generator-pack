import random
from .body import Chest, Thighs, Legs, Feet


GENDER_MALE = 0
GENDER_FEMALE = 1


names = (
    "Name",
)


class Paperdoll:
    def __init__(self, cloths=()):
        self.cloths = list(cloths)

    def wearing(self, part, take_off=False):
        cloths = self.sorted.get(part)
        if len(cloths) < 1:
            return None

        orders = list(cloths.keys())
        orders.sort(reverse=True)
        result = cloths[orders[0]]
        if take_off:
            del self.cloths[self.cloths.index(result)]
        return result

    @property
    def sorted(self):
        parts = {
            Chest: dict(),
            Thighs: dict(),
            Legs: dict(),
            Feet: dict(),
        }
        for cloth in self.cloths:
            for part in cloth.parts:
                parts[part][cloth.order] = cloth
        return parts


class Hair:
    def __init__(self):
        self.color = None


class Eyes:
    def __init__(self):
        self.color = None


class Person(Paperdoll):
    gender = None

    def __init__(self, name=None, hair=None, cloths=()):
        super().__init__(cloths)

        self.name = name or random.choice(names)
        self.hair = Hair()
        self.eyes = Eyes()

    def set_hair(self, color=None):
        self.hair.color = color or random.choice(hair_colors)

    def set_eyes(self, color=None):
        self.eyes.color = color or random.choice(hair_colors)


class Girl(Person):
    gender = GENDER_FEMALE
