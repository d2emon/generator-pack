from genesys.and_why.factories.clothing import ClothingFactory
from genesys.and_why.factories.doll import DollFactory
from genesys.and_why.factories.gender import GenderFactory
from genesys.and_why.factories.slot import SlotFactory
from utils.genders import MALE, FEMALE


GENDERS = (
    None,
    MALE,
    FEMALE,
)
MODELS_COUNT = 5
CHANGE_COUNT = 5

if __name__ == "__main__":
    clothing_factory = ClothingFactory()
    doll_factory = DollFactory()
    slot_factory = SlotFactory()

    for gender in GENDERS:
        for _ in range(MODELS_COUNT):
            slot = slot_factory(gender=gender)
            doll = doll_factory(gender=gender)

            print()
            print("Slot", gender, list(slot))

            print()
            print('Doll', gender, repr(doll))

            for _ in range(CHANGE_COUNT):
                print()
                clothing = clothing_factory(gender=gender)
                for item in clothing:
                    doll.put_on(item)
                print(doll.slots)
