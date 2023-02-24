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

def show_model(item):
    return item.data


def show_item(item):
    return item


def show_items(item):
    return list(item)


def show_factory(factory_class, view):
    factory = factory_class()
    print(factory_class.__name__)

    for gender in GENDERS:
        item = factory(gender=gender)
        print('\t', gender)
        print('\t\t', repr(item))
        print('\t\t', view(item))


if __name__ == "__main__":
    show_factory(ClothingFactory, show_items)
    show_factory(DollFactory, show_model)
    show_factory(GenderFactory, show_item)
    show_factory(SlotFactory, show_items)
