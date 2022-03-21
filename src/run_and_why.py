from genesys.and_why import factories
from utils.genders import MALE, FEMALE


if __name__ == "__main__":
    clothing_factory = factories.ClothingFactory()

    clothing = clothing_factory(gender=MALE)
    print(list(clothing))

    clothing = clothing_factory(gender=FEMALE)
    print(list(clothing))
