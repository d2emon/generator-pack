import random
from .body import Chest, Thighs, Legs, Feet


GENDER_MALE = 0
GENDER_FEMALE = 1


names = (
    "Name",
)


class Paperdoll:
    def __init__(self, cloths=()):
        self.parts = {
            Chest: dict(),
            Thighs: dict(),
            Legs: dict(),
            Feet: dict(),
        }

        for cloth in cloths:
            self.wear(cloth)

    def wearing(self, part, take_off=False):
        cloths = self.parts.get(part)
        if len(cloths) < 1:
            return None

        orders = list(cloths.keys())
        orders.sort(reverse=True)
        result = cloths[orders[0]]
        if take_off:
            del cloths[orders[0]]
        return result

    def wear(self, cloth):
        for part in cloth.parts:
            self.parts[part][cloth.order] = cloth


class Person(Paperdoll):
    gender = None

    def __init__(self, name=None, hair=None, cloths=()):
        super().__init__(cloths)

        self.name = name or random.choice(names)
        self.hair = hair or random.choice(hair_colors)


class Girl(Person):
    gender = GENDER_FEMALE
